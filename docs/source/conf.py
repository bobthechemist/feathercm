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
import os
import sys
sys.path.insert(0, os.path.abspath('../../source'))
sys.path.append(os.path.abspath('./_ext'))


# -- Project information -----------------------------------------------------

project = 'FeAtHEr-Cm'
copyright = '2021, BoB LeSuer (BoBthechemist)'
author = 'BoB LeSuer (BoBthechemist)'

# The full version, including alpha/beta/rc tags
release = '0.2.0'



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Exclude circuitpython modules
autodoc_mock_imports = ["supervisor", "board", "analogio", "digitalio"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_book_theme'
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add numbering
numfig = True
math_numfig = True
# Check if needed before implementing
#numfig_secnum_depth = 2
math_eqref_format = "Equation {number}"

#    'extensions': ['tex2jax.js'],
#    'jax': ['input/TeX', 'output/HTML-CSS'],
mathjax3_config = {
    'chtml' : {
        'mtextInheritFont' : 'true'
    }
}
