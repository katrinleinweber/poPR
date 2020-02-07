import click
from github import Github

from vipr.get_diff_urls import get_diff_urls


@click.command()
@click.option("--PAT", default="", help="Personal Access Token of your GitHub account.")
@click.option("--repo", help="NAMESPACE/REPO string of the origin to be analysed")
def open_urls(pat, repo):
    repo_obj = Github(pat).get_repo(repo)
    urls = get_diff_urls(repo=repo_obj)
    [print(url) for url in urls]


if __name__ == '__main__':
    open_urls()
