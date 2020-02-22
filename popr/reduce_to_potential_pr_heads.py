def reduce_to_potential_pr_heads(fork_branches: object, pr_branches: object,
                                 repo_branches: object) -> object:
    # TODO: Also remove branches with empty diff
    # TODO: Check head-SHAs against origin:master & skip if found
    remaining = fork_branches \
        .difference(repo_branches) \
        .difference(pr_branches)
    return remaining
