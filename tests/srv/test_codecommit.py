# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console, prefix_snake


def test():
    repo = "test"
    pr_id = 9

    # --- resource
    codecommit_repo = resource.CodeCommitRepository.from_arn(
        resource.CodeCommitRepository.make(
            console.aws_account_id, console.aws_region, repo
        ).arn
    )
    assert codecommit_repo.name == repo

    # --- console
    print(console.codecommit.get_repo_arn(repo))
    print(console.codecommit.repositories)

    print(console.codecommit.get_repo(repo))
    print(console.codecommit.get_repo_prs(repo))
    print(console.codecommit.get_repo_commits(repo))
    print(console.codecommit.get_repo_branches(repo))
    print(console.codecommit.get_repo_tags(repo))
    print(console.codecommit.get_repo_settings(repo))

    print(console.codecommit.get_pr(repo, pr_id))
    print(console.codecommit.get_pr_details(repo, pr_id))
    print(console.codecommit.get_pr_activity(repo, pr_id))
    print(console.codecommit.get_pr_changes(repo, pr_id))
    print(console.codecommit.get_pr_commits(repo, pr_id))
    print(console.codecommit.get_pr_approvals(repo, pr_id))

    commit_id = "24757d14b01e1dab1e8e0813bdfd6c4829e6780f"
    print(console.codecommit.get_commit(repo, commit_id))
    print(console.codecommit.get_browse_commit(repo, commit_id))
    print(console.codecommit.get_browse_commit(repo, commit_id, "data/1.json"))

    tag = "0.1.1"
    print(console.codecommit.get_browse_tag(repo, tag))
    print(console.codecommit.get_browse_tag(repo, tag, "data/1.json"))

    print(console.codecommit.get_browse_branch(repo, "main"))
    print(console.codecommit.get_browse_branch(repo, "feat/1"))
    print(console.codecommit.get_browse_branch(repo, "feat/1", "data/1.json"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.codecommit", preview=False)
