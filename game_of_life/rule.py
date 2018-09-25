'''
file: rule.py
date: 2018-09-25
purpose:

'''
# ==============================================================================
# CLASSES
# ==============================================================================
class Rule:
    def __init__(self, rule_tab):
        self.current_state = rule_tab[0]
        self.condition = rule_tab[1]
        self.neighbour_count = rule_tab[2]
        self.next_state = rule_tab[3]

    def match(self, current_state, neigh):
        if self.current_state == current_state:
            if self.condition == '=' and neigh == self.neighbour_count:
                return self.next_state
            elif self.condition == '>' and neigh > self.neighbour_count:
                return self.next_state
            elif self.condition == '<' and neigh < self.neighbour_count:
                return self.next_state
            elif self.condition == '>=' and neigh >= self.neighbour_count:
                return self.next_state
            elif self.condition == '<=' and neigh <= self.neighbour_count:
                return self.next_state
        return None

    def jsonify(self):
        return [
            self.current_state,
            self.condition,
            self.neighbour_count,
            self.next_state
        ]
