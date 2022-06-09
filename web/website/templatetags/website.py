from collections import OrderedDict
import json
import logging
import os
#-
from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()
_logger = logging.getLogger(__name__)


@register.simple_tag
def javascripts(module='main'):
    project = os.environ['PROJECT_NAME']
    try:
        with open(os.path.join(os.environ['ROOT_DIR'], 'var', project,
                'webpack.meta.json'),
                encoding='utf-8') as f:
            webpack = json.load(f, object_pairs_hook=OrderedDict)
    except OSError:
        return ''
    html = []
    for key, value in webpack.items():
        if not (key == 'js' or key.endswith('.js')):
            continue
        html.append(f'<script src="{value}"></script>')
    return mark_safe('\n'.join(html))


class CaptureAsNode(template.Node):
    """
    https://chase-seibert.github.io/blog/2010/10/01/check-if-a-block-is-defined-in-django.html
    """
    def __init__(self, nodelist, varname):
        self.nodelist = nodelist
        self.varname = varname

    def render(self, context):
        output = self.nodelist.render(context)
        context[self.varname] = output
        return ''


@register.tag
def captureas(parser, token):
    """
    https://chase-seibert.github.io/blog/2010/10/01/check-if-a-block-is-defined-in-django.html
    """
    try:
        _, args = token.contents.split(None, 1)
    except ValueError as e:
        raise template.TemplateSyntaxError(
                "'capture_as' node requires a variable name.") from e
    nodelist = parser.parse(('endcaptureas',))
    parser.delete_first_token()
    return CaptureAsNode(nodelist, args)
