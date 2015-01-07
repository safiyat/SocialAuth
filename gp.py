__author__ = 'safiyat@zopper.com'

from flask import redirect, request

import oauth2client.client as oc
import gdata.gauth
import gdata.contacts.client

from models import UserData


flow = oc.flow_from_clientsecrets('client_secrets.json', scope='https://www.google.com/m8/feeds', redirect_uri='http://localhost:8080/gapicallback')

def login():
    auth_uri = flow.step1_get_authorize_url()
    return auth_uri


def check_login(request):
    code = request.args.get('code')
    if code is None:
        return redirect('/?error=%s' % request.args['error'])
    credentials = flow.step2_exchange(code)

    auth2token = gdata.gauth.OAuth2Token(client_id=credentials.client_id, client_secret=credentials.client_secret, scope='https://www.google.com/m8/feeds/contacts/default/full', access_token=credentials.access_token, refresh_token=credentials.refresh_token, user_agent='sites-test/1.0')
    client = gdata.contacts.client.ContactsClient()
    auth2token.authorize(client)

    query = gdata.contacts.client.ContactsQuery()
    query.max_results = 1000
    feed = client.GetContacts(q = query)

    user=UserData()
    for x in feed.entry:
        user.save_user(x, 'google')

    return 'Success'