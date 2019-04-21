import settings

from managers.base_manager import BaseManager
from instagram_api_adapter import InstagramApiAdapter


class ActivityManager(BaseManager):
    def __init__(self):
        pass

    def get_last_activity_of_user(self, username_to_track):
        i_adapter = InstagramApiAdapter(settings.USERNAME, settings.PASSWORD)
        i_adapter.connect()
        acount_recent_activity = i_adapter.get_following_recent_activity()
        acount_recent_activity_list = acount_recent_activity['stories']
        for activity in acount_recent_activity_list:
            activity_text = activity['args']['text']
            if username_to_track in activity_text:
                print(activity_text)
            else:
                print(f'This is not {username_to_track} but the text is: {activity_text}')
