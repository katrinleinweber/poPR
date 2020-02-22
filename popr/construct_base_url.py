def construct_base_url(repo: object) -> str:
    base_url = (
        repo.compare_url.replace("//api.", "//")
        .replace(".com/repos/", ".com/")
        .replace("{base}", repo.default_branch)
    )
    return base_url
