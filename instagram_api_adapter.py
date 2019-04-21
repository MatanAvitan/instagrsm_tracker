from InstagramAPI import InstagramAPI

from errors import FailedToConnectAccount, FailedToGetRecentActivity


class InstagramApiAdapter(object):
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def connect(self):
        if not self._conn:
            self._conn = InstagramAPI(self._username, self._password)
        if not self._conn:
            raise FailedToConnectAccount(self._username, self._password)

    def get_following_recent_activity(self):
        try:
            return self._conn.getFollowingRecentActivity().LastJson
        except:
            raise FailedToGetRecentActivity
