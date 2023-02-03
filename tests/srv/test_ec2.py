# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    inst_name = "sanhe-infra-dev-jump-box"
    inst_id = "i-0e18f4688442b9c24"

    image_name = "wserver-build-env-with-python-2022-09-06"
    image_id = "ami-081755a1bae54d330"

    # --- resource

    # --- console
    print(console.ec2.instances)
    print(console.ec2.amis)

    print(console.ec2.filter_instances_by_name(inst_name))
    print(console.ec2.get_instance(inst_id))
    print(console.ec2.filter_amis_by_name(image_name))
    print(console.ec2.get_ami(image_id))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ec2", preview=False)
