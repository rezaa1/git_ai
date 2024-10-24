from flask import Flask, request, jsonify
from flask_cors import CORS
from src.ai_team import AITeam  # Make sure this import works
from src.github_manager import GitHubManager
import os

app = Flask(__name__)
CORS(app)

github_token = os.getenv("GITHUB_TOKEN")
if not github_token:
    raise ValueError("GITHUB_TOKEN environment variable is not set")

github_manager = GitHubManager("", github_token)
ai_team = AITeam(github_manager)

@app.route('/generate-code', methods=['POST'])
def generate_code():
    data = request.json
    code = ai_team.generate_code(data['prompt'])
    return jsonify({"generated_code": code})

@app.route('/create-repository', methods=['POST'])
def create_repository():
    data = request.json
    repo = github_manager.create_repository(data['repo_name'], data['description'], data['private'])
    return jsonify({"repo_url": repo.html_url})

@app.route('/create-pull-request', methods=['POST'])
def create_pull_request():
    data = request.json
    github_manager.repo_name = data['repo_name']
    github_manager.create_branch(data['branch_name'])
    github_manager.commit_and_push(data['branch_name'], data['file_path'], data['code'], "Add generated code")
    pr = github_manager.create_pull_request(data['branch_name'], data['pr_title'], data['pr_description'])
    return jsonify({"pull_request_url": pr.html_url})

@app.route('/team-expertise', methods=['GET'])
def get_team_expertise():
    return jsonify({"expertise": ai_team.get_team_expertise()})

@app.route('/team_size', methods=['GET'])
def get_team_size():
    size = ai_team.get_team_size()
    return jsonify({"team_size": size})

@app.route('/add_member', methods=['POST'])
def add_team_member():
    data = request.json
    member_name = data.get('name')
    if member_name:
        ai_team.add_member(member_name)
        return jsonify({"message": f"Added {member_name} to the team"}), 201
    else:
        return jsonify({"error": "Member name is required"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
