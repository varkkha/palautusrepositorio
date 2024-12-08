from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self):
        self._matcher = All()

    def one_of(self, m1, m2):
        self._matcher = Or(m1, m2)
        return self

    def plays_in(self, team):
        self._matcher = And(self._matcher, PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self._matcher = And(self._matcher, HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self._matcher = And(self._matcher, HasFewerThan(value, attr))
        return self

    def build(self):
        matcher = self._matcher
        self._matcher = All()
        return matcher

