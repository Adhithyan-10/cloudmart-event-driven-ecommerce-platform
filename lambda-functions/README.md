# ⚡ AWS Lambda Functions

This folder contains all AWS Lambda functions used in the **Smart Event-Driven Order Processing System**.

These functions form the core business logic of the application and work together to process customer orders asynchronously using AWS serverless services.

---

# 📂 Lambda Functions Structure

```text
lambda-functions/
│
├── order-handler/
│   └── lambda_function.py
│
├── inventory-handler/
│   └── lambda_function.py
│
├── payment-handler/
│   └── lambda_function.py
│
└── notification-handler/
    └── lambda_function.py
```

---

# 🔗 Lambda Functions

| Function | Purpose |
|-----------|-----------|
| [Order Handler](./order-handler/lambda_function.py) | Receives customer orders from API Gateway and publishes events to SNS |
| [Inventory Handler](./inventory-handler/lambda_function.py) | Updates inventory stock and performs idempotency checks |
| [Payment Handler](./payment-handler/lambda_function.py) | Simulates payment processing workflow |
| [Notification Handler](./notification-handler/lambda_function.py) | Sends order confirmation notifications |

---

# 🏗️ Event Processing Flow

```text
Customer
    │
    ▼
CloudFront + S3 Frontend
    │
    ▼
API Gateway
    │
    ▼
Order Handler Lambda
    │
    ▼
SNS Topic
    │
 ┌──┼───────────────┐
 ▼  ▼               ▼
Inventory Queue  Payment Queue  Notification Queue
 │                │              │
 ▼                ▼              ▼
Inventory      Payment      Notification
Handler        Handler      Handler
 │
 ▼
DynamoDB
```

---

# 1️⃣ Order Handler

📄 Code:

[View Order Handler](./order-handler/lambda_function.py)

---

## Purpose

The Order Handler Lambda acts as the entry point of the backend system.

It receives customer orders from API Gateway and initiates the event-driven workflow.

---

## Trigger

```text
API Gateway
```

---

## Responsibilities

- Receive customer order
- Validate incoming request
- Generate order record
- Store order in DynamoDB
- Publish event to SNS Topic
- Return success response

---

## Services Used

- API Gateway
- DynamoDB
- SNS
- CloudWatch

---

## Sample Order

```json
{
  "orderId": "ORD001",
  "customer": "Adhithyan",
  "email": "adhi@gmail.com",
  "product": "Laptop",
  "quantity": 1
}
```

---

## Output

```json
{
  "message": "Order sent successfully"
}
```

---

# 2️⃣ Inventory Handler

📄 Code:

[View Inventory Handler](./inventory-handler/lambda_function.py)

---

## Purpose

The Inventory Handler manages stock updates after an order is received.

This function ensures inventory consistency and prevents duplicate stock deductions.

---

## Trigger

```text
Inventory Queue (SQS)
```

---

## Responsibilities

- Consume messages from Inventory Queue
- Read order details
- Verify stock availability
- Reduce stock quantity
- Update Inventory table
- Mark order as processed
- Perform idempotency validation

---

## Services Used

- SQS
- DynamoDB
- CloudWatch

---

## Idempotency Protection

The function checks whether an order has already been processed.

Example:

```text
ORD009 already processed
```

Stock will not be deducted again.

This prevents duplicate inventory updates caused by retries.

---

## DynamoDB Update

Before:

```text
Laptop : 50
```

After Order Quantity = 5

```text
Laptop : 45
```

---

# 3️⃣ Payment Handler

📄 Code:

[View Payment Handler](./payment-handler/lambda_function.py)

---

## Purpose

The Payment Handler simulates a payment processing service.

In production, this function could integrate with:

- Stripe
- Razorpay
- PayPal
- Amazon Pay

---

## Trigger

```text
Payment Queue (SQS)
```

---

## Responsibilities

- Consume payment events
- Validate order information
- Process payment request
- Update payment status
- Store result in DynamoDB

---

## Services Used

- SQS
- DynamoDB
- CloudWatch

---

## Example Status

```json
{
  "paymentStatus": "SUCCESS"
}
```

---

# 4️⃣ Notification Handler

📄 Code:

[View Notification Handler](./notification-handler/lambda_function.py)

---

## Purpose

The Notification Handler sends customer notifications after order processing.

For this project, notifications are simulated using CloudWatch Logs.

---

## Trigger

```text
Notification Queue (SQS)
```

---

## Responsibilities

- Consume notification events
- Generate confirmation message
- Log notification details
- Simulate email delivery

---

## Services Used

- SQS
- CloudWatch

---

## Example Notification

```text
Email Sent

Customer : Adhithyan
Product  : Laptop
Quantity : 1
```

---

# 🔒 Reliability Features

## SNS Fan-Out Architecture

One order event is automatically distributed to multiple services.

```text
SNS Topic
│
├── Inventory Service
├── Payment Service
└── Notification Service
```

---

## Dead Letter Queue (DLQ)

Inventory Queue is configured with a DLQ.

Benefits:

- Failed messages are isolated
- No data loss
- Easy troubleshooting
- Improved reliability

---

## CloudWatch Logging

All Lambda functions send logs to CloudWatch.

Examples:

- Order Received
- Inventory Updated
- Payment Successful
- Notification Sent

---

# 🚀 Benefits of Serverless Architecture

✅ Event Driven

✅ Auto Scaling

✅ Fault Tolerant

✅ Fully Managed

✅ Pay As You Go

✅ Decoupled Microservices

✅ High Availability

---

# 🎯 Interview Questions

### Why use SNS instead of directly invoking Lambdas?

SNS provides asynchronous communication and fan-out architecture, enabling multiple services to process the same event independently.

---

### Why use SQS between SNS and Lambda?

SQS improves reliability, buffering, fault tolerance, and message durability.

---

### Why implement idempotency?

To prevent duplicate inventory deductions during retries or repeated message delivery.

---

### Why use a DLQ?

To capture failed messages and prevent message loss during processing failures.

---

### What architecture pattern is used?

**Event-Driven Serverless Microservices Architecture**
