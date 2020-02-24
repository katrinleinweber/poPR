import webbrowser


def compare_in_browser(head: str, compare_base: str):
    url = compare_base.format(head)
    # Open compare URL in browser
    # learned from https://stackoverflow.com/a/7062272/4341322

    if url != {}:
        webbrowser.get().open(url)
