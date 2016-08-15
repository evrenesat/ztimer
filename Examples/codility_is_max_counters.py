# -*-  coding: utf-8 -*-
"""
benchmark of alternative solutions for codility max_counters lesson

python2.7

solution_LC_dict_of_class   : 2.1342 sec
solution_LC_dict_of_dict    : 2.02559 sec
solution_LC_list_of_class   : 1.38945 sec
solution_LC_list_of_dict    : 1.21718 sec
solution_LC_w_dict          : 1.12243 sec
solution_LC_w_list          : 0.61688 sec
solution_w_list             : 0.77215 sec

Each method run 10 times:

solution_LC_w_list          : 0.61688 sec
solution_w_list             : 0.77215 sec 1.25x slower
solution_LC_w_dict          : 1.12243 sec 1.82x slower
solution_LC_list_of_dict    : 1.21718 sec 1.97x slower
solution_LC_list_of_class   : 1.38945 sec 2.25x slower
solution_LC_dict_of_dict    : 2.02559 sec 3.28x slower
solution_LC_dict_of_class   : 2.1342 sec 3.46x slower


"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from random import randint, randrange, shuffle

from ztimer import Timer, M

N = 100000
maxc = 500
A = ([N + maxc] * maxc) + range(N)
shuffle(A)


class TST(Timer):
    def solution_w_list(self):
        result = [0] * N  # The list to be returned
        max_counter = 0  # The used value in previous max_counter command
        current_max = 0  # The current maximum value of any counter

        for command in A:
            if 1 <= command <= N:
                # increase(X) command
                if max_counter > result[command - 1]:
                    # lazy write
                    result[command - 1] = max_counter
                result[command - 1] += 1
                if current_max < result[command - 1]:
                    current_max = result[command - 1]
            else:
                # max_counter command
                # just record the current maximum value for later write
                max_counter = current_max

        for index in range(0, N):
            if result[index] < max_counter:
                # This element has never been used/updated after previous
                #     max_counter command
                result[index] = max_counter

        return result

    def solution_LC_w_list(self):
        result = [0] * N  # The list to be returned
        max_counter = 0  # The used value in previous max_counter command
        current_max = 0  # The current maximum value of any counter

        for command in A:
            if 1 <= command <= N:
                # increase(X) command
                if max_counter > result[command - 1]:
                    # lazy write
                    result[command - 1] = max_counter
                result[command - 1] += 1
                if current_max < result[command - 1]:
                    current_max = result[command - 1]
            else:
                # max_counter command
                # just record the current maximum value for later write
                max_counter = current_max

        return [c if c > max_counter else max_counter for c in result]

    def solution_LC_w_dict(self):
        result = dict((i,0) for i in range(N+1))
        max_counter = 0  # The used value in previous max_counter command
        current_max = 0  # The current maximum value of any counter

        for command in A:
            if 1 <= command <= N:
                # increase(X) command
                if max_counter > result[command - 1]:
                    # lazy write
                    result[command - 1] = max_counter
                result[command - 1] += 1
                if current_max < result[command - 1]:
                    current_max = result[command - 1]
            else:
                # max_counter command
                # just record the current maximum value for later write
                max_counter = current_max

        return [c if c > max_counter else max_counter for c in result]

    def solution_LC_dict_of_class(self):
        # https://codility.com/demo/results/trainingGEMA5F-333/
        Np1 = N + 1

        class Count(object):
            __slots__ = ['counter', 'ver']

            def __init__(self):
                self.counter = 0
                self.ver = 0

        C = dict([(i, Count()) for i in range(Np1)])
        G_current_high = 0
        G_high_ver = 0
        last_applied_high = 0
        for i in A:
            if i >= 1 and i <= N:
                c = C[i]
                if c.ver != G_high_ver:
                    c.ver = G_high_ver
                    c.counter = last_applied_high + 1
                else:
                    c.counter += 1
                if c.counter > G_current_high:
                    G_current_high = c.counter
            elif i == Np1:
                G_high_ver += 1
                last_applied_high = G_current_high
        return [c.counter if c.counter > last_applied_high else last_applied_high for c in
                C.values()[1:]]


    def solution_LC_list_of_class(self):
        # https://codility.com/demo/results/trainingGEMA5F-333/
        Np1 = N + 1

        class Count(object):
            __slots__ = ['counter', 'ver']

            def __init__(self):
                self.counter = 0
                self.ver = 0

        C = [Count() for i in range(Np1)]
        G_current_high = 0
        G_high_ver = 0
        last_applied_high = 0
        for i in A:
            if i >= 1 and i <= N:
                c = C[i]
                if c.ver != G_high_ver:
                    c.ver = G_high_ver
                    c.counter = last_applied_high + 1
                else:
                    c.counter += 1
                if c.counter > G_current_high:
                    G_current_high = c.counter
            elif i == Np1:
                G_high_ver += 1
                last_applied_high = G_current_high
        return [c.counter if c.counter > last_applied_high else last_applied_high for c in C[1:]]

    def solution_LC_dict_of_dict(self):
        Np1 = N + 1

        C = dict([(i, {'counter': 0, 'ver': 0}) for i in range(Np1)])
        G_current_high = 0
        G_high_ver = 0
        last_applied_high = 0
        for i in A:
            if i >= 1 and i <= N:
                c = C[i]
                if c['ver'] != G_high_ver:
                    c['ver'] = G_high_ver
                    c['counter'] = last_applied_high + 1
                else:
                    c['counter'] += 1
                if c['counter'] > G_current_high:
                    G_current_high = c['counter']
            elif i == Np1:
                G_high_ver += 1
                last_applied_high = G_current_high
        return [c['counter'] if c['counter'] > last_applied_high else last_applied_high for c in
                C.values()[1:]]

    def solution_LC_list_of_dict(self):
        Np1 = N + 1

        C = [{'counter': 0, 'ver': 0} for i in range(Np1)]
        G_current_high = 0
        G_high_ver = 0
        last_applied_high = 0
        for i in A:
            if i >= 1 and i <= N:
                c = C[i]
                if c['ver'] != G_high_ver:
                    c['ver'] = G_high_ver
                    c['counter'] = last_applied_high + 1
                else:
                    c['counter'] += 1
                if c['counter'] > G_current_high:
                    G_current_high = c['counter']
            elif i == Np1:
                G_high_ver += 1
                last_applied_high = G_current_high
        return [c['counter'] if c['counter'] > last_applied_high else last_applied_high for c in C[1:]]


TST(10, hide_unsorted=False)
