"""Inject scrollable-slide CSS into a Reveal.js HTML file produced by
`nbconvert --to slides`.

Reveal.js's default layout is a fixed 960x700 canvas scaled to fit the
viewport. Long lecture slides overflow that canvas and get clipped. The CSS
below converts each active slide into a single full-viewport scroll
container, top-aligned, with bottom padding so the last line isn't flush at
the viewport edge.

Usage:
    python inject_scrollable_css.py <path-to.slides.html>

Re-runs are safe: the injection is keyed by `id="scrollable-slides"` and
skipped if already present.

Used by both `DSA/render_preview.sh` (local preview) and
`publish-lecture-XX.sh` (website publish), so the preview and the published
site behave identically.
"""
import pathlib
import re
import sys

# Horizontal placement of the ~960px reading column: (margin-left, margin-right)
# for the column block. margin:auto centers a max-width block at ANY viewport
# (no viewport math), so it stays correct on low-res / mirrored projectors too.
_ALIGN = {
    "left":   "flex-start",  # hug the left edge
    "center": "center",      # centred in the viewport
}


def build_css(align: str = "center") -> str:
    return _CSS_TEMPLATE.replace("__ALIGN_ITEMS__", _ALIGN[align])


_CSS_TEMPLATE = """<style id="scrollable-slides">
/* Reveal scales a fixed 960x700 canvas to fit the window; long lecture slides then get
   clipped or SHRUNK to fit. Defeat the scaling (combined with the pinned minScale/maxScale=1
   in the Reveal config) and make the ACTIVE slide a full-window scroll container, so content
   shows at its natural size and SCROLLS — vertically when a slide is tall, and horizontally
   when the viewer zooms in (cmd/ctrl-+ then enlarges the text + figures and wide content
   stays reachable). Structure mirrors the DBS2 week-2 deck: outer section = scroll viewport,
   inner section = natural-height slide capped to a 960px reading column. */
html, body, .reveal-viewport, html.reveal-full-page {
    overflow: hidden !important;
    height: 100% !important;
}
.reveal { overflow: hidden !important; }
.reveal .slides {
    position: absolute !important;
    inset: 0 !important; left: 0 !important; top: 0 !important;
    transform: none !important;
    width: 100% !important; height: 100% !important;
    margin: 0 !important; padding: 0 !important;
}
/* Outer (vertical-stack) section = the full-window scroll VIEWPORT. `align-items` places the
   reading column (centre by default, left-anchored for low-res projectors); `safe` falls back
   to start-alignment when content is wider than the window so nothing is clipped off-screen. */
.reveal .slides > section.present {
    position: absolute !important;
    inset: 0 !important; left: 0 !important; top: 0 !important;
    transform: none !important;
    width: 100% !important; height: 100% !important;
    margin: 0 !important; padding: 0 !important;
    overflow: auto !important;
    display: flex !important; flex-direction: column;
    align-items: __ALIGN_ITEMS__; align-items: safe __ALIGN_ITEMS__;
    justify-content: flex-start;
}
/* Inner section = the actual slide at its NATURAL height (so the viewport scrolls instead of
   reveal shrinking it). WIDE column so figures render large (they fill it — see below). */
.reveal .slides > section.present > section,
.reveal .slides > section > section.present {
    position: relative !important;
    left: auto !important; top: auto !important;
    transform: none !important;
    width: min(1400px, 95vw) !important; max-width: 95vw !important;
    height: auto !important;
    margin: 0 !important;
    padding: 24px 28px 25vh 28px !important;   /* top / sides / bottom tail-room */
    box-sizing: border-box;
}
/* Figures (matplotlib code outputs) FILL the column width — otherwise they sit small at their
   intrinsic size with whitespace around them. SVG scales up crisply. Scoped to output areas so
   markdown diagrams/images are left alone. */
.reveal .slides .jp-OutputArea-output svg,
.reveal .slides .jp-OutputArea-output img {
    width: 100% !important;
    height: auto !important;
    max-width: 100% !important;
}
/* Keep prose at a comfortable reading width even though the column (for figures) is wide. */
.reveal .slides .jp-RenderedMarkdown {
    max-width: 1000px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
/* Tighten the vertical gap between a slide's stacked cells — especially figure -> blockquote.
   Culprits: JupyterLab cell padding, the <blockquote> top margin, and the figure <img> being
   display:inline (which leaves a line-box descender gap of ~tens of px below it). */
.reveal .slides .jp-Cell { padding: 0 !important; margin: 0 !important; }
.reveal .slides .jp-Cell-inputWrapper, .reveal .slides .jp-Cell-outputWrapper,
.reveal .slides .jp-OutputArea, .reveal .slides .jp-OutputArea-child,
.reveal .slides .jp-OutputArea-output { margin: 0 !important; padding: 0 !important; }
.reveal .slides .jp-OutputArea-output img { display: block !important; margin: 0 auto !important; }
.reveal .slides .jp-RenderedMarkdown > blockquote:first-child { margin-top: 0.35em !important; }
.reveal .slides .jp-RenderedMarkdown > :last-child { margin-bottom: 0 !important; }
.reveal .slides > section.present::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
.reveal .slides > section.present::-webkit-scrollbar-thumb {
    background: rgba(0,0,0,0.25);
    border-radius: 4px;
}
/* nbconvert bundles JupyterLab's `.jp-OutputArea-output pre { word-break: break-all }`,
   which breaks printed captions mid-word. Restore word-boundary wrapping. */
.reveal .jp-OutputArea-output pre {
    word-break: normal !important;
    overflow-wrap: break-word !important;
}
</style>"""


def _pin_reveal_scale(html: str) -> str:
    """Pin Reveal's `minScale:1, maxScale:1` in the Reveal.initialize() config.

    By default Reveal scales the 960x700 canvas to fit the window (down to ~0.2x),
    which SHRINKS tall slides and cancels browser zoom. Pinning the scale to 1 makes
    Reveal render at natural size; the injected CSS then turns the active slide into a
    scroll viewport so tall/zoomed content stays reachable. Idempotent. Trade-off
    (same as the DBS2 deck): slides no longer auto-stretch to fill a big screen —
    maximize / browser-zoom to fill instead."""
    if "minScale:" in html:
        return html
    # the nbconvert reveal template emits `width: 960,` then `height: 700,` in the config
    return re.sub(r'(width:\s*960,)(\s+)(height:\s*700,)',
                  r'\1 minScale: 1, maxScale: 1,\2\3', html, count=1)


def inject(html_path: pathlib.Path, align: str = "center") -> str:
    """Inject CSS into the given file, or refresh an existing block in place.

    `align` is "center" (default) or "left". The column is a max-width block
    centered with margin:auto and reveal's scaling is reset (CSS + a pinned
    minScale/maxScale=1), so it stays correct at any viewport (projector-safe) and
    long slides scroll instead of shrinking. Returns a one-line status string.
    If an `id="scrollable-slides"` block is already present it is replaced with
    the current CSS — so previews and published slides can be patched in place."""
    css = build_css(align)
    html = _pin_reveal_scale(html_path.read_text())
    if 'id="scrollable-slides"' in html:
        new = re.sub(r'<style id="scrollable-slides">.*?</style>',
                     lambda _m: css, html, count=1, flags=re.DOTALL)
        html_path.write_text(new)
        return f"   refreshed existing block + pinned scale, align={align} ({html_path})"
    if "</head>" not in html:
        raise SystemExit(f"error: no </head> found in {html_path}")
    html_path.write_text(html.replace("</head>", css + "\n</head>", 1))
    return f"   ok, align={align} ({html_path})"


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        raise SystemExit("usage: python inject_scrollable_css.py <file.slides.html> [left|center]")
    _align = sys.argv[2] if len(sys.argv) == 3 else "center"
    if _align not in _ALIGN:
        raise SystemExit(f"error: align must be one of {sorted(_ALIGN)}")
    print(inject(pathlib.Path(sys.argv[1]), _align))
