const API_URL = "https://516yijok0l.execute-api.ap-south-1.amazonaws.com";

async function placeOrder(){

    const customer = document.getElementById("customer").value;
    const email = document.getElementById("email").value;
    const product = document.getElementById("product").value;
    const quantity = document.getElementById("quantity").value;

    const order = {
        orderId: "ORD" + Date.now(),
        customer: customer,
        email: email,
        product: product,
        quantity: parseInt(quantity)
    };

    try{

        const response = await fetch(API_URL + "/order", {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(order)
        });

        await response.json();

        document.getElementById("result").innerHTML =
        `
        ✅ Order Submitted Successfully <br><br>
        Order ID: ${order.orderId}
        `;

    }catch(error){

        document.getElementById("result").innerHTML =
        "❌ Order Failed";

        console.error(error);
    }
}
