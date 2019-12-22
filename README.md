# ailab-api

## How to use
Install : ```pip install ailab-api```

This version : ```pip install ailab-api==0.3```

Upgrade : ```pip install --upgrade ailab-api```

Import : ```import ailab_api```

### Example Code 
```python
>>> from ailab_api.sendMsg import sendSms

>>> response = sendSms('[TEST] TEST SMS 12345','01012341234','API Key Here')
# response = sendSms(text='[TEST] TEST SMS 12345',phone='01012341234',key='API Key Here')
>>> print(response)
{'text': '[OK] : 200 - [TEST] TEST SMS 12345'}
```

### 403 - API Key Error
```python
>>> response = sendSms('[TEST] TEST SMS 12345','01012341234','API Key Here')
>>> print(response)
{'text': '[ERROR] : 403 - API Key Error'}
```
