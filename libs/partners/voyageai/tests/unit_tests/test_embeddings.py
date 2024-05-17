"""Test embedding model integration."""

from langchain_core.embeddings import Embeddings

from langchain_voyageai import VoyageAIEmbeddings

MODEL = "voyage-2"


def test_initialization_voyage_2() -> None:
    """Test embedding model initialization."""
    emb = VoyageAIEmbeddings(voyage_api_key="NOT_A_VALID_KEY", model=MODEL)
    assert isinstance(emb, Embeddings)
    assert emb.batch_size == 72
    assert emb.model == MODEL
    assert emb._client is not None


def test_initialization_voyage_1() -> None:
    """Test embedding model initialization."""
    emb = VoyageAIEmbeddings(voyage_api_key="NOT_A_VALID_KEY", model="voyage-01")
    assert isinstance(emb, Embeddings)
    assert emb.batch_size == 7
    assert emb.model == "voyage-01"
    assert emb._client is not None


def test_initialization_voyage_1_batch_size() -> None:
    """Test embedding model initialization."""
    emb = VoyageAIEmbeddings(
        voyage_api_key="NOT_A_VALID_KEY", model="voyage-01", batch_size=15
    )
    assert isinstance(emb, Embeddings)
    assert emb.batch_size == 15
    assert emb.model == "voyage-01"
    assert emb._client is not None
