# -*- coding: utf-8 -*-

from aws_console_url.tests import aws


def test():
    repo = "test"
    pr_id = 9

    print(aws.codecommit.repositories)

    print(aws.codecommit.get_repo(repo))
    print(aws.codecommit.get_repo_prs(repo))
    print(aws.codecommit.get_repo_commits(repo))
    print(aws.codecommit.get_repo_branches(repo))
    print(aws.codecommit.get_repo_tags(repo))
    print(aws.codecommit.get_repo_settings(repo))

    print(aws.codecommit.get_pr(repo, pr_id))
    print(aws.codecommit.get_pr_details(repo, pr_id))
    print(aws.codecommit.get_pr_activity(repo, pr_id))
    print(aws.codecommit.get_pr_changes(repo, pr_id))
    print(aws.codecommit.get_pr_commits(repo, pr_id))
    print(aws.codecommit.get_pr_approvals(repo, pr_id))

    commit_id = "24757d14b01e1dab1e8e0813bdfd6c4829e6780f"
    print(aws.codecommit.get_commit(repo, commit_id))
    print(aws.codecommit.get_browse_commit(repo, commit_id))
    print(aws.codecommit.get_browse_commit(repo, commit_id, "data/1.json"))

    tag = "0.1.1"
    print(aws.codecommit.get_browse_tag(repo, tag))
    print(aws.codecommit.get_browse_tag(repo, tag, "data/1.json"))

    print(aws.codecommit.get_browse_branch(repo, "main"))
    print(aws.codecommit.get_browse_branch(repo, "feat/1"))
    print(aws.codecommit.get_browse_branch(repo, "feat/1", "data/1.json"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.codecommit", preview=False)
