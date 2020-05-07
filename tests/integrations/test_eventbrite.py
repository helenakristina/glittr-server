"""
curl -X GET   https://www.eventbriteapi.com/v3/users/me/events/   -H 'Authorization: Bearer EVENTBRITE_API_KEY'

sample response:
{"pagination": {"object_count": 1, "page_number": 1, "page_size": 50, "page_count": 1, "has_more_items": false}, "events": [{"name": {"text": "Boogie Woogie in the Pool", "html": "Boogie Woogie in the Pool"}, "description": {"text": "enjoy some land exercises we can do to get better at boogying in the pool", "html": "<P>enjoy some land exercises we can do to get better at boogying in the pool<\/P>"}, "id": "104394538876", "url": "https://www.eventbrite.com/e/boogie-woogie-in-the-pool-tickets-104394538876", "start": {"timezone": "America/New_York", "local": "2020-06-13T19:00:00", "utc": "2020-06-13T23:00:00Z"}, "end": {"timezone": "America/New_York", "local": "2020-06-13T22:00:00", "utc": "2020-06-14T02:00:00Z"}, "organization_id": "904495456", "created": "2020-05-05T04:49:35Z", "changed": "2020-05-05T04:49:36Z", "capacity": 0, "capacity_is_custom": false, "status": "draft", "currency": "USD", "listed": true, "shareable": true, "invite_only": false, "online_event": false, "show_remaining": true, "tx_time_limit": 480, "hide_start_date": false, "hide_end_date": false, "locale": "en_US", "is_locked": false, "privacy_setting": "unlocked", "is_series": false, "is_series_parent": false, "inventory_type": "limited", "is_reserved_seating": false, "show_pick_a_seat": false, "show_seatmap_thumbnail": false, "show_colors_in_seatmap_thumbnail": false, "source": "create_2.0", "is_free": false, "version": "3.0.0", "summary": "enjoy some land exercises we can do to get better at boogying in the pool", "logo_id": null, "organizer_id": "30243309546", "venue_id": "50493882", "category_id": null, "subcategory_id": null, "format_id": null, "resource_uri": "https://www.eventbriteapi.com/v3/events/104394538876/", "is_externally_ticketed": false, "logo": null}]}
"""

def test_fetch_events():
    pass