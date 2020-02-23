import requests
import json
import db, helpers
from utils import debug

def get_authEndpoint():
    config = helpers.load_config()['gateways'][1]
    headers = {'Authorization':'Basic %s' % helpers.format_basicAuth(config['client_id'],config['client_secret'])}
    payload = {'grant_type':'client_credentials'}
    return {'url':config['endpoints']['auth'],'headers':headers,'payload':payload}

def get_new_token():
    auth = get_authEndpoint()
    response = requests.post(auth['url'], headers = auth['headers'], data = auth['payload'])
    token = json.loads(response.text)['access_token']
    db.persist_access_token(token)
    return token

def get_requestHeader():
    access_token = db.get_access_token()
    return {'Authorization':'Bearer %s' % access_token,'Accept':'application/json','Content-Type':'application/json'}

# @debug
def get_artistByName(name):
    config = helpers.load_config()['gateways'][1]
    response = requests.get('%s%s' % (config['endpoints']['artist'], helpers.format_query(name)), headers = get_requestHeader())
    if (response.status_code == 200):
        return json.loads(response.text)
    if (response.status_code == 401):
        get_new_token()
        return get_artistByName(name)
    return {}