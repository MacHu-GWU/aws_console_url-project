# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service
from ..utils import encode_arn_in_url


T_IAM_OBJ = T.Union[
    aws_arns.res.IamGroup,
    aws_arns.res.IamUser,
    aws_arns.res.IamRole,
    aws_arns.res.IamPolicy,
]


@dataclasses.dataclass(frozen=True)
class Iam(Service):
    _AWS_SERVICE = "iamv2"

    def _get_iam_obj(self, name_or_arn: str, class_: T.Type[T_IAM_OBJ]) -> T_IAM_OBJ:
        if name_or_arn.startswith("arn:"):
            return class_.from_arn(name_or_arn)
        else:
            return class_.new(
                self._account_id,
                name_or_arn,
            )

    def _get_iam_group_obj(self, name_or_arn: str) -> aws_arns.res.IamGroup:
        return self._get_iam_obj(name_or_arn, aws_arns.res.IamGroup)

    def _get_iam_user_obj(self, name_or_arn: str) -> aws_arns.res.IamUser:
        return self._get_iam_obj(name_or_arn, aws_arns.res.IamUser)

    def _get_iam_role_obj(self, name_or_arn: str) -> aws_arns.res.IamRole:
        return self._get_iam_obj(name_or_arn, aws_arns.res.IamRole)

    def _get_iam_policy_obj(self, name_or_arn: str) -> aws_arns.res.IamPolicy:
        return self._get_iam_obj(name_or_arn, aws_arns.res.IamPolicy)

    # --- arn
    def get_user_group_arn(self, name: str) -> str:
        return self._get_iam_group_obj(name).to_arn()

    def get_user_arn(self, name: str) -> str:
        return self._get_iam_user_obj(name).to_arn()

    def get_role_arn(self, name: str) -> str:
        return self._get_iam_role_obj(name).to_arn()

    def get_policy_arn(self, name: str) -> str:
        return self._get_iam_policy_obj(name).to_arn()

    # --- dashboard
    @property
    def groups(self) -> str:
        return f"{self._service_root}/home?#/groups"

    @property
    def users(self) -> str:
        return f"{self._service_root}/home?#/users"

    @property
    def roles(self) -> str:
        return f"{self._service_root}/home?#/roles"

    @property
    def policies(self) -> str:
        return f"{self._service_root}/home?#/policies"

    def get_user_group(self, name_or_arn: str) -> str:
        obj = self._get_iam_group_obj(name_or_arn)
        return f"{self._service_root}/home#/groups/details/{obj.iam_group_name}?section=users"

    def get_user(self, name_or_arn: str) -> str:
        obj = self._get_iam_user_obj(name_or_arn)
        return f"{self._service_root}/home?#/users/details/{obj.iam_user_name}?section=permissions"

    def get_role(self, name_or_arn: str) -> str:
        obj = self._get_iam_role_obj(name_or_arn)
        return f"{self._service_root}/home#/roles/details/{obj.iam_role_name}?section=permissions"

    def get_policy(self, name_or_arn: str) -> str:
        """
        Examples:

        - AWS Managed Policy: https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2FdAwsManagePolicy?section=permissions
        - User Managed Policy: https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3A111122223333%3Apolicy%2Fservice-role%2Fmy-policy?section=permissions
        """
        obj = self._get_iam_policy_obj(name_or_arn)
        return (
            f"{self._service_root}/home?#/policies/details"
            f"/{encode_arn_in_url(obj.to_arn())}?section=permissions"
        )

    def get_user_inline_policy(self, user_name_or_arn: str, policy_name: str) -> str:
        """
        Example:

        - Role inline Policy: https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users/details/iam-role-name/editPolicy/inline-policy-name?step=addPermissions
        """
        obj = self._get_iam_user_obj(user_name_or_arn)
        return (
            f"{self._service_root}/home?#/users/details"
            f"/{obj.iam_user_name}/editPolicy/{policy_name}?step=addPermissions"
        )

    def get_role_inline_policy(self, role_name_or_arn: str, policy_name: str) -> str:
        """
        Example:

        - Role inline Policy: https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/roles/details/iam-role-name/editPolicy/inline-policy-name?step=addPermissions
        """
        obj = self._get_iam_role_obj(role_name_or_arn)
        return (
            f"{self._root_url}/iamv2/home?#/roles/details"
            f"/{obj.iam_role_name}/editPolicy/{policy_name}?step=addPermissions"
        )
