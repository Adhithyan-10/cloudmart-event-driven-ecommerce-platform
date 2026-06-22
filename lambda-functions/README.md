# ⚡ AWS Lambda Functions

This folder contains all AWS Lambda functions used in the **Smart Event-Driven Order Processing System**.

These functions form the core business logic of the application and work together to process customer orders asynchronously using AWS serverless services.

---

# 📂 Lambda Functions Structure

```text
lambda-functions/
│
├── README.md
├── order-handler.py
├── inventory-handler.py
├── payment-handler.py
└── notification-handler.py
```

---

# 🔗 Lambda Functions

| Function | Purpose |
|-----------|-----------|
| [📄 Order Handler](./order-handler.py) | Receives customer orders from API Gateway and publishes events to SNS |
| [📄 Inventory Handler](./inventory-handler.py) | Updates inventory stock and performs idempotency checks |
| [📄 Payment Handler](./payment-handler.py) | Simulates payment processing workflow |
| [📄 Notification Handler](./notification-handler.py) | Sends order confirmation notifications |

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

📄 Source Code:

👉 **[View Order Handler](./order-handler.py)**

---

## Purpose

The Order Handler Lambda acts as the entry point of the backend system.

It receives customer orders from API Gateway and initiates the event-driven workflow.

### Trigger

```text
API Gateway
```

### Responsibilities

- Receive customer orders
- Validate request payload
- Store order in DynamoDB
- Publish order event to SNS
- Return API response to frontend

### AWS Services Used

- Amazon API Gateway
- AWS Lambda
- Amazon SNS
- Amazon DynamoDB
- Amazon CloudWatch

### Output

```json
{
  "message": "Order sent successfully"
}
```

---

# 2️⃣ Inventory Handler

📄 Source Code:

👉 **[View Inventory Handler](./inventory-handler.py)**

---

## Purpose

The Inventory Handler manages stock updates after an order is received.

It ensures inventory consistency and prevents duplicate stock deductions.

### Trigger

```text
Inventory Queue (SQS)
```

### Responsibilities

- Consume inventory messages
- Read order details
- Verify stock availability
- Deduct inventory quantity
- Update Inventory table
- Mark order as processed
- Perform idempotency validation

### AWS Services Used

- Amazon SQS
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch

### Key Feature

#### Idempotency Protection

Example:

```text
ORD009 already processed
```

This prevents stock from being deducted multiple times if the same message is delivered again.

### Inventory Update Example

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

📄 Source Code:

👉 **[View Payment Handler](./payment-handler.py)**

---

## Purpose

The Payment Handler simulates a payment processing service.

In a production environment, this Lambda could integrate with external payment providers.

### Trigger

```text
Payment Queue (SQS)
```

### Responsibilities

- Consume payment events
- Validate order information
- Process payment workflow
- Update payment status
- Store payment result

### AWS Services Used

- Amazon SQS
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch

### Example Status

```json
{
  "paymentStatus": "SUCCESS"
}
```

### Future Enhancements

- Stripe Integration
- Razorpay Integration
- PayPal Integration
- Amazon Pay Integration

---

# 4️⃣ Notification Handler

📄 Source Code:

👉 **[View Notification Handler](./notification-handler.py)**

---

## Purpose

The Notification Handler is responsible for customer communication after order processing.

For this project, notifications are simulated using CloudWatch logs.

### Trigger

```text
Notification Queue (SQS)
```

### Responsibilities

- Consume notification events
- Generate order confirmation messages
- Simulate email delivery
- Log notification activity

### AWS Services Used

- Amazon SQS
- AWS Lambda
- Amazon CloudWatch

### Example Notification

```text
Email Sent

Customer : Adhithyan
Product  : Laptop
Quantity : 1
```

---

# 🔒 Reliability Features

## SNS Fan-Out Architecture

A single order event is automatically distributed to multiple independent services.

```text
SNS Topic
│
├── Inventory Service
├── Payment Service
└── Notification Service
```

### Benefits

- Decoupled Architecture
- Independent Processing
- High Scalability
- Improved Reliability

---

## Dead Letter Queue (DLQ)

The Inventory Queue is configured with a Dead Letter Queue.

### Benefits

- Captures failed messages
- Prevents data loss
- Enables troubleshooting
- Supports message replay

---

## CloudWatch Logging

Every Lambda function sends logs to CloudWatch.

Examples:

- Order Received
- Inventory Updated
- Payment Successful
- Notification Sent

---

# 🚀 Serverless Benefits

✅ Event Driven

✅ Auto Scaling

✅ Highly Available

✅ Fault Tolerant

✅ Cost Optimized

✅ Decoupled Microservices

✅ Fully Managed Infrastructure

---

# 🎯 Interview Questions

### Why use SNS instead of directly invoking Lambda functions?

SNS enables asynchronous communication and fan-out architecture, allowing multiple services to process the same event independently.

---

### Why place SQS between SNS and Lambda?

SQS provides buffering, durability, retry mechanisms, and fault tolerance.

---

### Why implement idempotency?

To prevent duplicate inventory deductions caused by retries or repeated message deliveries.

---

### Why use a Dead Letter Queue?

To isolate failed messages and ensure they are not lost during processing failures.

---

### What architecture pattern is implemented?

**Event-Driven Serverless Microservices Architecture**
