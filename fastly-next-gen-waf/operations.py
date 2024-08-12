""""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError
import requests
from .constants import *

logger = get_logger('fastly-next-gen-waf')


class FastlyNGWAF:
    def __init__(self, config):
        self.server_url = config.get('server_url').strip('/')
        if not (self.server_url.startswith('http://') or self.server_url.startswith('https://')):
            self.server_url = 'https://' + self.server_url
        if not self.server_url.endswith('/api/v0'):
            self.server_url += '/api/v0'
        self.email_id = config.get('email_id')
        self.api_key = config.get('api_key')
        self.verify_ssl = config.get('verify_ssl', True)

    def make_request(self, endpoint, method='GET', data=None, params=None, files=None):
        try:
            url = self.server_url + endpoint
            logger.info('Executing url {}'.format(url))
            headers = {
                'Content-type': 'application/json',
                'x-api-user': self.email_id,
                'x-api-token': self.api_key
            }
            # CURL UTILS CODE
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, url, headers=headers, params=params, data=data, verify_ssl=self.verify_ssl)
            except Exception as err:
                logger.debug(f"Error in curl utils: {str(err)}")

            response = requests.request(method, url, params=params, files=files, data=data, headers=headers,
                                        verify=self.verify_ssl)
            if response.ok:
                logger.debug('successfully get response for url {}'.format(url))
                if method.lower() == 'delete':
                    return response
                else:
                    return response.json()
            elif response.status_code == 400:
                error_response = response.json()
                error_description = error_response['message'] if error_response.get('message') else error_response
                raise ConnectorError({'error_description': error_description})
            elif response.status_code == 401:
                error_response = response.json()
                if error_response.get('error'):
                    error_description = error_response['error']
                else:
                    error_description = error_response['message'] if error_response.get('message') else error_response
                raise ConnectorError({'error_description': error_description})
            elif response.status_code == 404:
                error_response = response.json()
                if error_response.get('message'):
                    error_description = error_response['message'] if error_response.get('message') else error_response
                    raise ConnectorError({'error_description': error_description})
                raise ConnectorError(error_response)
            else:
                try:
                    logger.error(response.json())
                    raise ConnectorError(str(response.json()))
                except Exception as err:
                    logger.debug(str(err))
                    error_response = {'status_code': response.status_code,
                                      'message': response.text if response.text else response.reason}
                    logger.error(str(error_response))
                    raise ConnectorError(str(error_response))
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError('The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            raise ConnectorError(str(err))


def build_payload(params: dict):
    payload = {}
    for k, v in params.items():
        if isinstance(v, dict) and v:
            payload[k] = build_payload(v)
        elif isinstance(v, (int, bool)) or v:
            payload[k] = v
    return payload


def get_site_allow_list(config, params):
    client = FastlyNGWAF(config)
    endpoint = ACCESS_ALLOW_LIST_ENDPOINT.format(params.get('corporation'), params.get('site_name'))
    return client.make_request(endpoint=endpoint)


def add_ip_to_allow_list(config, params):
    client = FastlyNGWAF(config)
    endpoint = ACCESS_ALLOW_LIST_ENDPOINT.format(params.pop('corporation', ''), params.pop('site_name', ''))
    payload = build_payload(params)
    return client.make_request(endpoint, method='PUT', data=payload)


def remove_ip_from_allow_list(config, params):
    client = FastlyNGWAF(config)
    endpoint = REMOVE_ALLOW_LIST_ENDPOINT.format(params.get('corporation'), params.get('site_name'), params.get('id'))
    result = client.make_request(endpoint=endpoint, method='DELETE')
    return {"status": 204, 'message': "Successful removal from the allow list"}


def get_site_block_list(config, params):
    client = FastlyNGWAF(config)
    endpoint = ACCESS_BLOCK_LIST_ENDPOINT.format(params.get('corporation'), params.get('site_name'))
    return client.make_request(endpoint=endpoint)


def add_ip_to_block_list(config, params):
    client = FastlyNGWAF(config)
    endpoint = ACCESS_BLOCK_LIST_ENDPOINT.format(params.pop('corporation', ''), params.pop('site_name', ''))
    payload = build_payload(params)
    return client.make_request(endpoint=endpoint, method='PUT', data=payload)


def remove_ip_from_block_list(config, params):
    client = FastlyNGWAF(config)
    endpoint = REMOVE_BLOCK_LIST_ENDPOINT.format(params.get('corporation'), params.get('site_name'), params.get('id'))
    result = client.make_request(endpoint=endpoint, method='DELETE')
    return {"status": 204, 'message': "Successful removal from the block list"}


def get_all_site_lists(config, params):
    client = FastlyNGWAF(config)
    endpoint = SITE_LIST_ENDPOINT.format(params.get('corporation'), params.get('site_name'))
    return client.make_request(endpoint=endpoint)


def get_site_list_by_id(config, params):
    client = FastlyNGWAF(config)
    endpoint = SITE_LIST_DETAILS_ENDPOINT.format(params.get('corporation'), params.get('site_name'), params.get('id'))
    return client.make_request(endpoint=endpoint)


def list_sites_in_corp(config, params):
    client = FastlyNGWAF(config)
    endpoint = CORP_SITES_ENDPOINT.format(params.pop('corporation', ''))
    params['agent_level'] = params.get('agent_level', '').lower()
    payload = build_payload(params)
    return client.make_request(endpoint=endpoint, params=payload)


def list_corps(config, params):
    client = FastlyNGWAF(config)
    return client.make_request(endpoint=LIST_CORPS_ENDPOINT)


def list_alerts(config, params):
    client = FastlyNGWAF(config)
    endpoint = LIST_ALERT_ENDPOINT.format(params.get('corporation'), params.get('site_name'))
    return client.make_request(endpoint=endpoint)


def get_alert_details(config, params):
    client = FastlyNGWAF(config)
    endpoint = GET_ALERT_ENDPOINT.format(params.get('corporation'), params.get('site_name'), params.get('id'))
    return client.make_request(endpoint=endpoint)


def update_alert(config, params):
    client = FastlyNGWAF(config)
    endpoint = GET_ALERT_ENDPOINT.format(params.pop('corporation', ''), params.pop('site_name', ''), params.pop('id', ''))
    params['action'] = params.get('action', '').lower()
    payload = build_payload(params)
    return client.make_request(endpoint=endpoint, method='PATCH', data=payload)


def list_events(config, params):
    client = FastlyNGWAF(config)
    endpoint = LIST_EVENTS_ENDPOINT.format(params.pop('corporation', ''), params.pop('site_name', ''))
    for field in ['status', 'action', 'sort']:
        params[field] = params.get(field, '').lower()
    for field in ['from', 'until']:
        if params.get(field):
            params[field] = int(datetime.strptime(params[field], "%Y-%m-%dT%H:%M:%S.%fZ").timestamp())
    payload = build_payload(params)
    return client.make_request(endpoint=endpoint, params=payload)


def get_event_details(config, params):
    client = FastlyNGWAF(config)
    endpoint = GET_EVENTS_ENDPOINT.format(params.get('corporation'), params.get('site_name'), params.get('id'))
    return client.make_request(endpoint=endpoint)


def expire_event_by_id(config, params):
    client = FastlyNGWAF(config)
    endpoint = EXPIRE_EVENT_ENDPOINT.format(params.get('corporation'), params.get('site_name'), params.get('id'))
    return client.make_request(endpoint=endpoint, method='POST')


def check_health(config):
    list_corps(config, {})
    return True


operations = {
    'get_site_allow_list': get_site_allow_list,
    'add_ip_to_allow_list': add_ip_to_allow_list,
    'remove_ip_from_allow_list': remove_ip_from_allow_list,
    'get_site_block_list': get_site_block_list,
    'add_ip_to_block_list': add_ip_to_block_list,
    'remove_ip_from_block_list': remove_ip_from_block_list,
    'get_all_site_lists': get_all_site_lists,
    'get_site_list_by_id': get_site_list_by_id,
    'list_sites_in_corp': list_sites_in_corp,
    'list_corps': list_corps,
    'list_alerts': list_alerts,
    'get_alert_details': get_alert_details,
    'update_alert': update_alert,
    'list_events': list_events,
    'get_event_details': get_event_details,
    'expire_event_by_id': expire_event_by_id
}
