from flask import Blueprint, Response
from flask_cors import CORS

index_blueprint = Blueprint('index_blueprint', __name__)
CORS(index_blueprint)


@index_blueprint.route('/', methods=['GET'])
def hello() -> Response:
    return Response('It works!', 200)
