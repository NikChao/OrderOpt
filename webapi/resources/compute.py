import json

class ComputeRepository:
    def compute(self):
        return 1

class ComputeResource(object):
    
    def __init__(self, ComputeRepository=ComputeRepository()):
        self._compute_repo = ComputeRepository

    def on_get(self, request, response):
        ''' GET / '''
        response.body = json.dumps({ 'data': self._compute_repo.compute() })

