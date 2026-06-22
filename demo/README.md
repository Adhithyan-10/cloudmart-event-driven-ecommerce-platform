# 🎬 Demo Videos

This folder contains demonstration videos showcasing the complete implementation and working of the **CloudMart Event-Driven E-Commerce Platform**.

The videos provide a detailed walkthrough of the AWS infrastructure setup and demonstrate the complete end-to-end order processing workflow.

---

# 📹 Demo Video Links

| Video | Description |
|---------|------------|
| [🎥 AWS Console Implementation Walkthrough](https://drive.google.com/file/d/1wXQ_m7HRWb7NlWU42HiYe4tv7iYuODj0/view?usp=drive_link) | Complete AWS Console walkthrough showing architecture implementation and service configuration |
| [🎥 End-to-End Working Demo](https://drive.google.com/file/d/1Nyyey6yIZxnf-XCFTbBEkwGVvA0slPkR/view?usp=drive_link) | Demonstrates order placement, backend processing, database updates, and service execution |

---

# 🎥 AWS Console Implementation Walkthrough

## 🔗 Watch Video

👉 **[Open Console Walkthrough](https://drive.google.com/file/d/1wXQ_m7HRWb7NlWU42HiYe4tv7iYuODj0/view?usp=drive_link)**

---

## Video Overview

This video demonstrates the complete AWS infrastructure implementation of the CloudMart Event-Driven E-Commerce Platform.

### Services Covered

### AWS Lambda

Serverless compute functions used for business logic:

- Order Handler
- Inventory Handler
- Payment Handler
- Notification Handler

### Amazon SNS

Shows:

- SNS Topic Creation
- Event Publishing
- Fan-Out Architecture
- Queue Subscriptions

### Amazon SQS

Demonstrates:

- Inventory Queue
- Payment Queue
- Notification Queue
- Dead Letter Queue (DLQ)

### Amazon DynamoDB

Shows:

- Orders Table
- Inventory Table
- Order Tracking Records
- Stock Management

### Amazon API Gateway

Demonstrates:

- REST API Creation
- Route Configuration
- Backend Integration

### Amazon S3

Shows:

- Static Website Hosting
- Frontend Deployment

### Amazon CloudFront

Demonstrates:

- Content Delivery
- Frontend Distribution

### Amazon CloudWatch

Shows:

- Lambda Monitoring
- Execution Logs
- Troubleshooting Process

---

## Key Learning Outcomes

✅ Event-Driven Architecture

✅ AWS Serverless Services Integration

✅ SNS Fan-Out Design Pattern

✅ Queue-Based Decoupled Processing

✅ DynamoDB Data Persistence

✅ Cloud Monitoring & Logging

---

# 🎥 End-to-End Working Demo

## 🔗 Watch Video

👉 **[Open Working Demo](https://drive.google.com/file/d/1Nyyey6yIZxnf-XCFTbBEkwGVvA0slPkR/view?usp=drive_link)**

---

## Video Overview

This video demonstrates the complete order lifecycle from customer order placement to backend processing.

---

## Demonstrated Workflow

### Step 1 — Customer Places Order

Customer accesses the CloudMart Store hosted on:

- Amazon S3
- Amazon CloudFront

The user:

- Enters customer details
- Selects a product
- Places an order

---

### Step 2 — API Gateway Receives Request

The frontend sends the order request to:

```text
API Gateway
