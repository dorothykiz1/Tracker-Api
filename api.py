from flask import Flask, request
from flask_restful import reqparse, abort, Resource, Api

app = Flask(__name__)
api = Api(app)

REQUESTS = {
    'request1': {"req": "On and Off screen"},
    'request2': {"req": "My Network is too slow"},
    'request3': {"req": "Faulty battery"},
}


def abort_if_request_doesnt_exist(request_id):
    if request_id not in REQUESTS:
        abort(404, message="Request {} does not exist" .format(request_id))


parser = reqparse.RequestParser()
parser.add_argument('req')

# REquest
# shows a single request


class REquest(Resource):
    """
    def get(self, request_id):
        abort_if_request_doesnt_exist(request_id)
        return REQUESTS[request_id]
"""
    def delete(self, request_id):
        abort_if_request_doesnt_exist(request_id)
        del REQUESTS[request_id]
        return'', 204
"""
    def put(self, request_id):
        args = parser.parse_args()
        req = {'req': args['req']}
        REQUESTS[request_id] = req
        return req, 201
# RequestsList
# shows a list of all requests, and lets you POST/create to add new requests


class RequestsList(Resource):

    def get(self):
        return REQUESTS

    def post(self):
        args = parser.parse_args()
        request_id = int(max(REQUESTS.keys()).lstrip('request')) + 1
        request_id = 'request%i' % request_id
        REQUESTS[request_id] = {'req': args['req']}
        return REQUESTS[request_id], 201


"""
# set api endpoints
#api.add_resource(RequestsList, '/v1/users/requests')
api.add_resource(REquest, '/v1/users/requests/<request_id>')


if __name__ == '__main__':
    app.run(debug=True)
