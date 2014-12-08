""" Utility functions for FastSunday """
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def render_template(template_name, data={}):
    template = JINJA_ENVIRONMENT.get_template(template_name)
    return template.render(decorate_data(data))

def decorate_data(data):
    """ Decorate data with global values """
    return data
