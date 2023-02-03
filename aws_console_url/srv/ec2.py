# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Service


@dataclasses.dataclass(frozen=True)
class EC2(Service):
    _AWS_SERVICE = "ec2"

    # --- arn

    # --- dashboard
    @property
    def instances(self) -> str:
        return f"{self._service_root}/home?region={self._region}#Instances:"

    @property
    def amis(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}"
            "#Images:visibility=owned-by-me"
        )

    # --- instance
    def filter_instances_by_name(self, facets: T.Union[str, T.List[str]]) -> str:
        if isinstance(facets, str):
            facets = [
                facets,
            ]
        search = ",".join([f":{facet}" for facet in facets])
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#Instances:search={search};v=3;$case=tags:true%5C,client:false;$regex=tags:false%5C,client:false"
        )

    def get_instance(self, instance_id: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#InstanceDetails:instanceId={instance_id}"
        )

    # --- ami
    def filter_amis_by_name(self, facets: T.Union[str, T.List[str]]) -> str:
        if isinstance(facets, str):
            facets = [
                facets,
            ]
        search = ",".join([f":{facet}" for facet in facets])
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#Images:visibility=owned-by-me;search={search};v=3;$case=tags:false%5C,client:false;$regex=tags:false%5C,client:false"
        )

    def get_ami(self, image_id: str) -> str:
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#ImageDetails:imageId={image_id}"
        )
