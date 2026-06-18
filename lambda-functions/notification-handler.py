import json


def lambda_handler(event, context):

    print("Notification Service Triggered")

    for record in event["Records"]:

        body = json.loads(record["body"])

        if "Message" in body:
            order = json.loads(body["Message"])
        else:
            order = body

        print("Sending Notification For Order:")
        print(order)

        print(
            f"""
            Email Sent

            Customer : {order['customer']}
            Product  : {order['product']}
            Quantity : {order['quantity']}
            """
        )

    return {
        "statusCode": 200
    }
