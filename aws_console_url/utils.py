# -*- coding: utf-8 -*-

encode_mapper = {
    ":": "%3A",
    "/": "%2F",
}


def encode_arn_in_url(arn: str) -> str:
    chars = list(arn)
    return "".join([encode_mapper.get(char, char) for char in chars])
