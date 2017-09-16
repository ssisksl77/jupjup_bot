# -*- coding: utf-8 -*-
# !/usr/bin/env python
# import json
import requests
import validators
import os

def lambda_function(event, context):
    msg = event['message']
    sURL = os.environ['telegram_token']
    chat_id = msg['chat']['id']
    url = msg['text']
    if validators.url(url) or validators.url('http://' + url):
        requests.get('{}?chat_id={}&text={}'.format(sURL,
                                                    chat_id,
                                                    url + ' 이놈은 진짜구먼?'))
    else:
        requests.get('{}?chat_id={}&text={}'.format(sURL,
                                                    chat_id,
                                                    '이건 링크가 아니잖아!'))
    
    return {'content': 200}
