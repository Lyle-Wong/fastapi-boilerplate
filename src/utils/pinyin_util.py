#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-03-05 19:23:54
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


from pypinyin import lazy_pinyin, Style


def get_full_pinyin(text: str) -> str:
    return ''.join(lazy_pinyin(text))

def get_initial_pinyin(text: str) -> str:
    return ''.join(lazy_pinyin(text, style=Style.FIRST_LETTER))