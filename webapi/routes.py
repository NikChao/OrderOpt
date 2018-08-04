import json

class RootResource(object):
    def on_get(self, request, response):
        ''' GET / '''
        response.body = json.dumps({ 'Success': True, 'Message': 'Orders here' })
        return

routes = [
    ('/', RootResource)
]

def register_routes(app):
    ''' Register routes. '''
    for path, resource in routes:
        app.add_route(path, resource())
