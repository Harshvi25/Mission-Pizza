import uuid

DELIVERIES = {}

def schedule_delivery(order_id: str, estimated_time: int):
    delivery_id = str(uuid.uuid4())
    delivery_time = f"In {estimated_time} minutes"

    DELIVERIES[delivery_id] = {
        "order_id": order_id,
        "delivery_time": delivery_time,
        "status": "Scheduled"
    }

    return {
        "delivery_id": delivery_id,
        "order_id": order_id,
        "delivery_time": delivery_time,
        "status": "Scheduled"
    }
