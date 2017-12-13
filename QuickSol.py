from operator import itemgetter
from shapely.geometry import *
from shapely.affinity import *

from random import randint, uniform

room = [(0, 0), (10, 0), (10, 10), (0, 10)]
furniture = [[(0, 0), (4, 0), (4, 10), (0, 10), (40, 40.0)], [(0, 0), (4, 0), (4, 10), (0, 10), (40, 40.0)],
        [(0, 0), (6, 0), (0, 10), (30, 30.0)], [(0, 0), (6, 0), (0, 10), (30, 30.0)],
        [(0, 0), (3, 0), (3, 5), (-3, 5), (23, 22.5)], [(0, 0), (3, 0), (3, 5), (-3, 5), (23, 22.5)],
        [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767),
         (21, 21.25502559083609)],
        [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767),
         (21, 21.25502559083609)],
        [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767),
         (21, 21.25502559083609)],
        [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767),
         (21, 21.25502559083609)],
        [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767),
         (21, 21.25502559083609)],
        [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767),
         (21, 21.25502559083609)], [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)],
        [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)],
        [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)],
        [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)],
        [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)],
        [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)],
        [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)],
        [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)],
        [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)],
        [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)],
        [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)],
        [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)],
        [(0, 0), (0, 5), (-3, 5), (8, 7.5)], [(0, 0), (0, 5), (-3, 5), (8, 7.5)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624),
         (6, 6.144791453994818)],
        [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833),
         (5, 5.313756397709023)],
        [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833),
         (5, 5.313756397709023)],
        [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833),
         (5, 5.313756397709023)],
        [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833),
         (5, 5.313756397709023)],
        [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833),
         (5, 5.313756397709023)],
        [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833),
         (5, 5.313756397709023)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)],
        [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)],
        [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)],
        [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)],
        [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)],
        [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)],
        [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)],
        [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)],
        [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)],
        [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)]]

q3 = [(0, 0), (5, 0), (6, 4), (5, 4), (5, 6), (3, 6), (3, 4), (2, 4), (2, 6), (0, 6), (0, 4), (-2, 4)]
q3f = [[(0, 0), (5, 0), (6, 4), (-2, 4), (26, 26.0)], [(0, 0), (5, 0), (6, 4), (-2, 4), (26, 26.0)], [(0, 0), (2.699405197577155, 0), (2.6994051975771556, 2.699405197577155), (0, 2.699405197577155), (7, 7.286788420706561)], [(0, 0), (2.699405197577155, 0), (2.6994051975771556, 2.699405197577155), (0, 2.699405197577155), (7, 7.286788420706561)], [(0, 0), (2.5, 0), (2.5000000000000004, 2.5), (0, 2.5), (6, 6.25)], [(0, 0), (2.5, 0), (2.5000000000000004, 2.5), (0, 2.5), (6, 6.25)], [(0, 0), (2.5, 0), (2.5000000000000004, 2.5), (0, 2.5), (6, 6.25)], [(0, 0), (2.5, 0), (2.5000000000000004, 2.5), (0, 2.5), (6, 6.25)], [(0, 0), (1, 2), (1, 4), (-1, 4), (-1, 2), (6, 6.0)], [(0, 0), (1, 2), (1, 4), (-1, 4), (-1, 2), (6, 6.0)], [(0, 0), (1, 2), (1, 4), (-1, 4), (-1, 2), (6, 6.0)], [(0, 0), (1, 2), (1, 4), (-1, 4), (-1, 2), (6, 6.0)], [(0, 0), (2.23606797749979, 0), (2.23606797749979, 2.23606797749979), (0, 2.23606797749979), (5, 5.000000000000001)], [(0, 0), (2.23606797749979, 0), (2.23606797749979, 2.23606797749979), (0, 2.23606797749979), (5, 5.000000000000001)], [(0, 0), (2.23606797749979, 0), (2.23606797749979, 2.23606797749979), (0, 2.23606797749979), (5, 5.000000000000001)], [(0, 0), (2.23606797749979, 0), (2.23606797749979, 2.23606797749979), (0, 2.23606797749979), (5, 5.000000000000001)], [(0, 0), (2.0615528128088303, 0), (2.0615528128088303, 2.0615528128088303), (0, 2.0615528128088303), (4, 4.25)], [(0, 0), (2.0615528128088303, 0), (2.0615528128088303, 2.0615528128088303), (0, 2.0615528128088303), (4, 4.25)], [(0, 0), (2.0615528128088303, 0), (2.0615528128088303, 2.0615528128088303), (0, 2.0615528128088303), (4, 4.25)], [(0, 0), (2.0615528128088303, 0), (2.0615528128088303, 2.0615528128088303), (0, 2.0615528128088303), (4, 4.25)], [(0, 0), (3, 0), (2, 2), (1, 2), (4, 4.0)], [(0, 0), (3, 0), (2, 2), (1, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.0590169943749475, 0), (1.0590169943749477, 1.0590169943749475), (0, 1.0590169943749475), (1, 1.1215169943749475)], [(0, 0), (1.047213595499958, 0), (1.047213595499958, 1.047213595499958), (0, 1.047213595499958), (1, 1.0966563145999495)], [(0, 0), (1.047213595499958, 0), (1.047213595499958, 1.047213595499958), (0, 1.047213595499958), (1, 1.0966563145999495)], [(0, 0), (1.047213595499958, 0), (1.047213595499958, 1.047213595499958), (0, 1.047213595499958), (1, 1.0966563145999495)], [(0, 0), (1.047213595499958, 0), (1.047213595499958, 1.047213595499958), (0, 1.047213595499958), (1, 1.0966563145999495)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (1, 0), (1, 1), (0, 1), (1, 1.0)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)], [(0, 0), (0.5, 0), (0.5000000000000001, 0.5), (0, 0.5), (1, 0.25)]]


# q5
room = [(0, 0), (0.8676384980996892, 0.014961046014522923), (1.3969052365800665, 0.702636198845332), (1.1892515662914749, 1.5451920423941201), (0.40104493632415167, 1.9081668414616144), (-0.37417898447138936, 1.5182331690134385), (-0.5526607720499913, 0.6690190336004208)]

furniture = [[(0, 0), (-0.7757710192719733, -0.38884408435805773), (-0.38692693491391605, -1.164615103630031), (0.38884408435805806, -0.7757710192719731), (1, 0.7530203962825329)], [(0, 0), (-0.8667842979142654, 0.04129621256007303), (-0.9080805104743385, -0.8254880853541923), (-0.041296212560072695, -0.8667842979142655), (1, 0.7530203962825328)], [(0, 0), (0.3936451744525826, -0.773345894740981), (1.1669910691935637, -0.37970072028839846), (0.7733458947409809, 0.3936451744525829), (1, 0.7530203962825328)], [(0, 0), (0.09912641756737516, 0.8620872053468785), (-0.7629607877795033, 0.9612136229142537), (-0.8620872053468785, 0.09912641756737521), (1, 0.7530203962825328)], [(0, 0), (0.46422748325724916, -0.7331529445287478), (1.197380427785997, -0.2689254612714987), (0.7331529445287478, 0.46422748325724916), (1, 0.7530203962825328)], [(0, 0), (-0.8240814028411737, -0.27186437385920176), (-0.5522170289819719, -1.0959457767003755), (0.2718643738592017, -0.8240814028411737), (1, 0.7530203962825327)], [(0, 0), (0.08763293870708272, 0.8633312599090186), (-0.7756983212019358, 0.9509641986161014), (-0.8633312599090186, 0.08763293870708276), (1, 0.7530203962825327)], [(0, 0), (0.8499053202642943, 0.1751609056524316), (0.6747444146118627, 1.0250662259167258), (-0.17516090565243153, 0.8499053202642943), (1, 0.7530203962825327)], [(0, 0), (0.13546943680848592, 0.8571280114273039), (-0.7216585746188179, 0.9925974482357897), (-0.8571280114273039, 0.13546943680848597), (1, 0.7530203962825326)], [(0, 0), (-0.35323005882826847, 0.7926215501881783), (-1.1458516090164466, 0.4393914913599098), (-0.7926215501881783, -0.3532300588282684), (1, 0.7530203962825326)], [(0, 0), (-0.15596335534773087, 0.8536368244582764), (-1.009600179806007, 0.6976734691105455), (-0.8536368244582764, -0.15596335534773081), (1, 0.7530203962825326)], [(0, 0), (0.8064168409880026, -0.320487558032232), (1.1269043990202345, 0.4859292829557703), (0.3204875580322322, 0.8064168409880026), (1, 0.7530203962825326)], [(0, 0), (-0.7674617055359428, -0.4049974405084488), (-0.3624642650274935, -1.1724591460443918), (0.40499744050844844, -0.767461705535943), (1, 0.7530203962825326)], [(0, 0), (-0.8668293978814872, 0.04033845870817575), (-0.9071678565896628, -0.8264909391733114), (-0.040338458708176185, -0.8668293978814872), (1, 0.7530203962825326)], [(0, 0), (-0.23783406043453104, -0.8345390080635875), (0.5967049476290555, -1.072373068498119), (0.8345390080635875, -0.23783406043453106), (1, 0.7530203962825326)], [(0, 0), (-0.30834329411487216, -0.8111379717760241), (0.5027946776611519, -1.1194812658908964), (0.8111379717760241, -0.3083432941148722), (1, 0.7530203962825326)], [(0, 0), (0.44060597515381156, 0.7475872998796138), (-0.30698132472580214, 1.1881932750334252), (-0.7475872998796137, 0.44060597515381167), (1, 0.7530203962825326)], [(0, 0), (-0.64347929707973, 0.5821982398739362), (-1.225677536953666, -0.061281057205793854), (-0.5821982398739363, -0.64347929707973), (1, 0.7530203962825326)], [(0, 0), (0.5304703068765909, -0.6867471512898967), (1.2172174581664874, -0.1562768444133069), (0.6867471512898968, 0.5304703068765907), (1, 0.7530203962825326)], [(0, 0), (-0.805658653472568, -0.32238878759550765), (-0.4832698658770604, -1.1280474410680754), (0.3223887875955076, -0.805658653472568), (1, 0.7530203962825326)], [(0, 0), (0.6999793503383961, 0.5128833253112931), (0.18709602502710307, 1.212862675649689), (-0.512883325311293, 0.6999793503383962), (1, 0.7530203962825326)], [(0, 0), (0.7672767906930581, -0.40534765664339767), (1.1726244473364558, 0.36192913404966026), (0.40534765664339784, 0.767276790693058), (1, 0.7530203962825326)], [(0, 0), (-0.6801531795226188, -0.5388989224964225), (-0.14125425702619582, -1.2190521020190412), (0.5388989224964221, -0.680153179522619), (1, 0.7530203962825326)], [(0, 0), (-0.7164310549569408, -0.4896396019275989), (-0.22679145302934142, -1.2060706568845398), (0.48963960192759853, -0.7164310549569411), (1, 0.7530203962825324)], [(0, 0), (-0.3393580498993522, 0.27035386632919084), (-0.6097119162285429, -0.06900418357016132), (-0.27035386632919073, -0.33935804989935225), (1, 0.1882550990706332)], [(0, 0), (-0.39713926908291053, 0.1747440986783953), (-0.5718833677613059, -0.2223951704045152), (-0.17474409867839516, -0.3971392690829106), (1, 0.1882550990706332)], [(0, 0), (-0.41125990083302294, 0.13827650934791982), (-0.5495364101809427, -0.2729833914851031), (-0.13827650934791982, -0.41125990083302294), (1, 0.1882550990706332)], [(0, 0), (0.36172339441832757, -0.23960652119906123), (0.6013299156173888, 0.12211687321926648), (0.23960652119906117, 0.3617233944183277), (1, 0.1882550990706332)], [(0, 0), (-0.4318310345880036, 0.042155149593941635), (-0.4739861841819452, -0.3896758849940619), (-0.042155149593941475, -0.43183103458800365), (1, 0.1882550990706332)], [(0, 0), (-0.4146646445455367, 0.12770407837871453), (-0.5423687229242512, -0.2869605661668222), (-0.12770407837871436, -0.41466464454553675), (1, 0.1882550990706332)], [(0, 0), (-0.0791174599116699, -0.42660933722523997), (0.34749187731357, -0.5057267971369098), (0.42660933722523997, -0.07911745991166992), (1, 0.18825509907063318)], [(0, 0), (-0.27238894214141046, 0.33772675829687604), (-0.6101157004382864, 0.06533781615546558), (-0.33772675829687604, -0.27238894214141046), (1, 0.18825509907063318)], [(0, 0), (-0.03825595256904528, 0.4321939161576296), (-0.4704498687266748, 0.3939379635885843), (-0.4321939161576296, -0.038255952569045244), (1, 0.18825509907063318)], [(0, 0), (0.28627753899057645, -0.3260372214029131), (0.6123147603934894, -0.039759682412336635), (0.32603722140291297, 0.2862775389905765), (1, 0.18825509907063315)], [(0, 0), (-0.42551564287959703, -0.08480292881378838), (-0.3407127140658084, -0.5103185716933855), (0.08480292881378818, -0.42551564287959703), (1, 0.18825509907063315)], [(0, 0), (-0.2606224059714267, 0.34688767717562125), (-0.6075100831470479, 0.08626527120419451), (-0.34688767717562125, -0.2606224059714267), (1, 0.18825509907063315)], [(0, 0), (-0.1998357060561464, 0.3851243820581536), (-0.5849600881142999, 0.18528867600200719), (-0.3851243820581536, -0.19983570605614637), (1, 0.18825509907063315)], [(0, 0), (0.43381155110273034, -0.007914366713539102), (0.4417259178162695, 0.4258971843891911), (0.007914366713539215, 0.43381155110273034), (1, 0.18825509907063315)], [(0, 0), (-0.3913590971095896, -0.18733167425771854), (-0.2040274228518711, -0.5786907713673082), (0.18733167425771854, -0.3913590971095896), (1, 0.18825509907063315)]]


# Add shapes to random position
def checkIntersect(room, furniture):
    return room.intersects(furniture)


# Find largest x,y for room
largestx = max(room, key=itemgetter(1))[0]
largesty = max(room, key=itemgetter(1))[1]
room = Polygon(room)
reqArea = room.area * 0.3
print("Room Area: ", reqArea)
currentArea = 0
currentFurniture = []    # Array of polygons already in solution


print("Largest Room: ", largestx, largesty)

# Loop Starts
# Get furniture

for index, itemNormal in enumerate(furniture):
    item = Polygon(itemNormal[:-1])

#item = furniture[0]

    itemAddAttempt = 0

    while itemAddAttempt < 40:
        itemAddAttempt += 1

        # Randomly translate furniture in max room range
        largestFurnx = item.bounds[2]
        largestFurny = item.bounds[3]

        print("Largest: ", largestFurnx, largestFurny)

        translatex = round(uniform(0, largestx),5)
        translatey = round(uniform(0, largesty),5)

        print("Translation: ", translatex, translatey)

        item = translate(item, translatex, translatey)
        print(item)

        # Check furniture fits inside room
        if room.contains(item):

            # Check furniture not inside currentFurniture
            intersect = False
            for furniture in currentFurniture:
                if checkIntersect(furniture, item):
                    intersect = True
                    break

            # Add furniture to currentFurniture
            if intersect == False:
                currentFurniture.append(item)
                currentArea += item.area
                print("Added furniture, Area: ", item.area)
                itemAddAttempt += 1000

    # Check if area over 30%
    if currentArea > reqArea:
        print("Done:\nCurrent Area: ", currentArea, " Required Area: ", reqArea, "Total Shapes: ", len(currentFurniture), "Total Shapes Attempted: ", index)

        currentFurnitureNormal = []

        for i in currentFurniture:
            currentFurnitureNormal.append(list(zip(*i.exterior.coords.xy)))

        print (currentFurnitureNormal)

        for i in currentFurnitureNormal:
            for j in i:
                print("(" + str(j[0]) + ", " + str(j[1]) + ")," , end="")

            print(";", end=" ")

        break





