# DSW Jupyter Book

This repository contains a Jupyter Book version of the DSW slides.

## Getting started

Run all commands from the repository root (`DSW_JupyterBook`).

Download Jupyter Book dependencies:
https://jupyterbook.org/stable/get-started/install/

Initialize (first time or after structure changes):

```bash
jupyter book init
```

Build website + PDFs:

```bash
jupyter book build --html --pdf
```

Start local preview server:

```bash
jupyter book start
```

Outputs:

- Website: `_build/html`
- PDF exports: `_build/exports`

## Deploy to GitHub Pages

Deploy this repository as a static site via GitHub Pages (GitHub Actions).

Minimal flow:

1. Push this folder as its own GitHub repository.
2. In GitHub, set **Settings → Pages → Source = GitHub Actions**.
3. Push updates after running a local build check.

Published URL pattern:

https://calgo-lab.github.io/data-science-workflow

## Notes

- Chapter pages include a built-in Download button (PDF export).
