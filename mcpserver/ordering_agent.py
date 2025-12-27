from server import call_tool
from scheduling_agent import SchedulingAgent

class PizzaOrderingAgent:
    """
    Phase 2: Pizza Ordering Agent
    - Accepts natural language input
    - Decides which MCP tool to call
    - Returns structured responses
    """

    def handle_user_input(self, user_input: str):
        user_input = user_input.lower()

        if "track" in user_input or "status" in user_input:
            words = user_input.split()
            order_id = words[-1]
            return call_tool("get_order_order_id", {"order_id": order_id})

        if "order" in user_input:
            pizza_name = "margherita" if "margherita" in user_input else "pepperoni"
            size = "medium"
            quantity = 1

            for word in user_input.split():
                if word.isdigit():
                    quantity = int(word)

            if "small" in user_input:
                size = "Small"
            elif "large" in user_input:
                size = "Large"
            else:
                size = "Medium"

            return call_tool(
                "post_order",
                {
                    "pizza_name": pizza_name.capitalize(),
                    "size": size,
                    "quantity": quantity
                }
            )

        if "menu" in user_input or "pizzas" in user_input:
            return call_tool("get_menu", {})

        

        return {"message": "Sorry, I didn’t understand your request."}



if __name__ == "__main__":
    agent = PizzaOrderingAgent()
    scheduler = SchedulingAgent()

    print("\n--- Phase 3: Agent-to-Agent Demo ---")

    menu = agent.handle_user_input("Show me the pizza menu")
    print(menu)

    order = agent.handle_user_input("Order 2 large Margherita pizzas")
    print(order)

    delivery = scheduler.coordinate_delivery(order)
    print(delivery)
