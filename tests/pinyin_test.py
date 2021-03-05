#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-02-05 15:28:31
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0

import os

from pypinyin import lazy_pinyin, Style

import unittest

class TestPinyin(unittest.TestCase):

    def test_pinpyin(self):
        self.assertEqual(lazy_pinyin('疥疮'), ['jie', 'chuang'])
        pinyin_str = ''.join(lazy_pinyin('疥疮'))
        self.assertEqual(pinyin_str, 'jiechuang')

    def test_pinyin_initial(self):
        pinyin_initial = ''.join(lazy_pinyin('疥疮', style=Style.FIRST_LETTER))
        self.assertEqual(pinyin_initial, 'jc')

    def test_pinyin_with_special(self):
        string = '腹痛（急诊）'
        pinyin_string = ''.join(lazy_pinyin(string, style=Style.FIRST_LETTER))
        self.assertEqual(pinyin_string, 'ft（jz）')
