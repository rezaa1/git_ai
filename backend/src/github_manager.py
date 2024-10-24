from github import Github
from typing import List

class GitHubManager:
    def __init__(self, repo_name: str, access_token: str):
        if not access_token:
            raise ValueError("GitHub access token is required")
        self.repo_name = repo_name
        self.github = Github(access_token)
        self.repo = self.github.get_repo(repo_name) if repo_name else None

    def create_branch(self, branch_name: str):
        source_branch = self.repo.get_branch("main")
        self.repo.create_git_ref(f"refs/heads/{branch_name}", source_branch.commit.sha)

    def commit_and_push(self, branch_name: str, file_path: str, content: str, commit_message: str):
        branch = self.repo.get_branch(branch_name)
        current_file = self.repo.get_contents(file_path, ref=branch_name)
        self.repo.update_file(file_path, commit_message, content, current_file.sha, branch=branch_name)

    def create_pull_request(self, branch_name: str, title: str, description: str):
        self.repo.create_pull(title=title, body=description, head=branch_name, base="main")

    def get_file_content(self, file_path: str, branch_name: str = "main") -> str:
        file_content = self.repo.get_contents(file_path, ref=branch_name)
        return file_content.decoded_content.decode()

    def list_branches(self) -> List[str]:
        return [branch.name for branch in self.repo.get_branches()]
