import pytest
from your_module import GitHubManager
import os

@pytest.mark.skipif(not os.getenv("GITHUB_TOKEN"), reason="GitHub token not set")
def test_github_manager_initialization():
    manager = GitHubManager("your-username/your-repo", os.getenv("GITHUB_TOKEN"))
    assert manager.repo_name == "your-username/your-repo"

@pytest.mark.skipif(not os.getenv("GITHUB_TOKEN"), reason="GitHub token not set")
def test_list_branches():
    manager = GitHubManager("your-username/your-repo", os.getenv("GITHUB_TOKEN"))
    branches = manager.list_branches()
    assert isinstance(branches, list)
    assert "main" in branches
