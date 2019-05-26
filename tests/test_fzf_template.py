#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `fzf_template` package."""

import pytest
import unittest.mock


from fzf_template import fzf_template


@pytest.fixture
def conf_dict():
    conf_dict = {
        'values': {
            'key1': {
                'a': 'test1',
                'b': 'test2'
            },
            'key2': {
                'a': 'test3',
                'b': 'test4'
            }
        },
        'templates': [
            {
                'src': 'test.conf.template',
                'dest': 'test.conf'
            },
            {
                'src': 'test2.conf.template',
                'dest': 'test2.conf'
            }
        ]
    }

    return conf_dict


def test_conf_keys(conf_dict):
    expected = ['key1', 'key2']
    keys = fzf_template.conf_keys(conf_dict)

    assert list(keys) == expected


def test_conf_get_value_dict(conf_dict):
    expected = {'a': 'test1', 'b': 'test2'}
    values = fzf_template.conf_get_value_dict(conf_dict, 'key1')

    assert values == expected


def test_apply_template():
    expected = 'value1: test1 test2'
    template = 'value1: {a} {b}'
    values = {'a': 'test1', 'b': 'test2'}
    templated = fzf_template.apply_template(template, values)

    assert templated == expected


@pytest.mark.parametrize('fn', ['test.conf',
                                '~/.config/fzf_template/test.conf',
                                '/home/test/.config/fzf_template/test.conf'])
@unittest.mock.patch('fzf_template.fzf_template.os.path.expanduser')
def test_get_conf_fn(mock_os_expanduser, fn):
    mock_os_expanduser.side_effect = lambda x: x.replace('~', '/home/test')

    expected = '/home/test/.config/fzf_template/test.conf'
    conf_fn = fzf_template.get_conf_fn('/home/test/.config/fzf_template', fn)

    assert conf_fn == expected
