# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class EC2(Service):
    _AWS_SERVICE = "ec2"

    # --- arn
    def _get_ec2_obj(
        self,
        id_or_arn: str,
        class_,
    ):
        if id_or_arn.startswith("arn:"):
            return class_.from_arn(id_or_arn)
        else:
            return class_.new(
                self._account_id,
                self._region,
                id_or_arn,
            )

    # --- dashboard
    @property
    def instances(self) -> str:
        return f"{self._service_root}/home?region={self._region}" f"#Instances:"

    @property
    def launch_templates(self) -> str:
        return f"{self._service_root}/home?region={self._region}" f"#LaunchTemplates:"

    @property
    def amis(self) -> str:
        return (
            f"{self._service_root}/home?region={self._region}"
            "#Images:visibility=owned-by-me"
        )

    @property
    def volumes(self) -> str:
        return f"{self._service_root}/home?region={self._region}#Volumes:"

    @property
    def snapshots(self) -> str:
        return f"{self._service_root}/home?region={self._region}#Snapshots:"

    @property
    def eips(self) -> str:
        return f"{self._service_root}/home?region={self._region}#Addresses:"

    @property
    def keys(self) -> str:
        return f"{self._service_root}/home?region={self._region}#KeyPairs:"

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

    def get_instance(
        self,
        instance_id_or_arn: str,
    ) -> str:
        obj = self._get_ec2_obj(instance_id_or_arn, aws_arns.res.Ec2Instance)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#InstanceDetails:instanceId={obj.resource_id}"
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

    def get_ami(
        self,
        image_id_or_arn: str,
    ) -> str:
        if image_id_or_arn.startswith("arn:"):
            obj = aws_arns.res.Ec2Image.from_arn(image_id_or_arn)
        else:
            obj = aws_arns.res.Ec2Image.new(self._region, image_id_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#ImageDetails:imageId={obj.ami_id}"
        )

    def filter_volumes_by_name(self, facets: T.Union[str, T.List[str]]) -> str:
        if isinstance(facets, str):
            facets = [
                facets,
            ]
        search = ",".join([f":{facet}" for facet in facets])
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#Volumes:v=3;search={search}"
        )

    def get_volume(
        self,
        volume_id_or_arn: str,
    ) -> str:
        obj = self._get_ec2_obj(volume_id_or_arn, aws_arns.res.EbsVolume)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#VolumeDetails:volumeId={obj.resource_id}"
        )

    def filter_snapshotss_by_name(self, facets: T.Union[str, T.List[str]]) -> str:
        if isinstance(facets, str):
            facets = [
                facets,
            ]
        search = ",".join([f":{facet}" for facet in facets])
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#Snapshots:visibility=owned-by-me;v=3;search={search}"
        )

    def get_snapshot(
        self,
        snapshot_id_or_arn: str,
    ) -> str:
        obj = self._get_ec2_obj(snapshot_id_or_arn, aws_arns.res.EbsSnapshot)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#SnapshotDetails:snapshotId={obj.resource_id}"
        )

    def filter_eip_by_name(self, facets: T.Union[str, T.List[str]]) -> str:
        if isinstance(facets, str):
            facets = [
                facets,
            ]
        search = ",".join(facets)
        return (
            f"{self._service_root}/home?region={self._region}"
            f"#Addresses:search={search}"
        )

    def get_eip(
        self,
        allocation_id_or_arn: str,
    ) -> str:
        obj = self._get_ec2_obj(allocation_id_or_arn, aws_arns.res.ElasticIpAllocation)
        return (
            f"{self._service_root}/home?region={obj.aws_region}"
            f"#ElasticIpDetails:AllocationId={obj.resource_id}"
        )
