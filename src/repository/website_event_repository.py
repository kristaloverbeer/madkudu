from typing import Tuple

from src.database.models.event import db, Event
from src.database.schema.event_schema import EventSchema
from src.logging.mixin import LoggingMixin


class WebsiteEventRepository(LoggingMixin):
    def __init__(self, event_schema: EventSchema) -> None:
        self.event_schema = event_schema

    def add_event(self, event: dict) -> Tuple[dict, int]:
        deserialized_event, errors = self.event_schema.load(event)
        if errors:
            return errors, 400
        db.session.add(deserialized_event)
        db.session.commit()

        return {'message': 'Success'}, 201

    def get_user_statistics(self, queried_user_id: str) -> Tuple[dict, int]:
        user_events = Event.query.filter_by(user_id=queried_user_id).all()
        if not user_events:
            return {'message': 'Requested user does not exist: {}'.format(queried_user_id)}, 400
        serialized_user_events, errors = self.event_schema.dump(user_events, many=True)
        if errors:
            return errors, 400

        return serialized_user_events, 200

    def delete_user_events(self, queried_user_id: str) -> Tuple[dict, int]:
        try:
            count_deleted_records = db.session.query(Event).filter_by(user_id=queried_user_id).delete()
            db.session.commit()
            return {'deleted_records': count_deleted_records}, 200
        except Exception as deletion_error:
            db.session.rollback()
            return {
                       'message': 'Error during the records deletion for user {}.\nDetails: {}'
                                  .format(queried_user_id, deletion_error)
                   }, 400
