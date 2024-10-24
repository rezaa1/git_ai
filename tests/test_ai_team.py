import pytest
from src.ai_character import AICharacter
from src.ai_team import AITeam

def test_ai_team_initialization():
    ai1 = AICharacter("AI1", ["Python"], "dummy_key")
    ai2 = AICharacter("AI2", ["JavaScript"], "dummy_key")
    team = AITeam("TestTeam", [ai1, ai2])
    assert team.team_name == "TestTeam"
    assert len(team.characters) == 2

def test_add_remove_character():
    ai1 = AICharacter("AI1", ["Python"], "dummy_key")
    team = AITeam("TestTeam", [ai1])
    ai2 = AICharacter("AI2", ["JavaScript"], "dummy_key")
    team.add_character(ai2)
    assert len(team.characters) == 2
    team.remove_character("AI1")
    assert len(team.characters) == 1
    assert team.characters[0].name == "AI2"

def test_get_team_expertise():
    ai1 = AICharacter("AI1", ["Python", "Data Structures"], "dummy_key")
    ai2 = AICharacter("AI2", ["JavaScript", "Python"], "dummy_key")
    team = AITeam("TestTeam", [ai1, ai2])
    expertise = team.get_team_expertise()
    assert set(expertise) == {"Python", "Data Structures", "JavaScript"}
