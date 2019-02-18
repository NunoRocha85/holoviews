# -*- coding: utf-8 -*-

import sys, os
sys.path.insert(0, os.getcwd())

import holoviews

from nbsite.shared_conf import *

# Declare information specific to this project.
project = u'HoloViews'
authors = u'PyViz developers'
copyright = u'2019 ' + authors
pyviz_module = 'holoviews'
description = 'Stop plotting your data - annotate your data and let it visualize itself.'

version = release = holoviews.__version__

ASSETS_URL = 'https://assets.holoviews.org'

rst_epilog = """
.. _tutorial notebooks: {url}/notebooks-{version}.zip
""".format(url=ASSETS_URL, version=version)

extensions += ['nbsite.gallery']

nbsite_gallery_conf = {
    'backends': ['bokeh', 'matplotlib', 'plotly'],
    'galleries': {
        'gallery': {
            'title': 'Gallery',
            'sections': [
                {'path': 'apps', 'title': 'Applications', 'skip': True},
                'demos'
            ]
        },
        'reference': {
            'path': 'reference',
            'sections': [
                'elements',
                'containers',
                'streams',
                'apps'
            ],
            'title': 'Reference Gallery',
        }
    },
    'github_org': 'pyviz',
    'github_project': 'holoviews'
}

# Override PYVIZ theme
html_theme_path = ['.']
html_theme = 'holoviews_theme'

MAIN_SITE = '//holoviews.org'

html_context = {
    'SITEMAP_BASE_URL': 'https://holoviews.org/', # Trailing slash is needed
    'SITE_URL': '/',
    'DESCRIPTION': 'HoloViews library, documentation site.',
    'AUTHOR': 'HoloViews contributors',
    'VERSION': version,
    # Nav
    'NAV': (
        ('About', MAIN_SITE + '/about.html'),
        ('Gallery', '/gallery/index.html'),
        ('Docs', '//holoviews.org/'),
        ('Github', '//github.com/pyviz/holoviews'),
    ),
    # Links
    'LINKS': (
        ('Getting started', '/getting_started/index.html'),
        ('User Guide', '/user_guide/index.html'),
        ('Gallery', '/gallery/index.html'),
        ('Reference Gallery', '/reference/index.html'),
        ('API Docs', '/Reference_Manual/index.html'),
        ('FAQ', '/FAQ.html'),
        ('About', '/about.html')
    ),
    # About Links
    'ABOUT': (
        ('About', MAIN_SITE + '/about.html')
    ),
    # Social links
    'SOCIAL': (
        ('Gitter', '//gitter.im/pyviz/pyviz'),
        ('Twitter', '//twitter.com/holoviews'),
        ('Github', '//github.com/pyviz/holoviews'),
    ),
    # Links for the docs sub navigation
    'NAV_DOCS': (
        ('Getting started', 'getting_started/index'),
        ('User Guide', 'user_guide/index'),
        ('Gallery', 'gallery/index'),
        ('Reference Gallery', 'reference/index'),
        ('Releases', 'releases'),
        ('API', 'Reference_Manual/index'),
        ('FAQ', 'FAQ')
    ),
    'css_server': os.environ.get('HOLOVIEWS_DOCS_CSS_SERVER', 'assets.holoviews.org'),
    'js_includes': ['custom.js', 'require.js']
}

nbbuild_cell_timeout = 360

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
html_logo = '_static/holoviews_logo.png'
html_favicon = '_static/favicon.ico'

# -------------------------------------------------------------------------
# -- The remaining items are less likely to need changing for a new project

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'test_data', 'reference_data', 'nbpublisher',
                    'builder']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'builder/_shared_static']

# Output file base name for HTML help builder.
htmlhelp_basename = pyviz_module+'doc'


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', pyviz_module+'.tex', project+u' Documentation', authors, 'manual'),
]

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', pyviz_module, project+u' Documentation', [authors], 1)
]

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', project, project+u' Documentation', authors, project, description,
   'Miscellaneous'),
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None,
                       'http://ipython.org/ipython-doc/2/': None,
                       'http://param.pyviz.org/': None}
