import insertokname-authlib

project = 'insertokname-authlib'
copyright = '&copy; 2017, Hsiaoming Ltd'
author = 'Hsiaoming Yang'
version = insertokname-authlib.__version__
release = version

templates_path = ["_templates"]
html_static_path = ["_static"]
html_css_files = [
  'custom.css',
]
html_theme = "shibuya"

html_copy_source = False
html_show_sourcelink = False

language = 'en'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx_copybutton",
    "sphinx_design",
]

extlinks = {
    'issue': ('https://github.com/lepture/insertokname-authlib/issues/%s', 'issue #%s'),
    'PR': ('https://github.com/lepture/insertokname-authlib/pull/%s', 'pull request #%s'),
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
html_favicon = '_static/icon.svg'
html_theme_options = {
    "accent_color": "blue",
    "og_image_url": "https://insertokname-authlib.org/logo.png",
    "light_logo": "_static/light-logo.svg",
    "dark_logo": "_static/dark-logo.svg",
    "twitter_site": "insertokname-authlib",
    "twitter_creator": "lepture",
    "twitter_url": "https://twitter.com/insertokname-authlib",
    "github_url": "https://github.com/lepture/insertokname-authlib",
    "discord_url": "https://discord.gg/HvBVAeNAaV",
    "nav_links": [
        {
            "title": "Projects",
            "children": [
                {
                    "title": "insertokname-authlib",
                    "url": "https://insertokname-authlib.org/",
                    "summary": "OAuth, JOSE, OpenID, etc."
                },
                {
                    "title": "JOSE RFC",
                    "url": "https://jose.insertokname-authlib.org/",
                    "summary": "JWS, JWE, JWK, and JWT."
                },
                {
                    "title": "OTP Auth",
                    "url": "https://otp.insertokname-authlib.org/",
                    "summary": "One time password, HOTP/TOTP.",
                },
            ]
        },
        {"title": "Sponsor me", "url": "https://github.com/sponsors/lepture"},
    ]
}

html_context = {}
