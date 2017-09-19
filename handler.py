# -*- coding: utf-8 -*-
# !/usr/bin/env python
# import json
import requests
import validators
import os
import link_handler


def lambda_function(event, context):
    msg = event['message']
    sURL = os.environ['telegram_token']
    chatId = msg['chat']['id']
    context = msg['text']
    userName = msg['chat']['username']

    if context[0] == '/':
        handleCommands(sURL, chatId, context[1:])
    elif validators.url(context) or validators.url('http://' + context):
        link_handler.addLink(sURL, chatId, userName, context)
    else:
        link_handler.handleMessage(sURL, chatId, userName, context)

    return {'content': 200}


def handleCommands(sURL, chatId, context):
    print(context)
    if context == 'start':
        introduceJupjup(sURL, chatId)
    elif '취소' in context:
        print('취소명령어')
        pass


def introduceJupjup(sURL, chatId):
    greeting = """링크넣기:
      1. jupjup에게 링크URL 공유
      2. jupjup이 응답하면 태그를 붙인다 or '/취소' 로 취소한다
    링크부르기: 1. 태그이름
    링크삭제: '/삭제' 태그이름 or '/삭제 링크URL'"""

    requests.get('{}?chat_id={}&text={}'.format(sURL,
                                                chatId,
                                                greeting))


def cancle():
    pass
