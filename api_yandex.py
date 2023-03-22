import requests
import json
import configparser


folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'


def get_token_ya():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    token = config['YA']['TOKEN_YA']
    return token


def _get_headers(token):
    return {
        'Content-type': 'application/json',
        'Authorization': f'OAuth {token}'
    }


def create_folder(token, folder_name):
    params = {"path": {folder_name}}
    create_folder = requests.put(folder_url, headers=_get_headers(token), params=params)
    return create_folder.status_code


def get_metatype_folder(token, folder_name):
    params = {'path': {folder_name}}
    result = requests.get(folder_url, headers=_get_headers(token), params=params)
    if result.status_code == 200:
        res_dict = json.loads(result.text)
        return res_dict.get('type')
