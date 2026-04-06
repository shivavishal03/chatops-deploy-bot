import json
import urllib.parse

def lambda_handler(event, context):
    body = event.get("body", "")
    parsed = urllib.parse.parse_qs(body)

    command = parsed.get("command", [""])[0]
    text = parsed.get("text", [""])[0]

    message = f"Received command: {command} {text}"

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "response_type": "in_channel",
            "text": message
        })
    }