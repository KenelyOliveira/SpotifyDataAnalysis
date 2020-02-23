import requests
import songsbyseason.helpers as helpers
print(helpers.format_query('Olá mundo'))

def get_artistByName(payload):
    gateway = helpers.load_config()['gateways'][0]
    headers = { 'user-agent': gateway['user_agent'] }
    payload['api_key'] = gateway['api_key']
    payload['format'] = 'json'

    response = requests.get(gateway['url'], headers = headers, params = payload)
    return response