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
    serviceId = "ncp:sms:kr:263531129738:jalclean"
    # 플랫폼 api key
    access_key = "pY51xDidzwhzpdL91p1P"
    # 플랫폼 api sercret key
    secret_key = "7wA0G8yZQxqMnPa9TrEU7uL2ahha4IaD5s7Z9YlD"

    uri = requestUrl1 + serviceId + requestUrl2
    apiUrl = url + uri

    secret_key = bytes(secret_key, 'UTF-8')

    method = "POST"

    signature = method + " " + uri + "\n" + timestamp + "\n" + access_key

    signature = bytes(signature, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, signature, digestmod=hashlib.sha256).digest())

    message_value = "성명 : " + data['clientName'] + "\n전화번호 : " + data['clientPhone']
    message_value = message_value + "\n주소 : " + data['requestAddress'] + "\n희망 날짜 : " + data['requestDate']

    phone_number = "01056671035"

    messages = { "to" : phone_number}
    body = {
        "type" : "SMS",
        "contentType" : "COMM",
        "from" : phone_number,
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