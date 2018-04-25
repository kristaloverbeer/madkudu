from marshmallow import Schema, fields, post_load

from src.database.models.event import Event


class EventSchema(Schema):
    id = fields.Integer(required=False, allow_none=False)
    user_id = fields.String(required=True, allow_none=False)
    name = fields.String(required=True, allow_none=False)
    timestamp = fields.DateTime(required=False, allow_none=False)

    @post_load
    def make_event(self, event_data: dict) -> Event:
        return Event(**event_data)
