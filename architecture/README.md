# 🏗️ System Architecture

CloudMart follows an Event-Driven Serverless Architecture on AWS. The project demonstrates how modern e-commerce systems can be designed using asynchronous communication patterns, decoupled services, and scalable cloud-native components.

This repository contains two architecture designs:

1. **Current Implementation Architecture** – The version that has been implemented and tested.
2. **Future Production Architecture** – An enhanced enterprise-grade design showing how the platform can evolve for real-world production workloads.

---

# Current Implementation Architecture

![Current Architecture](architecture/beforefuture.png)

## Overview

The current implementation demonstrates a fully serverless event-driven e-commerce platform built using AWS services including:

- Amazon S3
- Amazon CloudFront
- Amazon API Gateway
- AWS Lambda
- Amazon SNS
- Amazon SQS
- Amazon DynamoDB
- Amazon CloudWatch

The architecture follows the **SNS Fan-Out Pattern**, where a single event is distributed to multiple independent services for asynchronous processing.

---

## Detailed Flow

### 1. Customer Places an Order

The customer accesses the CloudMart web application through Amazon CloudFront, which delivers static content stored in Amazon S3.

```
Customer
    ↓
CloudFront
    ↓
S3 Hosted Frontend
```

---

### 2. API Request Processing

When the customer clicks **Place Order**, the frontend sends a request to Amazon API Gateway.

API Gateway acts as the secure entry point for backend services.

```
Frontend
    ↓
API Gateway
```

---

### 3. Order Lambda Execution

API Gateway invokes the Order Lambda.

The Order Lambda:

- Validates the request
- Generates a unique Order ID
- Creates the order event
- Stores the initial order information
- Publishes the event to Amazon SNS

```
API Gateway
    ↓
Order Lambda
    ↓
SNS Topic
```

---

### 4. SNS Fan-Out Pattern

Amazon SNS receives the order event and distributes it simultaneously to multiple SQS queues.

```
SNS Topic
   ├── Inventory Queue
   ├── Payment Queue
   └── Notification Queue
```

This allows all services to work independently without directly communicating with each other.

---

### 5. Inventory Service

The Inventory Queue triggers the Inventory Lambda.

Responsibilities:

- Idempotency validation
- Order validation
- Stock update
- Inventory persistence

Data is stored in DynamoDB Inventory Table.

```
Inventory Queue
      ↓
Inventory Lambda
      ↓
Inventory Table
```

---

### 6. Payment Service

The Payment Queue triggers the Payment Lambda.

Responsibilities:

- Payment processing
- Order status update
- Payment workflow execution

```
Payment Queue
      ↓
Payment Lambda
```

---

### 7. Notification Service

The Notification Queue triggers the Notification Lambda.

Responsibilities:

- Generate notification content
- Send customer notifications
- Update notification status

```
Notification Queue
      ↓
Notification Lambda
```

---

### 8. Monitoring & Reliability

CloudWatch provides:

- Logs
- Metrics
- Alarms
- Operational visibility

Dead Letter Queues (DLQ) capture failed messages for troubleshooting and recovery.

---

## Key Architectural Patterns

- Event-Driven Architecture
- SNS Fan-Out Pattern
- Asynchronous Processing
- Idempotent Consumers
- Dead Letter Queue Pattern
- Serverless Microservices

---

# Future Production Architecture

![Future Architecture](architecture/futureenc.png)

## Overview

The Future Production Architecture transforms CloudMart into an enterprise-grade e-commerce platform capable of handling real payment processing, real-time notifications, event integrations, and advanced business workflows.

Major enhancements include:

- Stripe / Razorpay Integration
- Payment Webhook Processing
- Amazon SES Email Notifications
- WebSocket Real-Time Updates
- EventBridge Enterprise Integrations
- Payment Failure Recovery
- Inventory Release Automation

---

## Detailed Flow

### 1. Customer Places Order

The customer submits an order through the frontend.

```
Customer
    ↓
API Gateway
    ↓
Order Lambda
```

The Order Lambda:

- Validates request
- Generates Order ID
- Stores order in DynamoDB
- Sets status as PENDING
- Publishes OrderCreated Event

---

### 2. SNS Fan-Out Processing

The OrderCreated event is published to SNS.

SNS distributes the event simultaneously to:

```
Inventory Queue
Payment Queue
```

This allows inventory reservation and payment processing to begin independently.

---

### 3. Inventory Reservation

Inventory Queue triggers Inventory Lambda.

Responsibilities:

- Validate order
- Reserve stock
- Update inventory table
- Handle inventory release on payment failure

```
Inventory Queue
      ↓
Inventory Lambda
      ↓
Inventory Table
```

---

### 4. Payment Processing

Payment Queue triggers Payment Lambda.

Responsibilities:

- Create payment session
- Call Stripe / Razorpay
- Initiate customer payment

```
Payment Queue
      ↓
Payment Lambda
      ↓
Stripe / Razorpay
```

---

### 5. Payment Webhook Processing

After payment completion, Stripe/Razorpay sends a webhook event.

```
Stripe / Razorpay
        ↓
Webhook Endpoint
        ↓
Payment Webhook Lambda
```

The Webhook Lambda:

- Validates webhook signature
- Verifies payment
- Updates order status
- Processes payment events

Order status becomes:

```
PENDING
   ↓
PAID
   ↓
SHIPPED
   ↓
DELIVERED
   ↓
COMPLETED

FAILED (Terminal State)
```

---

### 6. Payment Completion Event

Once payment is verified, the Payment Webhook Lambda publishes a PaymentCompleted event.

```
Payment Webhook Lambda
        ↓
SNS Topic
(PaymentCompleted Event)
```

This ensures notifications are sent only after successful payment confirmation.

---

### 7. Customer Notifications

The PaymentCompleted SNS Topic triggers the Notification Queue.

```
PaymentCompleted SNS
         ↓
Notification Queue
         ↓
Notification Lambda
```

The Notification Lambda:

- Sends Order Confirmation
- Sends Payment Success Notification
- Sends Shipping Updates
- Publishes Real-Time Updates
- Sends Customer Emails

---

### 8. Real-Time Updates

Customers receive live updates through WebSockets.

```
Notification Lambda
        ↓
WebSocket API
        ↓
Customer App
```

Examples:

- Payment Success
- Order Confirmed
- Order Shipped
- Inventory Updated
- Order Status Changed

---

### 9. Email Notifications

Amazon SES delivers transactional emails.

```
Notification Lambda
        ↓
Amazon SES
        ↓
Customer Email
```

---

### 10. Payment Failure Recovery

If payment fails:

```
PaymentFailed Event
        ↓
Inventory Release
        ↓
Inventory Lambda
        ↓
Inventory Table
```

The system automatically restores reserved stock.

Additional actions:

- Failed payment email
- Retry payment link
- Payment recovery workflow

---

### 11. Enterprise Integrations

EventBridge enables future integrations.

```
Order Lambda
      ↓
EventBridge
      ↓
Enterprise Integrations
```

Potential consumers:

- Analytics Platforms
- Data Lakes
- BI Dashboards
- Third-Party Applications
- Cross-Account Integrations
- Marketing Platforms

---

# Architecture Evolution

| Current Implementation | Future Production Architecture |
|------------------------|-------------------------------|
| Basic Event Processing | Enterprise Event Processing |
| Simulated Payments | Stripe/Razorpay Integration |
| Direct Notifications | Payment-Driven Notifications |
| Single SNS Workflow | Multi-Stage Event Workflows |
| Basic Monitoring | Enterprise Observability |
| No Webhooks | Payment Webhook Validation |
| No Real-Time Updates | WebSocket Notifications |
| No EventBridge | Enterprise Integrations |
| Basic Recovery | Automated Failure Handling |

---

## Result

CloudMart demonstrates how a simple event-driven AWS application can evolve into a production-ready, enterprise-scale e-commerce platform using modern cloud-native architectural patterns.
