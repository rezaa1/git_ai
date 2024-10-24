import os
from typing import List, Dict
import openai
from github import Github
from github.Repository import Repository
from github.Branch import Branch
from github.PullRequest import PullRequest

class AICharacter:
    def __init__(self, name: str, expertise: List[str]):
        self.name = name
        self.expertise = expertise

    def generate_code(self, prompt: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are an AI assistant with expertise in {', '.join(self.expertise)}. Generate code based on the given prompt."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating code: {str(e)}")
            return ""

class GitHubManager:
    def __init__(self, repo_name: str):
        self.repo_name = repo_name
        self.github = Github(os.getenv("GITHUB_TOKEN"))
        self.repo: Repository = self.github.get_repo(self.repo_name)

    def create_branch(self, branch_name: str):
        try:
            source = self.repo.get_branch("main")
            self.repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=source.commit.sha)
            print(f"Branch '{branch_name}' created successfully.")
        except Exception as e:
            print(f"Error creating branch: {str(e)}")

    def commit_and_push(self, branch_name: str, file_path: str, content: str, commit_message: str):
        try:
            branch: Branch = self.repo.get_branch(branch_name)
            current_file = self.repo.get_contents(file_path, ref=branch_name)
            self.repo.update_file(file_path, commit_message, content, current_file.sha, branch=branch_name)
            print(f"Changes committed and pushed to '{branch_name}'.")
        except Exception as e:
            print(f"Error committing and pushing changes: {str(e)}")

    def create_pull_request(self, branch_name: str, title: str, description: str):
        try:
            pr: PullRequest = self.repo.create_pull(title=title, body=description, head=branch_name, base="main")
            print(f"Pull request created: {pr.html_url}")
            return pr
        except Exception as e:
            print(f"Error creating pull request: {str(e)}")
            return None

class CodebaseManager:
    def __init__(self, repo_manager: GitHubManager):
        self.repo_manager = repo_manager
        self.codebase: Dict[str, str] = {}

    def update_file(self, file_path: str, content: str):
        self.codebase[file_path] = content
        print(f"File '{file_path}' updated in the codebase.")

    def get_file_content(self, file_path: str) -> str:
        content = self.codebase.get(file_path, "")
        if not content:
            try:
                github_content = self.repo_manager.repo.get_contents(file_path)
                content = github_content.decoded_content.decode('utf-8')
                self.codebase[file_path] = content
            except Exception as e:
                print(f"Error fetching file content: {str(e)}")
        return content

class AITeam:
    def __init__(self, characters: List[AICharacter], github_manager: GitHubManager, codebase_manager: CodebaseManager):
        self.characters = characters
        self.github_manager = github_manager
        self.codebase_manager = codebase_manager

    def develop_software(self, project_description: str):
        for character in self.characters:
            task = self.assign_task(character, project_description)
            code = character.generate_code(task)
            self.implement_code(character.name, code)

    def assign_task(self, character: AICharacter, project_description: str) -> str:
        expertise_str = ", ".join(character.expertise)
        task = f"Given your expertise in {expertise_str}, and based on the following project description: '{project_description}', generate appropriate code to contribute to the project."
        return task

    def implement_code(self, character_name: str, code: str):
        branch_name = f"{character_name.lower().replace(' ', '-')}-implementation"
        self.github_manager.create_branch(branch_name)
        
        file_path = f"{character_name.lower().replace(' ', '_')}_implementation.py"
        self.codebase_manager.update_file(file_path, code)
        self.github_manager.commit_and_push(branch_name, file_path, code, f"Implementation by {character_name}")
        
        pr = self.github_manager.create_pull_request(
            branch_name,
            f"New implementation by {character_name}",
            f"Please review and merge this implementation by {character_name}.\n\nCode:\n```python\n{code}\n```"
        )
        
        if pr:
            print(f"Pull request created for {character_name}'s implementation: {pr.html_url}")

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    github_manager = GitHubManager("your-username/your-repo-name")
    codebase_manager = CodebaseManager(github_manager)

    characters = [
        AICharacter("Design Expert", ["software architecture", "design patterns"]),
        AICharacter("Backend Developer", ["server-side programming", "databases"]),
        AICharacter("Frontend Developer", ["UI/UX", "client-side programming"]),
        AICharacter("DevOps Engineer", ["deployment", "CI/CD", "cloud infrastructure"])
    ]

    ai_team = AITeam(characters, github_manager, codebase_manager)

    project_description = "Create a web application for task management with user authentication, real-time updates, and cloud deployment."
    ai_team.develop_software(project_description)

if __name__ == "__main__":
    main()

