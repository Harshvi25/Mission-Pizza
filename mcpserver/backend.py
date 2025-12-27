import uuid

ORDERS = {}

def get_menu():
    return {
        "pizzas": [
            {"name": "Margherita", "sizes": ["Small", "Medium", "Large"], "price": 8.99},
            {"name": "Pepperoni", "sizes": ["Medium", "Large"], "price": 10.99}
        ]
    }

def post_order(pizza_name: str, size: str, quantity: int):
    order_id = str(uuid.uuid4())
    ORDERS[order_id] = {
        "pizza_name": pizza_name,
        "size": size,
        "quantity": quantity,
        "status": "Preparing",
        "estimated_time": 20
    }
    return {
        "order_id": order_id,
        "estimated_time": 20
    }

def track_order(order_id: str):
    order = ORDERS.get(order_id)
    if not order:
        return {"order_id": order_id, "status": "Unknown", "estimated_time": 0}

    return {
        "order_id": order_id,
        "status": order["status"],
        "estimated_time": order["estimated_time"]
    }

