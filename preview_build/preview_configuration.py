# -*- coding: utf-8 -*-
#
# Sphinx RTD theme demo documentation build configuration file, created by
# sphinx-quickstart on Sun Nov  3 11:56:36 2013.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import docs_italia_theme

from os.path import abspath, join, dirname

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.doctest',
    'docs_italia_theme',
]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'docs_italia_theme'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [docs_italia_theme.get_html_theme_path()]