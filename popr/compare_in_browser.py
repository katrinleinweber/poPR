import webbrowser

from github import Repository


def compare_in_browser(origin: Repository, head: str):
    url = prep_compare_base_url(origin).format(head)
    # Open compare URL in browser
    # learned from https://stackoverflow.com/a/7062272/4341322

    if url != {}:
        webbrowser.get().open(url)


def prep_compare_base_url(repo: Repository) -> str:
    """
    Prepares the URL of GitHub's comparison page.

    :return: The comparison URL with a placeholder for the head label
    """
    return repo.html_url + "/compare/" + repo.default_branch + "...{}"
    # repo als contains compare_url, but that includes
    # "api.", "/repos" and "{base}...{head}"
    # Instead of replace()-ing those (they aren't needed for the browser),
    # we insert {base} here & let compare_in_browser() insert {head},
    # but to avoid a KeyError, we use the simpler placeholder for .format()
