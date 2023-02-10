#!/usr/bin/python3

import os
import re
import sys


def format_credentials(input):
    for line in input.splitlines():
        if line.strip() == '':
            continue

        if match := re.search(
            r'(?P<host>.+?)\s*=\s*(?P<token>.+)', line.strip()
        ):
            yield f'''credentials "{match['host']}" {{
  token = "{match['token']}"
}}
'''
        else:
            raise ValueError('TERRAFORM_CLOUD_TOKENS environment variable should be "<hostname>=<token>"')

if __name__ == '__main__':
    try:
        for line in format_credentials(os.environ.get('TERRAFORM_CLOUD_TOKENS', '')):
            sys.stdout.write(line)
    except ValueError as e:
        sys.stderr.write(str(e))
        exit(1)
