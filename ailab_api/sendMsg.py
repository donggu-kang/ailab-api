import json
import requests


def send_sms(text, phone_number, api_key):
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    temp_dict = dict()
    temp_dict['text'] = str(text)
    temp_dict['phone'] = str(phone_number)
    temp_dict['key'] = str(api_key)
    json_data = json.dumps(temp_dict)

    try:
        request = requests.post('http://aiapi.ourplan.kr:5000/sms', headers=headers, data=json_data)
        return {'status': int(request.status_code), 'type': 'sms', 'text': str(text)}

    except Exception as error:
        return {'status': 'error', 'type': 'sms', 'text': str(error)}



