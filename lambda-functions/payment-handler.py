import json
import boto3

dynamodb = boto3.resource('dynamodb')

orders_table = dynamodb.Table("orders")


def lambda_handler(event, context):

    print("Payment Service Triggered")

    for record in event["Records"]:

        body = json.loads(record["body"])

        if "Message" in body:
            order = json.loads(body["Message"])
        else:
            order = body

        print("Payment Processing Order:")
        print(order)

        orders_table.update_item(
            Key={
                "orderId": order["orderId"]
            },
            UpdateExpression="SET paymentStatus = :s",
            ExpressionAttributeValues={
                ":s": "SUCCESS"
            }
        )

        print("Payment Successful")

    return {
        "statusCode": 200
    }
