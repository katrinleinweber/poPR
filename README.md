# poPR: Find potential Pull Requests

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![CodeScene Code Health](https://codescene.io/projects/7153/status-badges/code-health)](https://codescene.io/projects/7153)

> I believe it is worthwhile trying to discover more about the
> [branch-iverse], even if this only teaches us how little we
> [have merged].
>
> -- liberally quoted from: [Karl Popper's _Conjectures and Refutations: The Growth of Scientific Knowledge_ (1963)](https://en.wikiquote.org/wiki/Karl_Popper#Conjectures_and_Refutations:_The_Growth_of_Scientific_Knowledge_(1963))

This tool helps maintainers observe all forks of a given repository.
It finds branches that could be sent upstream by their authors,
but weren't (for whatever reason).
Thus, _poPR_ helps to review forked code, in order to merge or cherry-pick it.
