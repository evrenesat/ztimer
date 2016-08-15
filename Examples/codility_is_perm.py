# -*-  coding: utf-8 -*-
"""
benchmark of alternative solutions for codility is permutation lesson

python2.7

solution_0_set   : 2.26378 sec
solution_1_set   : 0.77648 sec
solution_2_set   : 1.56455 sec

Each method run 100 times:

solution_1_set   : 0.77648 sec
solution_2_set   : 1.56455 sec 2.01x slower
solution_0_set   : 2.26378 sec 2.92x slower

"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from ztimer import Timer, M
A = range(99999)
A.pop(0)

class TST(Timer):
    def solution_0_set(self):
        counter = [0] * len(A)
        limit = len(A)
        for element in A:
            if not 1 <= element <= limit:
                return 0
            else:
                if counter[element - 1] != 0:
                    return 0
                else:
                    counter[element - 1] = 1

        return 1

    def solution_1_set(self):
        ln = len(A)
        if ln == sorted(A)[-1]:
            if ln == len(set(A)):
                return 1
        return 0

    def solution_2_set(self):
        if set(A) == set(range(1, 1 + len(A))):
            return 1
        else:
            return 0

TST(100, hide_unsorted=False)

