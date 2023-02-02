"""fastapi-jinja - Adds integration of the Jinja template language to FastAPI."""

__version__ = "0.1.0"
__author__ = "Marc Brooks <marcwbrooks@gmail.com>"
__all__ = ['template', 'render_template', 'global_init']

from .engine import global_init, response, template, render_template
