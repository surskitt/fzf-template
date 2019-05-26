# -*- coding: utf-8 -*-

"""Main module."""

import os
import argparse

import iterfzf


def input_fn_validator(fn):
    return os.path.expanduser(str(fn))


def parse_args(args):
    desc = 'Template files using yaml config and an fzf selector'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('-i', '--input', type=input_fn_validator,
                        required=True)

    return parser.parse_args(args)


def conf_keys(conf_dict):
    return conf_dict['values'].keys()


def conf_get_value_dict(conf_dict, k):
    return conf_dict['values'][k]


def apply_template(template, values):
    return template.format(template, **values)


def get_conf_fn(conf_dir, fn):
    if not fn.startswith('/'):
        fn = os.path.join(conf_dir, fn)
    return fn


def main():
    pass
