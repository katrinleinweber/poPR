import webbrowser


def compare_in_browser(to_compare: str, base_url: str):
    url = base_url.format(head=to_compare)
    # Open compare URL in browser
    # learned from https://stackoverflow.com/a/7062272/4341322

    if url != {}:
        webbrowser.get().open(url)
