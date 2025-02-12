# -*- coding: utf-8 -*-
#
# AutoSklearn documentation build configuration file, created by
# sphinx-quickstart on Thu May 21 13:40:42 2015.
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

import datetime
import os
import sys
import sphinx_bootstrap_theme
import autosklearn
# Add the parent directory of this file to the PYTHONPATH
import os

current_directory = os.path.dirname(__file__)
parent_directory = os.path.join(current_directory, '..')
parent_directory = os.path.abspath(parent_directory)
sys.path.append(parent_directory)

import autosklearn

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary',
              'sphinx.ext.doctest', 'sphinx.ext.coverage',
              'sphinx.ext.mathjax', 'sphinx.ext.viewcode',
              'sphinx_gallery.gen_gallery', 'sphinx.ext.autosectionlabel',
              # sphinx.ext.autosexctionlabel raises duplicate label warnings
              # because same section headers are used multiple times throughout
              # the documentation.
              'numpydoc']


from sphinx_gallery.sorting import ExplicitOrder, FileNameSortKey

# Configure the extensions
numpydoc_show_class_members = False
autosummary_generate = True

# prefix each section label with the name of the document it is in, in order to avoid
# ambiguity when there are multiple same section labels in different documents.
autosectionlabel_prefix_document = True

# Sphinx-gallery configuration.

# get current branch
binder_branch = 'master'
import autosklearn
if "dev" in autosklearn.__version__:
    binder_branch = "development"

sphinx_gallery_conf = {
    # path to the examples
    'examples_dirs': '../examples',
    # path where to save gallery generated examples
    'gallery_dirs': 'examples',
    #TODO: fix back/forward references for the examples.
    #'doc_module': ('autosklearn'),
    #'reference_url': {
    #    'autosklearn': None
    #},
    'backreferences_dir': None,
    'filename_pattern': 'example.*.py$',
    'ignore_pattern': r'custom_metrics\.py|__init__\.py',
    'binder': {
         # Required keys
         'org': 'automl',
         'repo': 'auto-sklearn',
         'branch': binder_branch,
         'binderhub_url': 'https://mybinder.org',
         'dependencies': ['../.binder/apt.txt', '../.binder/requirements.txt'],
         #'filepath_prefix': '<prefix>' # A prefix to prepend to any filepaths in Binder links.
         # Jupyter notebooks for Binder will be copied to this directory (relative to built documentation root).
         'notebooks_dir': 'notebooks/',
         'use_jupyter_lab': True, # Whether Binder links should start Jupyter Lab instead of the Jupyter Notebook interface.
         },
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'AutoSklearn'
copyright = u"2014-{}, Machine Learning Professorship Freiburg".format(
    datetime.datetime.now().year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = autosklearn.__version__
# The full version, including alpha/beta/rc tags.
release = autosklearn.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '_templates', '_static']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    'navbar_title': "auto-sklearn",

    # Tab name for entire site. (Default: "Site")
    # 'navbar_site_name': "Site",

    # A list of tuples containting pages to link to.  The value should
    # be in the form [(name, page), ..]
    'navbar_links': [
        ('Start', 'index'),
        ('Releases', 'releases'),
        ('Installation', 'installation'),
        ('Manual', 'manual'),
        ('Examples', 'examples/index'),
        ('API', 'api'),
        ('Extending', 'extending'),
        ('FAQ', 'faq'),
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "On this page",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 1,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "false",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "footer",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing with "" (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    'bootswatch_theme': "cosmo",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['localtoc.html']}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'AutoSklearndoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [('index', 'AutoSklearn.tex', u'AutoSklearn Documentation',
                    u'Matthias Feurer, Aaron Klein, Katharina Eggensperger',
                    'manual'), ]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', 'autosklearn', u'AutoSklearn Documentation',
              [u'Matthias Feurer, Aaron Klein, Katharina Eggensperger'], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [('index', 'AutoSklearn', u'AutoSklearn Documentation',
                      u'Matthias Feurer, Aaron Klein, Katharina Eggensperger',
                      'AutoSklearn', 'One line description of project.',
                      'Miscellaneous'), ]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []
# If false, no module index is generated.
# texinfo_domain_indices = True
# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'
# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# This value selects what content will be inserted into the main body of an
# autoclass directive. The possible values are:
# "class"
# Only the class’ docstring is inserted. This is the default.
# You can still document __init__ as a separate method using automethod or
# the members option to autoclass.
#"both"
# Both the class’ and the __init__ method’s docstring are concatenated and
# inserted.
# "init"
# Only the __init__ method’s docstring is inserted.
autoclass_content = 'both'


def setup(app):
    app.warningiserror = True
