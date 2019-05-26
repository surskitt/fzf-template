# -*- coding: utf-8 -*-

"""Main module."""

import os
import iterfzf


def conf_keys(conf_dict):
    return conf_dict['values'].keys()


def conf_get_value_dict(conf_dict, k):
    return conf_dict['values'][k]


def apply_template(template, values):
    return template.format(template, **values)


def get_conf_fn(conf_dir, fn):
    fn = os.path.expanduser(fn)
    if not fn.startswith('/'):
        fn = os.path.join(conf_dir, fn)
    return fn
