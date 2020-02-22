from datetime import datetime as dt
from time import sleep

from github import Github


def wait_for_api(github: Github):
    """
    Be a humble netizen and use only 90% of allowed API calls
    and wait for 10% longer than requested.
    """
    rl = github.get_rate_limit().core
    if rl.remaining == round(rl.limit * 0.1):
        wait_sec = (dt.now() - rl.reset).seconds
        print(
            "Waiting for {} seconds while GitHub is regenerating your API mana ;-)".format(
                wait_sec
            )
        )
        sleep(wait_sec * 1.1)
