# AWS Lambda Functions

This folder contains all Lambda functions used in the Smart Event-Driven Order Processing System.

---

## Lambda Functions

### 1. Order Handler

Receives orders from API Gateway.

Responsibilities:

- Accept order requests
- Validate request payload
- Store order in DynamoDB
- Publish event to SNS Topic

Trigger:

API Gateway

---

### 2. Inventory Handler

Processes inventory updates.

Responsibilities:

- Consume messages from Inventory Queue
- Verify stock availability
- Reduce inventory count
- Perform idempotency check
- Prevent duplicate stock reduction

Trigger:

Inventory SQS Queue

---

### 3. Payment Handler

Simulates payment processing.

Responsibilities:

- Consume payment events
- Update order payment status
- Log payment completion

Trigger:

Payment SQS Queue

---

### 4. Notification Handler

Handles customer notifications.

Responsibilities:

- Consume notification events
- Send order confirmation
- Log notification details

Trigger:

Notification SQS Queue

---

## Event Flow

API Gateway
↓
Order Handler
↓
SNS Topic
↓
SQS Fan-Out
├── Inventory Queue
├── Payment Queue
└── Notification Queue
↓
Lambda Consumers
↓
DynamoDB Updates & Notifications

---

## AWS Services Used

- AWS Lambda
- Amazon SNS
- Amazon SQS
- Amazon DynamoDB
- Amazon API Gateway
- Amazon CloudWatch

---

## Architecture Benefits

- Fully Serverless
- Event-Driven
- Scalable
- Fault Tolerant
- Decoupled Services
- Supports DLQ Recovery
- Cost Optimized
