from vipr.get_pr_branches import get_pr_branches


def test_get_pr_branches():
    pr_branches = get_pr_branches('katrinleinweber/ViPR-test')
    assert (pr_branches == ['patch'])
