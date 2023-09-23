# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    inst_name = "sanhe-infra-dev-jump-box"
    inst_id = "i-0e18f4688442b9c24"

    image_name = "wserver-build-env-with-python-2022-09-06"
    image_id = "ami-081755a1bae54d330"

    vol_id = "vol-036bad5ae240736c2"
    snap_id = "snap-0eab54c73db1931f1"
    eip_id = "eipalloc-0c046c3022bc1d3c8"

    # --- console
    print("-" * 80)
    print(console.ec2.instances)
    print(console.ec2.launch_templates)
    print(console.ec2.amis)
    print(console.ec2.volumes)
    print(console.ec2.snapshots)
    print(console.ec2.eips)
    print(console.ec2.keys)

    print("-" * 80)
    print(console.ec2.filter_instances_by_name(inst_name))
    print(console.ec2.get_instance(inst_id))
    print(console.ec2.filter_amis_by_name(image_name))
    print(console.ec2.get_ami(image_id))
    print(console.ec2.filter_volumes_by_name("vol"))
    print(console.ec2.get_volume(vol_id))
    print(console.ec2.filter_snapshotss_by_name("snap"))
    print(console.ec2.get_snapshot(snap_id))
    print(console.ec2.filter_eip_by_name("eipalloc"))
    print(console.ec2.get_eip(eip_id))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ec2", preview=False)
