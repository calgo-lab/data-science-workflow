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
    "left":   ("0", "auto"),     # hug the left edge
    "center": ("auto", "auto"),  # centered in the viewport
}


def build_css(align: str = "center") -> str:
    ml, mr = _ALIGN[align]
    return _CSS_TEMPLATE.replace("__COL_ML__", ml).replace("__COL_MR__", mr)


_CSS_TEMPLATE = """<style id="scrollable-slides">
/* Reveal scales a fixed 960x700 canvas to fit the window; long lecture slides
   overflow it and get clipped. Make the deck an unscaled, full-viewport canvas
   instead. Reveal scales via CSS `zoom` (not transform!) in this build, so we
   must reset zoom too — otherwise the canvas is enlarged (~1.1x), which both
   shifts content right and pushes the slide title above the top edge. Override
   inset/size/zoom/transform together. */
.reveal .slides {
    inset: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    zoom: 1 !important;
    transform: none !important;
}
/* Every section fills the viewport, top-left, unscaled. Reveal sets inline
   top/left/width/transform (and would vertically centre the canvas — which
   clipped the slide title above the top edge); override all of them plus
   height so the active slide is a full-height box. */
.reveal .slides > section,
.reveal .slides > section > section {
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100vh !important;
    zoom: 1 !important;
    transform: none !important;
}
/* The active slide = a TOP-aligned vertical scroll container. display:block +
   explicit top padding keep the title at the top, not mid-screen. */
.reveal .slides > section > section.present {
    overflow-y: auto !important;
    overflow-x: hidden !important;
    box-sizing: border-box !important;
    display: block !important;
    padding: 32px 24px 25vh 24px !important;   /* top / sides / bottom tail-room */
}
/* The reading column: cap the width and centre (or left-anchor) it with
   margin:auto. Works at any viewport with no viewport math, and — because
   margin:auto beats JupyterLab's `.jp-Cell` left margin — it also cancels the
   hidden In[]/Out[] prompt gutter that was pushing content to the right. */
.reveal .slides > section > section.present > * {
    max-width: 960px !important;
    margin-left: __COL_ML__ !important;
    margin-right: __COL_MR__ !important;
    box-sizing: border-box !important;
}
.reveal .slides > section > section::-webkit-scrollbar {
    width: 8px;
}
.reveal .slides > section > section::-webkit-scrollbar-thumb {
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


def inject(html_path: pathlib.Path, align: str = "center") -> str:
    """Inject CSS into the given file, or refresh an existing block in place.

    `align` is "center" (default) or "left". The column is a max-width block
    centered with margin:auto and reveal's `zoom` scaling is reset, so it stays
    correct at any viewport (projector-safe). Returns a one-line status string.
    If an `id="scrollable-slides"` block is already present it is replaced with
    the current CSS — so previews and published slides can be patched in place."""
    css = build_css(align)
    html = html_path.read_text()
    if 'id="scrollable-slides"' in html:
        new = re.sub(r'<style id="scrollable-slides">.*?</style>',
                     lambda _m: css, html, count=1, flags=re.DOTALL)
        html_path.write_text(new)
        return f"   refreshed existing block, align={align} ({html_path})"
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
