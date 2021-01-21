import json, time
import requests
import base64
import hmac
import hashlib


def send_sms(data):

    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)

    url = "https://sens.apigw.ntruss.com"

    requestUrl1 = "/sms/v2/services/"
    requestUrl2 = "/messages"
    # 콘솔 프로젝트 key
    serviceId = ""
    # 플랫폼 api key
    access_key = ""
    # 플랫폼 api sercret key
    secret_key = ""

    uri = requestUrl1 + serviceId + requestUrl2
    apiUrl = url + uri

    secret_key = bytes(secret_key, 'UTF-8')

    method = "POST"

    signature = method + " " + uri + "\n" + timestamp + "\n" + access_key

    signature = bytes(signature, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, signature, digestmod=hashlib.sha256).digest())

    message_value = "성명 : " + data['clientName'] + "\n전화번호 : " + data['clientPhone']
    message_value = message_value + "\n주소 : " + data['requestAddress'] + "\n희망 날짜 : " + data['requestDate']

    messages = { "to" : "01088525151"}
    body = {
        "type" : "SMS",
        "contentType" : "COMM",
        "from" : "01088525151",
        "subject" : "subject",
        "content" : message_value,
        "messages" : [messages]
    }

    body_value = json.dumps(body)

    headers = {
        'Content-Type' : 'application/json; charset=utf-8',
        'x-ncp-apigw-timestamp': timestamp,
        'x-ncp-iam-access-key': access_key,
        'x-ncp-apigw-signature-v2': signingKey
    }

    res = requests.post(apiUrl, headers=headers, data=body_value)

    return