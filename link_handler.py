# -*- coding: utf-8 -*-
# !/usr/bin/env python
import requests
import boto3
import os


def addLink(sURL, chatId, userName, url):
    requests.get('{}?chat_id={}&text={}'.format(sURL,
                                                chatId,
                                                url + '\n 이름은?'))

    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('test_jupjup_links')
    table.put_item(
        Item={
            'user': userName,
            'tag_name': os.environ['temp_table'],
            'url': url
            })


def handleMessage(sURL, chatId, userName, tagName):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('test_jupjup_links')
    res = table.get_item(
        Key={
            'user': userName,
            'tag_name': os.environ['temp_table']})
    temp_link = res.get('Item')
    if temp_link:
        url = temp_link['url']
        table.update_item(
            Key={
                'user': userName,
                'tag_name': tagName},
            UpdateExpression='SET url_list = list_append(if_not_exists(url_list, :empty_list), :i)',
            ExpressionAttributeValues={
                ':empty_list': [],
                ':i': [url]},
            ReturnValues='UPDATED_NEW')

        table.delete_item(
            Key={
                'user': userName,
                'tag_name': 'temp_0first0'})
        
        requests.get('{}?chat_id={}&text={}'.format(sURL,
                                                    chatId,
                                                    'ㅇㅋ'))
    else:
        res = table.get_item(
            Key={
                'user': userName,
                'tag_name': tagName})
        item = res.get('Item')
        if item:
            print(item['url_list'])
            requests.get('{}?chat_id={}&text={}'.format(sURL,
                                                        chatId,
                                                        item['url_list']))
        else:
            requests.get('{}?chat_id={}&text={}'.format(sURL,
                                                        chatId,
                                                        '?? 없는 태그인데'))
