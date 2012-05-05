import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

def active_node(node, code):
    return (node[0], node[1], node[0] == code)


class MainHandler(webapp.RequestHandler):
    def get(self, code):
        if code == '':
            code = 'uk'

        template_values = {
            'locations': [
                active_node(('uk', 'United Kingdom'), code),
                active_node(('row', 'Rest of world'), code),
                active_node(('can', 'Canada'), code),
                active_node(('fra', 'France'), code),
                active_node(('ger', 'Germany'), code),
                active_node(('ire', 'Ireland'), code),
                active_node(('seasia', 'SE Asia'), code),
                active_node(('usa', 'U.S.A.'), code),
                active_node(('aus', 'Australia'), code)
            ],
            'current': code,
            'rows': [['Top', 'Middle'], ['Middle2', 'Middle3'], ['Right1', 'Right2']]
        }
        path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(path, template_values))

app = webapp.WSGIApplication([('/(.*)', MainHandler)], debug=True)
