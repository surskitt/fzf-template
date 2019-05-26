# -*- coding: utf-8 -*-

"""Main module."""

import os
import sys
import argparse
import yaml

import iterfzf


def input_fn_validator(fn):
    return os.path.expanduser(str(fn))


def parse_args(args):
    desc = 'Template files using yaml config and an fzf selector'
    parser = argparse.ArgumentParser(description=desc)

    config_dir = os.path.expanduser('~/.config/fzf_template')
    template_dir = os.path.expanduser('~/.config/fzf_template/templates')

    parser.add_argument('-i', '--input', type=input_fn_validator,
                        required=True)
    parser.add_argument('-c', '--config_dir', type=str, default=config_dir)
    parser.add_argument('-t', '--template_dir', type=str, default=template_dir)

    return parser.parse_args(args)


def conf_keys(conf_dict):
    return conf_dict['values'].keys()


def conf_get_value_dict(conf_dict, k):
    return conf_dict['values'][k]


def apply_template(template, values):
    return template.format(template, **values)


def get_abs_fn(conf_dir, fn):
    if not fn.startswith('/'):
        fn = os.path.join(conf_dir, fn)
    return fn


def main():
    args = parse_args(sys.argv[1:])

    input_fn = get_abs_fn(args.config_dir, args.input)

    with open(input_fn) as f:
        conf_dict = yaml.load(f.read(), Loader=yaml.SafeLoader)

    keys = conf_keys(conf_dict)
    selected_key = iterfzf.iterfzf(keys)
    if selected_key is None:
        sys.exit(1)
    selected_dict = conf_get_value_dict(conf_dict, selected_key)

    for td in conf_dict['templates']:
        template_fn = get_abs_fn(args.template_dir, td['src'])
        with open(template_fn) as src_f:
            templated = apply_template(src_f.read(), selected_dict)

            dest_fn = os.path.expanduser(td['dest'])
            with open(dest_fn, 'w') as dest_f:
                dest_f.write(templated)
