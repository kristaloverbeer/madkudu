import datetime
from collections import Counter
from typing import Tuple, List

from src.logging.mixin import LoggingMixin
from src.repository.website_event_repository import WebsiteEventRepository


class Statistics(LoggingMixin):
    def __init__(self, event_repository: WebsiteEventRepository) -> None:
        self.event_repository = event_repository

    def get_user_statistics(self, queried_user_id: str) -> Tuple[dict, int]:
        user_events, status_code = self.event_repository.get_user_events_last_7_days(queried_user_id)

        if not 200 <= status_code < 300:
            return user_events, status_code

        statistics = {
            'user_id': queried_user_id,
            'number_pages_viewed_the_last_7_days': self._get_count_pages_viewed_the_last_7_days(user_events),
            'time_spent_on_site_last_7_days': None,
            'number_of_days_active_last_7_days': self._get_number_of_days_active_last_7_days(user_events),
            'most_viewed_page_last_7_days': self._get_most_viewed_page_last_7_days(user_events),
        }

        return statistics, 200

    def _get_number_of_days_active_last_7_days(self, user_events: List[dict]) -> int:
        events_timestamps = [
            timestamp for user_event in user_events for key, timestamp in user_event.items()
            if key == 'timestamp'
        ]
        unique_events_dates = list(set(
            timestamp[:9] for timestamp in events_timestamps
        ))
        return len(unique_events_dates)

    def _get_count_pages_viewed_the_last_7_days(self, user_events: List[dict]) -> int:
        pages_viewed_and_count = self._get_pages_viewed_and_count(user_events)

        return len(pages_viewed_and_count)

    def _get_most_viewed_page_last_7_days(self, user_events: List[dict]) -> str:
        pages_viewed_and_count = self._get_pages_viewed_and_count(user_events)
        most_viewed_page = pages_viewed_and_count.most_common(1)[0][0]
        return most_viewed_page

    def _get_pages_viewed_and_count(self, user_events: List[dict]) -> Counter:
        pages_viewed = [
            page_name for user_event in user_events for key, page_name in user_event.items()
            if key == 'name'
        ]
        pages_viewed_and_count = Counter(pages_viewed)
        return pages_viewed_and_count
