# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console, prefix_snake


def test():
    repo = f"{prefix_snake}_test"
    commit_id = console.bsm.codecommit_client.get_branch(
        repositoryName=repo,
        branchName="main",
    )["branch"]["commitId"]
    pr_id = 1

    # --- resource
    codecommit_repo = resource.CodeCommitRepository.from_arn(
        console.codecommit.get_repo_arn(repo)
    )
    assert codecommit_repo.name == repo

    # --- console
    print("-" * 80)
    print(console.codecommit.repositories)

    print("-" * 80)
    print(console.codecommit.get_repo(repo))
    print(console.codecommit.get_repo_prs(repo))
    print(console.codecommit.get_repo_commits(repo))
    print(console.codecommit.get_repo_branches(repo))
    print(console.codecommit.get_repo_tags(repo))
    print(console.codecommit.get_repo_settings(repo))

    print("-" * 80)
    print(console.codecommit.get_pr(repo, pr_id))
    print(console.codecommit.get_pr_details(repo, pr_id))
    print(console.codecommit.get_pr_activity(repo, pr_id))
    print(console.codecommit.get_pr_changes(repo, pr_id))
    print(console.codecommit.get_pr_commits(repo, pr_id))
    print(console.codecommit.get_pr_approvals(repo, pr_id))

    print("-" * 80)
    print(console.codecommit.get_commit(repo, commit_id))
    print(console.codecommit.get_browse_commit(repo, commit_id))
    print(console.codecommit.get_browse_commit(repo, commit_id, "__init__.py"))

    print("-" * 80)
    tag = "0.1.1"
    print(console.codecommit.get_browse_tag(repo, tag))
    print(console.codecommit.get_browse_tag(repo, tag, "__init__.py"))

    print(console.codecommit.get_browse_branch(repo, "main"))
    print(console.codecommit.get_browse_branch(repo, "main"))
    print(console.codecommit.get_browse_branch(repo, "main", "__init__.py"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.codecommit", preview=False)
