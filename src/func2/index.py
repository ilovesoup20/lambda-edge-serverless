import json


def handler(event, context):
    body = {
        "message": "func2",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
