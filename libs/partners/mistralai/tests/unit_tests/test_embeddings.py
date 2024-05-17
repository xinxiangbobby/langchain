import os
from typing import cast

from langchain_core.pydantic_v1 import SecretStr

from langchain_mistralai import MistralAIEmbeddings

os.environ["MISTRAL_API_KEY"] = "foo"


def test_mistral_init() -> None:
    for model in [
        MistralAIEmbeddings(model="mistral-embed", mistral_api_key="test"),
        MistralAIEmbeddings(model="mistral-embed", api_key="test"),
    ]:
        assert model.model == "mistral-embed"
        assert cast(SecretStr, model.mistral_api_key).get_secret_value() == "test"
