#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics."""
import sys

codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


if __name__ == "__main__":
    count = 0
    file_size = 0
    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                file_size += int(data[-1])
            except Exception:
                pass
            try:
                if int(data[-2]) in codes:
                    codes[int(data[-2])] += 1
            except Exception:
                pass
            if count % 10 == 0:
                print("File size: {}".format(file_size))
                for key, value in sorted(codes.items()):
                    if value != 0:
                        print("{}: {}".format(key, value))
    except KeyboardInterrupt:
        raise
    finally:
        print("File size: {}".format(file_size))
        for key, value in sorted(codes.items()):
            if value != 0:
                print("{}: {}".format(key, value))
