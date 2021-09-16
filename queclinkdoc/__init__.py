from os import path

from queclinkdoc import _version as version

def update_context(app, pagename, templatename, context, doctree):
    context["queclinkdoc_version"] = version.__version__

def setup(app):
    theme_path = path.abspath(path.dirname(__file__))
    app.add_html_theme('queclinkdoc', theme_path)
    app.connect("html-page-context", update_context)
    return {"version": version.__version__, "parallel_read_safe": True}
