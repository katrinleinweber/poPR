def get_diff_urls(repo):
    base_url = construct_base_url(repo)
    forks = repo.get_forks()

    # Construct flat list of all comparisons between repo:default & fork:branches
    compare_urls = []
    [compare_urls.extend(get_compare_heads(base_url, fork))
     for fork in forks]

    return compare_urls


def construct_base_url(repo):
    return repo.compare_url \
        .replace('//api.', '//') \
        .replace('.com/repos/', '.com/') \
        .replace('{base}', repo.default_branch)


def get_compare_heads(base_url, fork):
    forker = fork.owner.login
    fork_branches = [fb.name for fb in fork.get_branches()]
    compare_heads = [base_url.format(head=forker + ":" + fb) for fb in
                     fork_branches]

    return compare_heads
