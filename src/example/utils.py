# Load config
import json

def get_config(platform="deepseek"):
    config_path = '../config/llm_config.json'
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Use deepseek as an example, or you can let the user choose
    selected_config = config.get(platform, config.get(next(iter(config))))

    api_key = selected_config.get("api_key")
    base_url = selected_config.get("base_url")
    model = selected_config.get("model")
    return api_key, base_url, model