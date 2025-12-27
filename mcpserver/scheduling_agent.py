from scheduling_mcp_server import schedule_delivery


class SchedulingAgent:
    """
    Phase 3: Scheduling / Coordination Agent
    - Receives order details from Ordering Agent
    - Uses external MCP server to schedule delivery
    """

    def coordinate_delivery(self, order_details: dict):
        order_id = order_details["order_id"]
        estimated_time = order_details["estimated_time"]

        print("\n[SchedulingAgent] Received order details")
        print(order_details)

        delivery = schedule_delivery(order_id, estimated_time)

        print("[SchedulingAgent] Delivery scheduled")
        return delivery
