# -*-  coding: utf-8 -*-
"""
Tuple rulez!

Each method run 10,000 times:

tuple_create        : 0.00115 sec
tuple_access        : 0.00155 sec 1.4x slower
class_access        : 0.00157 sec 1.4x slower
dict_access         : 0.00159 sec 1.4x slower
namedtuple_access   : 0.00285 sec 2.5x slower
dict_create         : 0.00314 sec 2.7x slower
class_create        : 0.16286 sec 142.1x slower
namedtuple_create   : 5.40666 sec 4717.5x slower

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


class A_CLASS(object):
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'


aclass = A_CLASS()


class Tst(Timer):
    def namedtuple_create(self):
        NTuple = namedtuple('ntuple', 'a b c d e')
        ntuple = NTuple(a='a', b='b', c='c', d='d', e='e')

    def namedtuple_access(self):
        a_ntuple.b

    def class_create(self):
        class N_CLASS(object): a = 'a'; b = 'b'; c = 'c'; d = 'd'; e = 'e'
        nclass = N_CLASS()

    def class_access(self):
        aclass.a

    def tuple_create(self):
        tuple = ('a', 'b', 'c', 'd', 'e')

    def tuple_access(self):
        a_tuple[1]

    def dict_access(self):
        a_dict['b']

    def dict_create(self):
        dct = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}


Tst(10 * K)
