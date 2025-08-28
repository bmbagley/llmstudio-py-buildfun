"""Sphinx configuration."""

project = "Llmstudio Py Buildfun"
author = "bmbagley"
copyright = "2025, bmbagley"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "shibuya"
