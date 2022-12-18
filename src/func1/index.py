import json


def handler(event, context):
    body = {
        "message": "func1",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
