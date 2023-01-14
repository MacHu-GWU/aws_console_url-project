# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..builder import Builder


@dataclasses.dataclass(frozen=True)
class CodeCommit(Builder):
    _AWS_SERVICE = "codesuite/codecommit"

    @property
    def repositories(self) -> str:
        return f"{self._service_root}/repositories?"

    def get_repo(self, repo: str) -> str:
        return f"{self._service_root}/repositories/{repo}/browse?"

    def get_repo_prs(self, repo: str) -> str:
        return f"{self._service_root}/repositories/{repo}/pull-requests?&status=OPEN"

    def get_repo_commits(self, repo: str) -> str:
        return f"{self._service_root}/repositories/{repo}/commits?"

    def get_repo_branches(self, repo: str) -> str:
        return f"{self._service_root}/repositories/{repo}/branches?"

    def get_repo_tags(self, repo: str) -> str:
        return f"{self._service_root}/repositories/{repo}/tags?"

    def get_repo_settings(self, repo: str) -> str:
        return f"{self._service_root}/repositories/{repo}/settings?"

    def _pr_tab(self, repo: str, pr_id: int, tab: str) -> str:
        return f"{self._service_root}/repositories/{repo}/pull-requests/{pr_id}/{tab}?"

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
        return f"{self._service_root}/repositories/{repo}/commit/{commit_id}?"

    def _get_browse(self, repo: str, ref: str) -> str:
        return f"{self._service_root}/repositories/{repo}/browse/{ref}?"

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
