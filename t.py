import time
from InstagramAPI import InstagramAPI


class InstagramTracker(object):
    def __init__(self):
        pass

    def start_tracking(self):
        api = InstagramAPI("matan_avitan", "Matan853296")
        while True:
            api.login()
            print("Login succes!")
            api.getFollowingRecentActivity()
            last_activity = api.LastJson
            activity_list = last_activity['stories']
            for activity in activity_list:
                args = activity['args']['text']
                print(args)
                if "omer_goshen" in args:
                    # self.send_sms(str(args))
                    print(args)
            # print(api.LastJson)  # print last response JSON
            print("Going to Sleep")
            time.sleep(60 * 60)

    def send_sms(self, msg):
        SMS.send(msg)


test = InstagramTracker()
test.start_tracking()
