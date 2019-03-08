#! /usr/bin/env python

from __future__ import print_function
import argparse
import json
import os
import os.path
import sys
import jinja2



def run(args):
    """
    Test a Jinja2 template.
    """
    jinja2_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True)
    t = jinja2_env.from_string(args.template.read())
    args.template.close()
    o = json.load(args.json)
    print(t.render(data=o)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test a jinja2 template.")
    parser.add_argument(
        "json",
        action="store",
        type=argparse.FileType("r"),
        help="A datafile in JSON format.")
    parser.add_argument(
        "template",
        action="store",
        type=argparse.FileType("r"),
        help="The Jinja2 template.")
    args = parser.parse_args()
    run(args)
