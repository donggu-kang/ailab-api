import json
import requests


def sendSms(text, phone, key):
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    temp_dict = dict()
    temp_dict['text'] = str(text)
    temp_dict['phone'] = str(phone)
    temp_dict['key'] = str(key)
    json_data = json.dumps(temp_dict)

    try:
        request = requests.post('http://aiapi.ourplan.kr:5000/sms', headers=headers, data=json_data)

        if int(request.status_code) == 200:
            return {'text': '[OK] : 200 - ' + str(text)}
        elif int(request.status_code) == 500:
            return {'text': '[ERROR] : 500 - Server Error'}
        elif int(request.status_code) == 403:
            return {'text': '[ERROR] : 403 - API Key Error'}
    except Exception as error:
        return {'text': '[ERROR] : ' + str(error)}
