def generate_tools(openapi_spec: dict):
    tools = []

    paths = openapi_spec.get("paths", {})

    for path, methods in paths.items():
        for method, details in methods.items():

            tool_name = f"{method}_{path.strip('/').replace('/', '_').replace('{', '').replace('}', '')}"

            tool = {
                "name": tool_name,
                "description": details.get("description", ""),
                "input_schema": extract_input_schema(details),
                "output_schema": extract_output_schema(details)
            }

            tools.append(tool)

    return tools


def extract_input_schema(details: dict):
    if "requestBody" in details:
        return details["requestBody"]["content"]["application/json"]["schema"]
    return {}


def extract_output_schema(details: dict):
    responses = details.get("responses", {})
    for code in responses:
        content = responses[code].get("content")
        if content:
            return content["application/json"]["schema"]
    return {}
