import os

from flask import Flask, redirect, url_for, render_template
from flask_api import status
from flask_dance.contrib.github import github, make_github_blueprint


app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY")

app.config["GITHUB_OAUTH_CLIENT_ID"] = os.environ.get("GITHUB_OAUTH_CLIENT_ID")
app.config["GITHUB_OAUTH_CLIENT_SECRET"] = os.environ.get("GITHUB_OAUTH_CLIENT_SECRET")

app.register_blueprint(blueprint=make_github_blueprint(scope='public_repo'),
                       url_prefix="/login")

username = os.environ.get("GITHUB_USERNAME")
repo_name = os.environ.get("REPOSITORY_NAME")


def get_link_to_repo(username, repo):
    return f"https://github.com/{username}/{repo}"


@app.route('/')
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))

    user_resp = github.get("/user")
    if not user_resp.ok:
        return "Oops! Something went wrong :( Try to refresh a page!"

    link_to_repo = get_link_to_repo(user_resp.json()["login"], repo_name)

    forking = github.post(f'/repos/{username}/{repo_name}/forks')

    if not forking.ok:
        if forking.status_code == status.HTTP_404_NOT_FOUND:
            return f"You are trying to fork your own repo or the repo does not exist."

        return "Oops! Something went wrong :( Try to refresh a page!"

    return render_template("success.html", link_to_repo=link_to_repo)


if __name__ == '__main__':
    app.run()
