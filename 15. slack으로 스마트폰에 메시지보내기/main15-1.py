import requests
import json

# Slack Webhook URL
slack_webhook_url = "https://hooks.slack.com/services/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"

def sendSlackWebhook(strText):
    headers = {
    "Content-type": "application/json"
    }

    data = {
        "text" : strText
    }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    
    if res.status_code == 200:
        return "ok"
    else:
        return "error"

print(sendSlackWebhook("안녕하세요 파이썬에서 보내는 메시지 입니다."))