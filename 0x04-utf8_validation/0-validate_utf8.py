#!/usr/bin/python3
"""This script contains the validUTF8 method."""


def validUTF8(data):
    """Determines if data represents a valid UTF-8 encoding."""
    byte_count = 0

    for byte in data:
        byte = byte & 255
        if byte_count:
            if byte >> 6 != 2:
                return False
            byte_count -= 1
        else:
            if byte >> 7 == 0:
                continue
            while byte & (1 << (7 - byte_count)):
                byte_count += 1
            if byte_count == 1 or byte_count > 4:
                return False
            byte_count = max(byte_count - 1, 0)

    return byte_count == 0
