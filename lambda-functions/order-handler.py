import json
import boto3
import os

sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

ORDERS_TABLE = "orders"

SNS_TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

table = dynamodb.Table(ORDERS_TABLE)


def lambda_handler(event, context):

    body = json.loads(event["body"])

    order = {
        "orderId": body["orderId"],
        "customer": body["customer"],
        "email": body["email"],
        "product": body["product"],
        "quantity": body["quantity"]
    }

    table.put_item(Item=order)

    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=json.dumps(order)
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "message": "Order sent successfully",
            "order": order,
            "messageId": response["MessageId"]
        })
    }
