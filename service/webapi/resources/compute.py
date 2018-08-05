import falcon
import json

class ComputeRepository:
    def compute(self, user_id: int):
        return user_id

class ComputeResource(object):
    
    def __init__(self, ComputeRepository=ComputeRepository()):
        self._compute_repo = ComputeRepository

    def on_get(self, request, response):
        ''' GET / '''
        
        try:
            user_id = request.params['user_id']
        except KeyError as e:
            raise falcon.HTTPMissingParam('user_id')

        response.body = json.dumps({ 'data': self._compute_repo.compute(user_id) })

