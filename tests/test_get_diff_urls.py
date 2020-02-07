from github import Github

from vipr.get_diff_urls import get_diff_urls


def test_get_diff_url():
    repo: str = 'katrinleinweber/ViPR-test'
    repo_obj = Github().get_repo(repo)
    diff_urls = get_diff_urls(repo=repo_obj)
    compare_base = 'https://github.com/' + repo + '/compare/master...'
    for head in ['ViPR-test-2:dev', 'ViPR-test-2:no-pr', 'ViPR-test-1:patch']:
        assert compare_base + head in diff_urls
