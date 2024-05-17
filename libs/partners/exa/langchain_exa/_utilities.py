import os
from typing import Dict

from exa_py import Exa  # type: ignore
from langchain_core.utils import convert_to_secret_str


def initialize_client(values: Dict) -> Dict:
    """Initialize the client."""
    exa_api_key = values.get("exa_api_key") or os.environ.get("EXA_API_KEY") or ""
    values["exa_api_key"] = convert_to_secret_str(exa_api_key)
    args = {
        "api_key": values["exa_api_key"].get_secret_value(),
    }
    if values.get("exa_base_url"):
        args["base_url"] = values["exa_base_url"]
    values["client"] = Exa(**args)
    return values
