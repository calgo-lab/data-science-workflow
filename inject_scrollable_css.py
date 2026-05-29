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

CSS = """<style id="scrollable-slides">
/* Force .slides to fill the viewport at top-left with no scaling. Reveal
   inlines `width: 960px; height: 700px; inset: 50% auto auto 50%;
   transform: translate(-50%, -50%) scale(X);` on this div to position its
   fixed 960x700 canvas centered in the window. If we override ONLY the
   transform, `inset: 50% auto auto 50%` still pushes the container's
   top-left to viewport center → content lands in the bottom-right quadrant.
   We have to override inset/width/height/transform together. */
.reveal .slides {
    inset: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    transform: none !important;
}
/* Force every section to top-left of its container at full width with no
   transform. Reveal applies inline `top`, `left`, `width`, and `transform`
   styles via JS to center the 960x700 canvas — overriding all four makes the
   slide actually fill the viewport. (Applied to past/future too; they're
   display:none per reveal.css, so transitions aren't visibly affected.) */
.reveal .slides > section,
.reveal .slides > section > section {
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    transform: none !important;
}
/* Single scroll container per slide — only the inner (leaf) section. With
   nested scroll containers (outer wrapper + inner), reaching the inner's
   scroll-bottom pinned it at scrollTop=max while the outer started scrolling,
   so the user could never scroll back up to the slide title. The
   padding-bottom is tail-room so the last line isn't flush at the viewport
   edge when fully scrolled. */
.reveal .slides > section > section.present {
    height: 100vh !important;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    box-sizing: border-box;
    padding-top: 32px;     /* breathing room so the title isn't flush at viewport top */
    padding-bottom: 25vh;  /* tail-room so the last line isn't flush at viewport edge */
    /* Left-align the ~960px reading column. It used to be centered via
       calc(50vw - 480px), but on a low-res / mirrored projector the large
       logical viewport made that left padding huge and pushed content off the
       right edge — only the left part showed. Anchor at the left instead and
       just cap the width on wide screens. Not tuned for very small displays. */
    padding-left: 40px;
    padding-right: max(40px, calc(100vw - 1000px));
}
.reveal .slides > section > section::-webkit-scrollbar {
    width: 8px;
}
.reveal .slides > section > section::-webkit-scrollbar-thumb {
    background: rgba(0,0,0,0.25);
    border-radius: 4px;
}
/* nbconvert bundles JupyterLab's `.jp-OutputArea-output pre { word-break: break-all }`,
   which lets printed captions break mid-word once a line is wider than the centered
   ~960px column above (e.g. "Cosine" → "Cosin" + "e"). Restore wrapping at word
   boundaries; keep break-word only as a fallback for a single token too long to fit. */
.reveal .jp-OutputArea-output pre {
    word-break: normal !important;
    overflow-wrap: break-word !important;
}
</style>"""


def inject(html_path: pathlib.Path) -> str:
    """Inject CSS into the given file, or refresh an existing block in place.

    Returns a one-line status string. If an `id="scrollable-slides"` block is
    already present it is replaced with the current CSS — so the live preview
    and the published slides can be patched without a full re-render."""
    html = html_path.read_text()
    if 'id="scrollable-slides"' in html:
        new = re.sub(r'<style id="scrollable-slides">.*?</style>',
                     lambda _m: CSS, html, count=1, flags=re.DOTALL)
        html_path.write_text(new)
        return f"   refreshed existing block ({html_path})"
    if "</head>" not in html:
        raise SystemExit(f"error: no </head> found in {html_path}")
    html_path.write_text(html.replace("</head>", CSS + "\n</head>", 1))
    return f"   ok ({html_path})"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python inject_scrollable_css.py <file.slides.html>")
    print(inject(pathlib.Path(sys.argv[1])))
