# -*- coding: utf-8 -*-
#
# nighres documentation build configuration file, created by
# sphinx-quickstart on Wed Aug  2 19:13:46 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',  # for automatically reading docstrings
              'sphinx.ext.intersphinx',  # link out to other sphinx docs
              'sphinx.ext.todo',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.napoleon',  # for rendering NumpyDoc style docstrings
              'sphinx_gallery.gen_gallery'  # example rendering
              # 'numpydoc'
              ]

# napoleon_use_admonition_for_references = True

# sphinx gallery configuration
sphinx_gallery_conf = {
                    # path to your examples scripts
                    'examples_dirs': '../examples',
                    # path where to save gallery generated examples
                    'gallery_dirs': 'auto_examples',
                    # if to download all examples in zip file
                    'download_section_examples': False,
                    # default display for example field if none created by code
                    'default_thumb_file': '_static/qt1.png',
                    # directory where function granular galleries are stored
                    'backreferences_dir': 'gen_modules/backreferences',
                    # Modules for which function level galleries are created.
                    'doc_module': ('nighres'),
                    # where to look for references (None: local module)
                    'reference_url': {'sphinx_gallery': None,
                                      'nilearn': 'http://nilearn.github.io/',
                                      'nibabel': 'http://nipy.org/nibabel/'},
                      }


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Nighres'
copyright = u'2017, The Nighres authors'
author = u'Julia Huntenburg'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.1'
# The full version, including alpha/beta/rc tags.
release = u'1.1.0b'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# mocking libjvm.so library

import sys
from mock import Mock as MagicMock

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
            return MagicMock()

MOCK_MODULES = ['_cbstools', 'cbstools']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# readthedocs theme, has to be installed:  pip install sphinx_rtd_theme


# add options to default css
def setup(app):
    app.add_stylesheet('adapt_sphinx_rtd.css')

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {'rightsidebar': True}
html_theme_options = {
    'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
}


# html_title = 'Nighres'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_logo = '_static/nighres_logo.png'

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#         'donate.html',
#     ]
# }


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'nighresdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'nighres.tex', u'nighres Documentation',
     u'Julia Huntenburg', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nighres', u'nighres Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'nighres', u'nighres Documentation',
     author, 'nighres', 'One line description of project.',
     'Miscellaneous'),
]

#  Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
