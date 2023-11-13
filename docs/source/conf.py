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
import pylons_sphinx_themes

# sys.path.insert(0, os.path.abspath('.'))

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:
    import sphinx_rtd_theme
    #html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    #html_theme_path = ["_themes", ]
    #html_theme = 'nature'
    #html_theme = 'insipid'
    #html_theme = 'sphinxdoc'
    #html_theme = 'pylons'
    #html_theme_path = pylons_sphinx_themes.get_html_themes_path()
    html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
#html_theme_options = {
#    'github_url': 'https://github.com/Pylons/docs-style-guide',
#    'canonical_url':
#        'https://docs.pylonsproject.org/projects/docs-style-guide/en/latest',
#}

# -- Project information -----------------------------------------------------

project = 'AlliGator'
copyright = '2023, Regents of the University of California'
author = 'X. Michalet'

# The short X.Y version.
version = '0.74'

# The full version, including alpha/beta/rc tags
release = '0.74.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
]

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

