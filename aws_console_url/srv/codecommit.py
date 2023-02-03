# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Resource, Service


@dataclasses.dataclass(frozen=True)
class CodeCommitRepository(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(
        cls, aws_account_id: str, aws_region: str, name: str
    ) -> "CodeCommitRepository":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:codecommit:{self.aws_region}:{self.aws_account_id}:{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "CodeCommitRepository":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[5]
        return cls.make(aws_account_id, aws_region, name)


@dataclasses.dataclass(frozen=True)
class CodeCommit(Service):
    _AWS_SERVICE = "codesuite/codecommit"

    # --- arn
    def get_repo_arn(self, name: str) -> str:
        return CodeCommitRepository(self._account_id, self._region, name).arn

    # --- dashboard
    @property
    def repositories(self) -> str:
        return f"{self._service_root}/repositories?"

    # --- repo
    def get_repo(self, repo: str) -> str:
        return f"{self._service_root}/repositories/{repo}/browse?region={self._region}"

    def get_repo_prs(self, repo: str) -> str:
        return f"{self._service_root}/repositories/{repo}/pull-requests?region={self._region}&status=OPEN"

    def get_repo_commits(self, repo: str) -> str:
        return f"{self._service_root}/repositories/{repo}/commits?region={self._region}"

    def get_repo_branches(self, repo: str) -> str:
        return (
            f"{self._service_root}/repositories/{repo}/branches?region={self._region}"
        )

    def get_repo_tags(self, repo: str) -> str:
        return f"{self._service_root}/repositories/{repo}/tags?region={self._region}"

    def get_repo_settings(self, repo: str) -> str:
        return (
            f"{self._service_root}/repositories/{repo}/settings?region={self._region}"
        )

    def _pr_tab(self, repo: str, pr_id: int, tab: str) -> str:
        return f"{self._service_root}/repositories/{repo}/pull-requests/{pr_id}/{tab}?region={self._region}"

    def get_pr(self, repo: str, pr_id: int) -> str:
        return self.get_pr_details(repo, pr_id)

    def get_pr_details(self, repo: str, pr_id: int) -> str:
        return self._pr_tab(repo, pr_id, "details")

    def get_pr_activity(self, repo: str, pr_id: int) -> str:
        return self._pr_tab(repo, pr_id, "activity")

    def get_pr_changes(self, repo: str, pr_id: int) -> str:
        return self._pr_tab(repo, pr_id, "changes")

    def get_pr_commits(self, repo: str, pr_id: int) -> str:
        return self._pr_tab(repo, pr_id, "commits")

    def get_pr_approvals(self, repo: str, pr_id: int) -> str:
        return self._pr_tab(repo, pr_id, "approvals")

    def get_commit(self, repo: str, commit_id: str) -> str:
        return f"{self._service_root}/repositories/{repo}/commit/{commit_id}?region={self._region}"

    def _get_browse(self, repo: str, ref: str) -> str:
        return f"{self._service_root}/repositories/{repo}/browse/{ref}?region={self._region}"

    def _encode_path(self, path: T.Optional[str] = None) -> str:
        if path is None:
            return ""
        else:
            return f"/--/{path}"

    def get_browse_commit(
        self,
        repo: str,
        commit_id: str,
        path: T.Optional[str] = None,
    ) -> str:
        return self._get_browse(repo, commit_id + self._encode_path(path))

    def get_browse_tag(
        self,
        repo: str,
        tag: str,
        path: T.Optional[str] = None,
    ) -> str:
        return self._get_browse(repo, f"refs/tags/{tag}" + self._encode_path(path))

    def get_browse_branch(
        self,
        repo: str,
        branch: str,
        path: T.Optional[str] = None,
    ) -> str:
        return self._get_browse(repo, f"refs/heads/{branch}" + self._encode_path(path))
