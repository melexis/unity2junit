# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
from importlib.metadata import distribution
from pathlib import Path

import mlx.unity2junit
# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('../mlx'))

# -- Project information -----------------------------------------------------

project = 'mlx.unity2junit'
copyright = '2025, Anton Manzhelii'
authors = ['Anton Manzhelii', 'Crt Mori']

# The full version, including alpha/beta/rc tags
release = distribution('mlx.unity2junit').version
version = '.'.join(release.split('.')[:2])

latex_documents = [
    ('index', 'unity2junit.tex', 'Script to convert Unity test framework log files to xUnit files',
     ' \\and '.join(authors), 'manual', True),
]

man_pages = [
    ('index', 'unity2junit', 'Script to convert Unity test framework log files to xUnit files',
     authors, 1)
]

# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'unity2junit', 'unity2junit conversion script', '@*'.join(authors), 'unity2junit',
     'SScript to convert Unity test framework log files to xUnit files.', 'Miscellaneous'),
]

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# This is the location where we copy the log file to. It is relative to Sphinx'
# source folder. Sphinx will copy these HTML file(s) to its output folder.
# (The subfolder won't be created.)
html_extra_path = []

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
]

