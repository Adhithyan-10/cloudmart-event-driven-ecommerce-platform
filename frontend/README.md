# 🎨 CloudMart Frontend

The CloudMart Frontend serves as the customer-facing interface for the Event-Driven E-Commerce Platform. It allows users to browse products, submit orders, and interact with the AWS serverless backend through Amazon API Gateway.

The frontend is intentionally lightweight and fully serverless, making it easy to host on Amazon S3 and distribute globally using Amazon CloudFront.

---

# 📂 Source Files

| File                       | Description                          |
| -------------------------- | ------------------------------------ |
| [index.html](./index.html) | Main user interface                  |
| [style.css](./style.css)   | Application styling and layout       |
| [script.js](./script.js)   | Order submission and API integration |

---

# 🏗 Frontend Architecture

```text
Customer
    ↓
CloudFront
    ↓
Amazon S3
    ↓
Frontend Application
    ↓
API Gateway
    ↓
Order Lambda
```

The frontend acts as the entry point into the CloudMart Event-Driven Architecture.

---

# 📄 index.html

## Purpose

The `index.html` file creates the CloudMart user interface.

It provides:

* Product showcase section
* Order placement form
* Customer information collection
* Product selection
* Order submission functionality

---

## Product Catalog

The frontend displays three sample products:

```text
💻 Laptop
⌨️ Keyboard
🖱️ Mouse
```

Each product is displayed inside a responsive card component.

Example:

```html
<div class="card">
    <h3>💻 Laptop</h3>
    <p>High Performance Device</p>
</div>
```

---

## Order Form

The order form collects:

### Customer Name

```html
<input type="text" id="customer">
```

### Customer Email

```html
<input type="email" id="email">
```

### Product Selection

```html
<select id="product">
```

### Quantity

```html
<input type="number" id="quantity">
```

### Submit Button

```html
<button onclick="placeOrder()">
```

When the button is clicked, the JavaScript function `placeOrder()` is executed.

---

## Result Section

The result container displays:

* Order Success
* Generated Order ID
* Error Messages

```html
<div id="result"></div>
```

---

## File Link

👉 [View index.html](./index.html)

---

# 🎨 style.css

## Purpose

The stylesheet provides a clean and responsive user interface.

The design follows a modern card-based layout commonly used in e-commerce applications.

---

## Global Styling

```css
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}
```

Ensures consistent spacing and layout across all elements.

---

## Container Layout

```css
.container{
    width:90%;
    max-width:1000px;
}
```

Creates a centered layout with responsive sizing.

---

## Product Cards

```css
.card{
    background:white;
    border-radius:10px;
}
```

Each product is displayed using a card component.

Features:

* White background
* Rounded corners
* Shadow effect
* Responsive sizing

---

## Product Grid

```css
.products{
    display:flex;
    gap:20px;
}
```

Displays products horizontally using Flexbox.

---

## Order Form Styling

```css
.order-form{
    background:white;
}
```

The form is visually separated from the product section using:

* Card design
* Box shadow
* Padding
* Rounded corners

---

## Form Controls

```css
input,
select,
button{
    width:100%;
}
```

Provides a clean and consistent user experience.

---

## Result Display

```css
#result{
    font-weight:bold;
}
```

Used to display order status messages.

---

## File Link

👉 [View style.css](./style.css)

---

# ⚙️ script.js

## Purpose

The JavaScript file handles communication between the frontend and the AWS backend.

---

## API Gateway Integration

The frontend communicates with:

```javascript
const API_URL = "https://516yijok0l.execute-api.ap-south-1.amazonaws.com";
```

All order requests are sent to:

```text
POST /order
```

through Amazon API Gateway.

---

## Order Creation

When the user clicks **Place Order**, the application:

1. Reads form values
2. Creates an order object
3. Generates a unique Order ID
4. Sends the request to API Gateway

Example:

```javascript
const order = {
    orderId: "ORD" + Date.now(),
    customer: customer,
    email: email,
    product: product,
    quantity: parseInt(quantity)
};
```

---

## Unique Order ID Generation

Order IDs are generated dynamically:

```javascript
"ORD" + Date.now()
```

Example:

```text
ORD1750253987123
```

This ensures every order has a unique identifier.

---

## API Request

The frontend sends the order using:

```javascript
fetch(API_URL + "/order")
```

Request Type:

```javascript
POST
```

Content Type:

```javascript
application/json
```

---

## Success Handling

If the request succeeds:

```javascript
✅ Order Submitted Successfully
```

is displayed along with the generated Order ID.

Example:

```text
Order ID: ORD1750253987123
```

---

## Error Handling

If the request fails:

```javascript
❌ Order Failed
```

is displayed.

Errors are also logged to the browser console.

---

## File Link

👉 [View script.js](./script.js)

---

# 🔄 End-to-End Order Flow

```text
Customer
    ↓
CloudMart Frontend
    ↓
API Gateway
    ↓
Order Lambda
    ↓
SNS Topic
    ↓
Inventory Queue
Payment Queue
Notification Queue
```

This initiates the event-driven processing workflow within AWS.

---

# ☁️ Hosting Architecture

The frontend is hosted using AWS serverless services.

```text
Amazon S3
      ↓
CloudFront
      ↓
Customer Browser
```

---

## Amazon S3

Stores:

* HTML files
* CSS files
* JavaScript files

Benefits:

* High durability
* Low cost
* Easy deployment

---

## Amazon CloudFront

Provides:

* Global content delivery
* HTTPS support
* Edge caching
* Low latency performance

---

# 🧪 Testing Performed

Frontend testing included:

* Form validation
* Order submission
* API integration testing
* Error handling
* End-to-end workflow testing

---

# 📈 Future Frontend Enhancements

Planned improvements:

* Product catalog page
* Shopping cart
* User authentication
* Payment UI integration
* Real-time order tracking
* WebSocket notifications
* Customer dashboard

---

# 🎯 Learning Outcomes

This frontend demonstrates:

* Static website hosting on AWS
* CloudFront CDN integration
* API Gateway communication
* JavaScript Fetch API
* Event-driven backend integration
* Serverless web application design
* Frontend-to-cloud communication

The frontend serves as the entry point to the CloudMart Event-Driven E-Commerce Platform while remaining lightweight, scalable, and fully serverless.

