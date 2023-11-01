# -*- coding: utf-8 -*-

import typing as T
import re
import dataclasses
from functools import lru_cache
import aws_arns.api as aws_arns

from ..model import Service


kms_key_pattern = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)


def is_kms_key_id(text: str) -> bool:
    """
    Reference: https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id
    """
    if text.startswith("mrk-"):
        return True
    else:
        return bool(kms_key_pattern.match(text))


@dataclasses.dataclass(frozen=True)
class AWSKMS(Service):
    _AWS_SERVICE = "kms"

    # --- arn
    @lru_cache(maxsize=32)
    def _get_kms_key_id_by_alias(self, alias: str):
        """
        Reference:

        - describe_key: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/client/describe_key.html
        """
        if not alias.startswith("alias/"):
            alias = f"alias/{alias}"
        res = self._bsm.kms_client.describe_key(KeyId=alias)
        return res["KeyMetadata"]["KeyId"]

    def _get_kms_key_object(self, key_id_or_alias_or_arn: str):
        if key_id_or_alias_or_arn.startswith("arn:"):
            return aws_arns.res.KmsKey.from_arn(key_id_or_alias_or_arn)
        elif is_kms_key_id(key_id_or_alias_or_arn):
            return aws_arns.res.KmsKey.new(
                self._account_id,
                self._region,
                key_id_or_alias_or_arn,
            )
        else:
            key_id = self._get_kms_key_id_by_alias(key_id_or_alias_or_arn)
            return aws_arns.res.KmsKey.new(
                self._account_id,
                self._region,
                key_id,
            )

    def get_kms_key_arn(self, key_id_or_alias: str) -> str:
        return self._get_kms_key_object(key_id_or_alias).to_arn()

    # --- dashboard
    @property
    def aws_managed_keys(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/kms/defaultKeys"

    @property
    def customer_managed_keys(self) -> str:
        return f"{self._service_root}/home?region={self._region}#/kms/keys"

    # --- resource
    def _get_key_tab(
        self,
        key_id_or_alias_or_arn: str,
        tab: T.Optional[str] = None,
    ) -> str:
        if tab:
            tab_href = f"/{tab}"
        else:
            tab_href = ""
        obj = self._get_kms_key_object(key_id_or_alias_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#"
            f"/kms/keys/{obj.key_id}{tab_href}"
        )

    def get_key(self, key_id_or_alias_or_arn: str) -> str:
        return self._get_key_tab(key_id_or_alias_or_arn)

    def get_key_policy_tab(self, key_id_or_alias_or_arn: str) -> str:
        return self._get_key_tab(key_id_or_alias_or_arn, "keyPolicy")

    def get_key_crypto_config_tab(self, key_id_or_alias_or_arn: str) -> str:
        return self._get_key_tab(key_id_or_alias_or_arn, "cryptographicConfiguration")

    def get_key_tags_tab(self, key_id_or_alias_or_arn: str) -> str:
        return self._get_key_tab(key_id_or_alias_or_arn, "tags")

    def get_key_key_rotation_tab(self, key_id_or_alias_or_arn: str) -> str:
        return self._get_key_tab(key_id_or_alias_or_arn, "keyRotation")

    def get_key_aliases_tab(self, key_id_or_alias_or_arn: str) -> str:
        return self._get_key_tab(key_id_or_alias_or_arn, "aliases")
