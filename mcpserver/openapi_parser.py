import yaml

def load_openapi_spec(path: str) -> dict:
    """
    Load OpenAPI YAML file and return as dictionary
    """
    with open(path, "r") as f:
        spec = yaml.safe_load(f)
    return spec
