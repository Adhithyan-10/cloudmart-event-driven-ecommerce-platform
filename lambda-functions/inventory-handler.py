import json
import boto3

dynamodb = boto3.resource('dynamodb')

inventory_table = dynamodb.Table("Inventory")
orders_table = dynamodb.Table("orders")


def lambda_handler(event, context):

    print("Inventory Service Triggered")

    for record in event["Records"]:

        body = json.loads(record["body"])

        if "Message" in body:
            order = json.loads(body["Message"])
        else:
            order = body

        order_id = order["orderId"]

        response = orders_table.get_item(
            Key={"orderId": order_id}
        )

        item = response.get("Item")

        if item and item.get("inventoryProcessed"):

            print(f"Order {order_id} already processed. Skipping.")
            continue

        product = order["product"]
        quantity = int(order["quantity"])

        inventory = inventory_table.get_item(
            Key={"productId": product}
        )

        current_stock = inventory["Item"]["stock"]

        if current_stock < quantity:
            raise Exception("Insufficient stock")

        inventory_table.update_item(
            Key={"productId": product},
            UpdateExpression="SET stock = stock - :q",
            ExpressionAttributeValues={
                ":q": quantity
            }
        )

        orders_table.update_item(
            Key={"orderId": order_id},
            UpdateExpression="SET inventoryProcessed = :v",
            ExpressionAttributeValues={
                ":v": True
            }
        )

        print("Inventory Updated Successfully")

    return {
        "statusCode": 200
    }
