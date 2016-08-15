# -*-  coding: utf-8 -*-
"""
While it's nice to be able to use dots instead of ugly brackets and quotes, it's unacceptably slower.

Each method run 2,000,000 times:

bracket_notation                        : 0.34383  sec
by_getter                               : 0.52543  sec 1.5x slower
dot_notation                            : 2.1887   sec 6.4x slower

"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from ztimer import Timer, K, M

from collections import namedtuple

a_tuple = ('a', 'b', 'c', 'd', 'e')
A_NTuple = namedtuple('ntuple', 'a b c d e')
a_ntuple = A_NTuple(a='a', b='b', c='c', d='d', e='e')
a_dict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}


class Tst(Timer):
    def namedtuple_create(self):
        NTuple = namedtuple('ntuple', 'a b c d e')
        ntuple = NTuple(a='a', b='b', c='c', d='d', e='e')

    def namedtuple_access(self):
        NTuple = namedtuple('ntuple', 'a b c d e')
        ntuple = NTuple(a='a', b='b', c='c', d='d', e='e')
        a_ntuple.b

    def tuple_create(self):
        tuple = ('a', 'b', 'c', 'd', 'e')

    def tuple_access(self):
        a_tuple[1]

    def dict_access(self):
        a_dict['b']

    def dict_create(self):
        dct = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}


Tst(10 * K)
