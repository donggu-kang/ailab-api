# ailab-api

## How to use
Install : ```pip install ailab-api```

This version : ```pip install ailab-api==0.6```

Upgrade : ```pip install --upgrade ailab-api```

Import : ```import ailab_api```

### Example Code 
```python
>>> from ailab_api.sendMsg import send_sms

>>> response = send_sms('[TEST] TEST SMS 12345','01012341234','API Key Here')
# response = send_sms(text='[TEST] TEST SMS 12345',phone_number='01012341234',api_key='API Key Here')
>>> print(response)
{'status': 200, 'type': 'sms', 'text': '[TEST] TEST SMS 12345'}


>>> response = send_lms('[TEST] TEST LMS 12345','01012341234','API Key Here')
# response = send_lms(text='[TEST] TEST SMS 12345',phone_number='01012341234',api_key='API Key Here')
>>> print(response)
{'status': 200, 'type': 'lms', 'text': '[TEST] TEST LMS 12345'}

```

### Example Error
```python
>>> response = send_sms('[TEST] TEST SMS 12345','01012341234','API Key Here')
>>> print(response)
{'status': 'error', 'type': 'sms', 'text': 'Error Message Here'}
```
