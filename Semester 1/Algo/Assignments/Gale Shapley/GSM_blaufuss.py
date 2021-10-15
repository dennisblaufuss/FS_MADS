from time import perf_counter_ns
import random as rd
import pandas as pd
import matplotlib.pyplot as plt


# quick note: first there is a obejct oriented approach as stated in the assignment
# secondly (commented out) there is more functional oriented approach that doesn't fullfill some of the createria given in the assignment (input critea)
class Person:
    # a Person can be a Proposer as well as Acceptor
    # this has to be defined before the setting of preferences though
    def __init__(self, name):
        self.name = name
        self.preferences = None
        self.partner = None

    def set_pref(self, pref):
        self.preferences = pref

    def get_pref(self):
        return self.preferences[0]

    def get_pref_index(self, person):
        return self.preferences.index(person)

    def proposing(self, acceptor):
        self.partner = acceptor.evaluating(self)

    def evaluating(self, proposer):
        if self.partner is None:
            self.partner = proposer
            return self
        elif self.get_pref_index(proposer) < self.get_pref_index(self.partner):
            self.breaking_up(self.partner)
            self.partner = proposer
            return self
        else:
            proposer.preferences.remove(self)

    def breaking_up(self, ex):
        ex.partner = None
        ex.preferences.remove(self)


def gale_shapley(proposers, acceptors):
    """match making (in this case marrying) with gale shapley algo

    Args:
        proposers (list): list contain objects of class Person, who shall propose
        acceptors (list): list contain objects of class Person, who shall accept
    """
    w = 0
    while w <= len(acceptors):
        # for acceptor in acceptors:
        for proposer in proposers:
            if proposer.partner is None:
                current_preference = proposer.get_pref()
                proposer.proposing(current_preference)
        w += 1


# Testing with example of yt-vid
A = Person("A")
B = Person("B")
C = Person("C")
D = Person("D")
E = Person("E")

L = Person("L")
M = Person("M")
N = Person("N")
O = Person("O")
P = Person("P")

A.set_pref([O, M, N, L, P])
B.set_pref([P, N, M, L, O])
C.set_pref([M, P, L, O, N])
D.set_pref([P, M, O, N, L])
E.set_pref([O, L, M, N, P])

L.set_pref([D, B, E, C, A])
M.set_pref([B, A, D, C, E])
N.set_pref([A, C, E, D, B])
O.set_pref([D, A, C, B, E])
P.set_pref([B, E, A, C, D])

proposers = [A, B, C, D, E]
acceptors = [L, M, N, O, P]

gale_shapley(proposers, acceptors)

print("A married " + A.partner.name)
print("B married " + B.partner.name)
print("C married " + C.partner.name)
print("D married " + D.partner.name)
print("E married " + E.partner.name)
print("L married " + L.partner.name)
print("M married " + M.partner.name)
print("N married " + N.partner.name)
print("O married " + O.partner.name)
print("P married " + P.partner.name)

# creating dataframe for plotting
timespan = []
people = []
n = 15
counter = 0
while counter < 10:
    n *= 2
    people.append(n)
    l = list(range(n))
    list_proposers = l[:n//2]
    list_acceptors = l[n//2:]
    proposers = [Person(i) for i in list_proposers]
    acceptors = [Person(i) for i in list_acceptors]
    for proposer in proposers:
        rd.shuffle(acceptors)
        proposer.set_pref(acceptors)
    for aceptor in acceptors:
        rd.shuffle(proposers)
        aceptor.set_pref(proposers)
    # time measureing
    time_start = perf_counter_ns()
    gale_shapley(proposers, acceptors)
    time_end = perf_counter_ns()
    time_span = (time_end - time_start)/1000000000
    timespan.append(time_span)
    counter += 1
df = pd.DataFrame({"People": people, "Time Span": timespan})

# plotting
plt.figure(figsize=(16, 5))
plt.style.use("ggplot")
plt.plot(df["People"], df["Time Span"],
         marker="o",
         color="red",
         label="Time Span")
plt.xlabel("Number of People")
plt.xlim(xmin=0)
plt.ylabel("Time Span in Seconds")
plt.ylim(ymin=0)
plt.title("Time complexity: Matching with Gale Shapley algorithm")
plt.show()


# The following was my solution in class
# Works totally fine, but the function only takes one input list
# Solution is not optimal
# class Proposer:
#     def __init__(self, name):
#         self.name = name
#         self.preference_list = None
#         self.partner = None
#         self.pref_rn = 0

#     def __str__(self):
#         return self.name

#     def __repr__(self):
#         return self.name

#     def set_preferences(self, pref_l):
#         self.preference_list = pref_l


# class Acceptor:
#     def __init__(self, name):
#         self.name = name
#         self.preference_list = None
#         self.partner = None

#     def __str__(self):
#         return self.name

#     def __repr__(self):
#         return self.name

#     def set_preferences(self, pref_l):
#         self.preference_list = pref_l


# def marriage(proposers):
#     """marries couples with gale shapley algo

#     Args:
#         proposers (list containing objects of class Proposer): marriage is optimized for them
#     """
#     for proposer in proposers:
#         for proposer in proposers:
#             if proposer.partner is None:
#                 m_help(proposer)


# def m_help(proposer):
#     """help function for marrying

#     Args:
#         proposer (obejct of class proposer): guy/girl/whatever who proposes
#     """
#     wish_rn = proposer.preference_list[proposer.pref_rn]
#     if wish_rn.partner is None:
#         proposer.partner = wish_rn
#         wish_rn.partner = proposer
#     elif wish_rn.preference_list.index(proposer) < wish_rn.preference_list.index(wish_rn.partner):
#         proposer.partner = wish_rn
#         wish_rn.partner.partner = None
#         wish_rn.partner = proposer
#     else:
#         proposer.pref_rn += 1
#         m_help(proposer)


# A = Proposer("A")
# B = Proposer("B")
# C = Proposer("C")
# D = Proposer("D")
# E = Proposer("E")

# L = Acceptor("L")
# M = Acceptor("M")
# N = Acceptor("N")
# O = Acceptor("O")
# P = Acceptor("P")

# A.set_preferences([O, M, N, L, P])
# B.set_preferences([P, N, M, L, O])
# C.set_preferences([M, P, L, O, N])
# D.set_preferences([P, M, L, O, N])
# E.set_preferences([O, L, M, N, P])

# L.set_preferences([D, B, E, C, A])
# M.set_preferences([B, A, D, C, E])
# N.set_preferences([A, C, E, D, B])
# O.set_preferences([D, A, C, B, E])
# P.set_preferences([B, E, A, C, D])

# marriage([A, B, C, D, E])


# p_l = []
# for proposer in [A, B, C, D, E]:
#     p_l.append(str(proposer) + " + " + str(proposer.partner))

# a_l = []
# for acceptor in [L, M, N, O, P]:
#     a_l.append(str(acceptor) + " + " + str(acceptor.partner))

# print(a_l)
# print(p_l)
