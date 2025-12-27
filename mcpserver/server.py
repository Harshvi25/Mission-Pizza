from openapi_parser import load_openapi_spec
from tool_generator import generate_tools
import backend

def call_tool(tool_name: str, arguments: dict):
    if tool_name == "get_menu":
        return backend.get_menu()
    if tool_name == "post_order":
        return backend.post_order(**arguments)
    if tool_name == "get_order_order_id":
        return backend.track_order(arguments["order_id"])
    raise ValueError("Unknown tool")

def start_server():
    spec = load_openapi_spec("./openapi/pizza.yaml")
    tools = generate_tools(spec)

    print("MCP Server Started")
    print("Available Tools:")
    for tool in tools:
        print(f"- {tool['name']}: {tool['description']}")

    return tools

if __name__ == "__main__":
    start_server()

    print("\n--- Test Calls ---")
    order = call_tool("post_order", {
        "pizza_name": "Margherita",
        "size": "Medium",
        "quantity": 2
    })
    print(order)

    status = call_tool("get_order_order_id", {
        "order_id": order["order_id"]
    })
    print(status)

