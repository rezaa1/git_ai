import pytest
from your_module import AICharacter
import os

def test_ai_character_initialization():
    character = AICharacter("Test AI", ["Python", "Testing"], "dummy_api_key")
    assert character.name == "Test AI"
    assert character.expertise == ["Python", "Testing"]

@pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="OpenAI API key not set")
def test_generate_code():
    character = AICharacter("Test AI", ["Python"], os.getenv("OPENAI_API_KEY"))
    code = character.generate_code("Write a Python function to add two numbers")
    assert "def" in code
    assert "return" in code
