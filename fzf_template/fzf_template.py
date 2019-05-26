# -*- coding: utf-8 -*-

"""Main module."""


def conf_keys(conf_dict):
    return conf_dict['values'].keys()


def conf_get_value_dict(conf_dict, k):
    return conf_dict['values'][k]


def apply_template(template, values):
    return template.format(template, **values)
