"""Standard LangChain interface tests"""

from typing import Type

import pytest
from langchain_core.language_models import BaseChatModel
from langchain_standard_tests.integration_tests import ChatModelIntegrationTests

from langchain_mistralai import ChatMistralAI


class TestMistralStandard(ChatModelIntegrationTests):
    @pytest.fixture
    def chat_model_class(self) -> Type[BaseChatModel]:
        return ChatMistralAI

    @pytest.fixture
    def chat_model_params(self) -> dict:
        return {
            "model": "mistral-large-latest",
            "temperature": 0,
        }

    @pytest.mark.xfail(reason="Not implemented.")
    def test_usage_metadata(
        self,
        chat_model_class: Type[BaseChatModel],
        chat_model_params: dict,
    ) -> None:
        super().test_usage_metadata(
            chat_model_class,
            chat_model_params,
        )
