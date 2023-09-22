# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class CodeCommit(Service):
    _AWS_SERVICE = "codesuite/codecommit"

    # --- arn
    def get_repo_arn(self, name: str) -> str:
        return aws_arns.res.CodeCommitRepository.new(
            self._account_id,
            self._region,
            name,
        ).to_arn()

    def _get_repo_object(self, name_or_arn: str) -> aws_arns.res.CodeCommitRepository:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.CodeCommitRepository.from_arn(name_or_arn)
        else:
            return aws_arns.res.CodeCommitRepository.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def _repo_arn_to_name(self, arn: str) -> str:
        return aws_arns.res.CodeCommitRepository.from_arn(arn).repo_name

    # --- dashboard
    @property
    def repositories(self) -> str:
        return f"{self._service_root}/repositories?"

    # --- repo
    def get_repo(self, repo_or_arn: str) -> str:
        repo = self._get_repo_object(repo_or_arn)
        return f"{self._service_root}/repositories/{repo.repo_name}/browse?region={repo.aws_region}"

    def get_repo_prs(self, repo_or_arn: str) -> str:
        repo = self._get_repo_object(repo_or_arn)
        return f"{self._service_root}/repositories/{repo.repo_name}/pull-requests?region={repo.aws_region}&status=OPEN"

    def get_repo_commits(self, repo_or_arn: str) -> str:
        repo = self._get_repo_object(repo_or_arn)
        return f"{self._service_root}/repositories/{repo.repo_name}/commits?region={repo.aws_region}"

    def get_repo_branches(self, repo_or_arn: str) -> str:
        repo = self._get_repo_object(repo_or_arn)
        return f"{self._service_root}/repositories/{repo.repo_name}/branches?region={repo.aws_region}"

    def get_repo_tags(self, repo_or_arn: str) -> str:
        repo = self._get_repo_object(repo_or_arn)
        return f"{self._service_root}/repositories/{repo.repo_name}/tags?region={repo.aws_region}"

    def get_repo_settings(self, repo_or_arn: str) -> str:
        repo = self._get_repo_object(repo_or_arn)
        return f"{self._service_root}/repositories/{repo.repo_name}/settings?region={repo.aws_region}"

    def _pr_tab(self, repo_or_arn: str, pr_id: int, tab: str) -> str:
        repo = self._get_repo_object(repo_or_arn)
        return f"{self._service_root}/repositories/{repo.repo_name}/pull-requests/{pr_id}/{tab}?region={repo.aws_region}"

    def get_pr(self, repo_or_arn: str, pr_id: int) -> str:
        return self.get_pr_details(repo_or_arn, pr_id)

    def get_pr_details(self, repo_or_arn: str, pr_id: int) -> str:
        return self._pr_tab(repo_or_arn, pr_id, "details")

    def get_pr_activity(self, repo_or_arn: str, pr_id: int) -> str:
        return self._pr_tab(repo_or_arn, pr_id, "activity")

    def get_pr_changes(self, repo_or_arn: str, pr_id: int) -> str:
        return self._pr_tab(repo_or_arn, pr_id, "changes")

    def get_pr_commits(self, repo_or_arn: str, pr_id: int) -> str:
        return self._pr_tab(repo_or_arn, pr_id, "commits")

    def get_pr_approvals(self, repo_or_arn: str, pr_id: int) -> str:
        return self._pr_tab(repo_or_arn, pr_id, "approvals")

    def get_commit(self, repo_or_arn: str, commit_id: str) -> str:
        repo = self._get_repo_object(repo_or_arn)
        return f"{self._service_root}/repositories/{repo.repo_name}/commit/{commit_id}?region={repo.aws_region}"

    def _get_browse(self, repo_or_arn: str, ref: str) -> str:
        repo = self._get_repo_object(repo_or_arn)
        return f"{self._service_root}/repositories/{repo.repo_name}/browse/{ref}?region={repo.aws_region}"

    def _encode_path(self, path: T.Optional[str] = None) -> str:
        if path is None:
            return ""
        else:
            return f"/--/{path}"

    def get_browse_commit(
        self,
        repo_or_arn: str,
        commit_id: str,
        path: T.Optional[str] = None,
    ) -> str:
        return self._get_browse(repo_or_arn, commit_id + self._encode_path(path))

    def get_browse_tag(
        self,
        repo_or_arn: str,
        tag: str,
        path: T.Optional[str] = None,
    ) -> str:
        return self._get_browse(
            repo_or_arn, f"refs/tags/{tag}" + self._encode_path(path)
        )

    def get_browse_branch(
        self,
        repo_or_arn: str,
        branch: str,
        path: T.Optional[str] = None,
    ) -> str:
        return self._get_browse(
            repo_or_arn, f"refs/heads/{branch}" + self._encode_path(path)
        )
