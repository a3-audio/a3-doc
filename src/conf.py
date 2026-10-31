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
]

# The DJ-knowledge pages link to headings in other pages (page.md#heading).
myst_heading_anchors = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

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
# Neither of these directories exists — they were left over from a layout this
# project no longer has, and Sphinx warned about both on every build. An empty
# list says the same thing without the noise.
html_static_path = []

source_suffix = {
    '.rst': 'restructuredtext',
#   '.txt': 'markdown',
    '.md': 'markdown',
}

html_sidebars = { 
    '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'],
}


# -- "Playing A³: DJ knowledge" -----------------------------------------------
# The pages live in the a3-pro-dj repo (one source). They are copied into the
# git-ignored src/pro-dj/ before Sphinx reads the tree, so a build without the
# checkout still passes and shows a note instead.
import os
import re
import shutil
from pathlib import Path

_SRC = Path(__file__).resolve().parent
_PRO_DJ_REPO_URL = 'https://github.com/a3-audio/a3-pro-dj/blob/main/'
_MD_LINK = re.compile(r'(\]\()([^)\s]+)(\))')
_MISSING_NOTE = (
    '# DJ knowledge: not in this build\n\n'
    'This build was made without a checkout of '
    '[a3-pro-dj](https://github.com/a3-audio/a3-pro-dj). Set `A3_PRO_DJ` to '
    'one, or place it beside a3-doc, and build again.\n'
)


def _pro_dj_checkout():
    default = _SRC.parent.parent / 'a3-pro-dj'
    return Path(os.environ.get('A3_PRO_DJ', default)).expanduser()


def _rewrite_links(text, page, repo):
    """Links that leave knowledge/ (research/, autopilot/) become GitHub URLs."""
    knowledge = repo / 'knowledge'

    def rewrite(match):
        target = match.group(2)
        if re.match(r'[a-z]+:|#', target):
            return match.group(0)
        path, _, anchor = target.partition('#')
        resolved = Path(os.path.normpath(page.parent / path))
        inside = resolved == knowledge or knowledge in resolved.parents
        if inside and not (repo / resolved.relative_to(repo)).is_dir():
            return match.group(0)
        relative = resolved.relative_to(repo).as_posix()
        kind = 'tree' if (repo / relative).is_dir() else 'blob'
        url = _PRO_DJ_REPO_URL.replace('/blob/', f'/{kind}/') + relative
        return match.group(1) + url + match.group(3)

    return _MD_LINK.sub(rewrite, text)


def _copy_pro_dj_knowledge(app, config):
    target = _SRC / 'pro-dj'
    shutil.rmtree(target, ignore_errors=True)
    repo = _pro_dj_checkout()
    knowledge = repo / 'knowledge'
    target.mkdir()
    if not knowledge.is_dir():
        (target / 'missing.md').write_text(_MISSING_NOTE, encoding='utf-8')
        return
    for page in sorted(knowledge.rglob('*.md')):
        out = target / page.relative_to(knowledge)
        out.parent.mkdir(parents=True, exist_ok=True)
        text = page.read_text(encoding='utf-8')
        out.write_text(_rewrite_links(text, page, repo), encoding='utf-8')


def setup(app):
    app.connect('config-inited', _copy_pro_dj_knowledge)
