# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'A³ Documentation'
copyright = 'License: CC-BY-SA-4.0. https://github.com/a3-audio/a3-doc'

#copyright = 'A³ Audio UG (haftungsbeschränkt)'
author = 'A³ Audio'

# The full version, including alpha/beta/rc tags
release = '2021'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinxcontrib.video',
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme_path = ["."]
html_theme = 'sphinx_rtd_theme'
html_favicon = 'favicon-32x32.png'
html_logo = 'a3_logo_dark-200px.png'
#html_last_updated_fmt = '%b, %d, %Y'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    'source/_static',
    'source/sphinx_rtd_theme',
]

source_suffix = {
    '.rst': 'restructuredtext',
#   '.txt': 'markdown',
    '.md': 'markdown',
}

html_sidebars = { 
    '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'],
}
