class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Proposer(Person):
    def __init__(self, name):
        super().__init__(name)

    def set_preferences(self, preferences):
        self.preferences = preferences
        self.match = None
        self.proposal_index = 0

    def propose(self):
        if self.match is not None:
            return
        if self.proposal_index >= len(self.preferences):
            raise Exception(f"{self.name} ran out of preferences to propose to")
        self.match = self.preferences[self.proposal_index].receive(self)
        self.proposal_index += 1

    def dump(self):
        self.match = None

    def matched(self):
        return self.match is not None


class Receiver(Person):
    def __init__(self, name):
        super().__init__(name)

    def set_preferences(self, preferences):
        self.preferences = {}
        i = 0
        while i < len(preferences):
            self.preferences[preferences[i].name] = i
            i += 1
        self.match = None

    def receive(self, proposer):
        if proposer.name not in self.preferences:
            raise Exception(f"{proposer.name} does not exist")
        elif self.match is None:
            self.match = proposer
            return self
        elif self.preferences[self.match.name] > self.preferences[proposer.name]:
            self.match.dump()
            self.match = proposer
            return self
        else:
            return None


A = Proposer("A")
B = Proposer("B")
C = Proposer("C")
D = Proposer("D")
E = Proposer("E")

L = Receiver("L")
M = Receiver("M")
N = Receiver("N")
O = Receiver("O")
P = Receiver("P")

A.set_preferences([O, M, N, L, P])
B.set_preferences([P, N, M, L, O])
C.set_preferences([M, P, L, O, N])
D.set_preferences([P, M, O, N, L])
E.set_preferences([O, L, M, N, P])

L.set_preferences([D, B, E, C, A])
M.set_preferences([B, A, D, C, E])
N.set_preferences([A, C, E, D, B])
O.set_preferences([D, A, C, B, E])
P.set_preferences([B, E, A, C, D])

proposers = [A, B, C, D, E]

# proposing untill everyone has a match
while None in [proposer.match for proposer in proposers]:
    for proposer in proposers:
        proposer.propose()

# printing the stuff
for proposer in proposers:
    print(proposer.name, ' + ', proposer.match.name)
