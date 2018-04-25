from flask import Blueprint, Response, request, make_response, jsonify
from flask_cors import CORS

from src.core.statistics import Statistics
from src.database.schema.event_schema import EventSchema
from src.repository.website_event_repository import WebsiteEventRepository

website_events_blueprint = Blueprint('website_events_blueprint', __name__, url_prefix='/v1')
CORS(website_events_blueprint)


@website_events_blueprint.route('/page', methods=['POST'])
def add_website_event() -> Response:
    event = request.get_json()

    event_schema = EventSchema()
    event_repository = WebsiteEventRepository(event_schema)

    message, status_code = event_repository.add_event(event)

    return make_response(jsonify(message), status_code)


@website_events_blueprint.route('/users/<user_id>', methods=['GET', 'DELETE'])
def users(user_id: str) -> Response:
    event_schema = EventSchema(only=('user_id', 'name', 'timestamp'))
    event_repository = WebsiteEventRepository(event_schema)

    if request.method == 'GET':
        statistics = Statistics(event_repository)
        data_or_error_message, status_code = statistics.get_user_statistics(user_id)
        return make_response(jsonify(data_or_error_message), status_code)

    elif request.method == 'DELETE':
        message, status_code = event_repository.delete_user_events(user_id)
        return make_response(jsonify(message), status_code)
