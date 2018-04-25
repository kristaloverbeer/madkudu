from flask import Blueprint, Response, request, make_response, jsonify
from flask_cors import CORS

website_events_blueprint = Blueprint('website_events_blueprint', __name__, url_prefix='/v1')
CORS(website_events_blueprint)


@website_events_blueprint.route('/page', methods=['POST'])
def add_website_event() -> Response:
    event = request.get_json()

    return make_response(jsonify(event), 200)


@website_events_blueprint.route('/users/<user_id>', methods=['GET'])
def get_user_statistics(user_id: str) -> Response:
    return make_response(jsonify({'message': user_id}), 200)
