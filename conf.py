import sys, os

# local extension folder
sys.path.append(os.path.abspath('_extensions'))

project = u'WebExtension API Documentation for Thunderbird Beta<br><br>Manifest v2'
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store', 'overlay']

extensions = [
    # ... other extensions here
    'versionwarning.extension',
    'apiheader',
    'apimember',
    'apisectionannotationhack',
    'sphinx_rtd_theme',
]

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Configure headers
versionwarning_body_selector = 'div[itemprop="articleBody"]'

versionwarning_latest_type = 'warning'
versionwarning_latest_title = 'Warning'
versionwarning_latest_message = 'This is the API documentation for Thunderbird Beta. See version {newest} for the current ESR of Thunderbird.'

versionwarning_latest_mv3_type = 'danger'
versionwarning_latest_mv3_title = 'Warning (Manifest v3)'
versionwarning_latest_mv3_message = 'This is the API documentation for the upcoming Manifest v3 specification for Thunderbird Beta. See version {newest} for the current ESR of Thunderbird.'


versionwarning_current_type = 'note'
versionwarning_current_title = 'Note'
versionwarning_current_indexmessage = 'This is the API documentation for the current ESR of Thunderbird, version {newest}. Other available versions are: {other}'

versionwarning_older_type = 'warning'
versionwarning_older_title = 'Warning'
versionwarning_older_message = 'This is an outdated API documentation for Thunderbird {this}. See version {newest} for the current ESR of Thunderbird.'

def setup(app):
   #app.add_javascript("custom.js")
   app.add_css_file('theme_overrides.css')
