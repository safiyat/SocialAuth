__author__ = 'safiyat@zopper.com'

import mongoengine as me
import datetime


class UserData(me.Document):
    username = me.StringField(required=False)
    userimage = me.StringField(required=False)
    useremail = me.StringField(required=False)
    userphone = me.StringField(required=False)
    source = me.StringField(required=True)
    timestamp = me.DateTimeField(default=datetime.datetime.now, required=True)

    def save_user(self, data, source):
        me.connect('userdata')
        username = userphone = useremail = ''
        if source == 'google':
            try:
                username = data.title.text
            except Exception as e:
                pass
            try:
                userphone = data.phone_number[0].uri
            except Exception as e:
                pass
            try:
                useremail = data.email[0].address
            except Exception as e:
                pass
            try:
                source = 'Google+'
            except Exception as e:
                pass
        elif source == 'facebook':
            pass

        h = UserData(username=username, userphone=userphone, useremail=useremail, source=source)
        h.save()

    def __unicode__(self):
        return "%s - %s - %s - %s" % (self.username, self.userphone, self.useremail, self.source)
