#!/usr/bin/env python3
# -!- encoding:utf8 -!-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    file: life.py
#    date: 2017-07-12
#  author: paul.dautry
# purpose:
#       Un petit jeu de la vie pour délirer
# license:
#       GPLv3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   IMPORT
#-------------------------------------------------------------------------------
import sys
import json
import copy
import time
#===============================================================================
#   CLASSES
#===============================================================================
#-------------------------------------------------------------------------------
#   LifeRule
#-------------------------------------------------------------------------------
class LifeRule(object):
    def __init__(self, rule_tab):
        super(LifeRule, self).__init__()
        self.bef = rule_tab[0]
        self.cond = rule_tab[1]
        self.neigh = rule_tab[2]
        self.aft = rule_tab[3]

    def match(self, bef, neigh):
        if self.bef == bef:
            if self.cond == '=' and neigh == self.neigh:
                return self.aft
            elif self.cond == '>' and neigh > self.neigh:
                return self.aft
            elif self.cond == '<' and neigh < self.neigh:
                return self.aft
            elif self.cond == '>=' and neigh >= self.neigh:
                return self.aft
            elif self.cond == '<=' and neigh <= self.neigh:
                return self.aft
        return None

    def jsonify(self):
        return [ self.bef, self.cond, self.neigh, self.aft ]
#-------------------------------------------------------------------------------
#   LifeState
#-------------------------------------------------------------------------------
class LifeState(object):
    def __init__(self, state_mat):
        super(LifeState, self).__init__()
        self.rc = len(state_mat)
        self.cc = len(state_mat[0])
        self.mat = state_mat

    def jsonify(self):
        return self.mat

    def equal(self, other):
        if other.rc != self.rc:
            return False
        if other.cc != self.cc:
            return False
        for r in range(self.rc):
            for c in range(self.cc):
                if other.mat[r][c] != self.mat[r][c]:
                    return False
        return True

    def stringify(self):
        text = ''
        for r in range(self.rc):
            text += '+' + '-+' * self.cc + '\n|'
            for c in range(self.cc):
                text += ' ' if self.mat[r][c] == 0 else 'X'
                text += '|'
            text += '\n'
        text += '+' + '-+' * self.cc + '\n\n'
        return text

    @staticmethod
    def count_neigh(cs, r, c):
        count = 0
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue # skip central cell
                lr = r-1+i
                lc = c-1+j
                if lr >= 0 and lr < cs.rc and lc >= 0 and lc < cs.cc:
                    count += cs.mat[lr][lc]
        return count

    @staticmethod
    def next_state(cs, rules):
        ns = LifeState(copy.deepcopy(cs.mat))
        for r in range(cs.rc):
            for c in range(cs.cc):
                bef = cs.mat[r][c]
                neigh = LifeState.count_neigh(cs, r, c)
                for rule in rules:
                    aft = rule.match(bef, neigh)
                    if aft is not None:
                        ns.mat[r][c] = aft
        return ns
#-------------------------------------------------------------------------------
#   LifeMachine
#-------------------------------------------------------------------------------
class LifeMachine(object):
    def __init__(self):
        super(LifeMachine, self).__init__()
        self.rc = 0
        self.cc = 0
        self.state = None
        self.rules = None 

    def step_forward(self, n=1):
        print('stepping forward !')
        while n > 0:
            n -= 1
            print(self.state.stringify())
            state = LifeState.next_state(self.state, self.rules)
            if self.state.equal(state):
                return False
            self.state = state
        return True

    def run(self):
        if self.state is None:
            return
        while True:
            if not step_forward():
                break
            time.sleep(2)

    def from_json(self, fpath):
        with open(fpath, 'r') as f:
            config = json.loads(f.read())
        self.rc = config['row']
        self.cc = config['col']
        self.rules = [ LifeRule(r) for r in config['rules'] ]
        self.state = LifeState(config['seed'])

    def to_json(self, fpath):
        config = {
            'row': self.rc,
            'col': self.cc,
            'rules': [ r.jsonify() for r in self.rules ],
            'seed': self.state.jsonify()
        }
        with open(fpath, 'w') as f:
            f.write(json.dumps(config))
#===============================================================================
#   FUNCTIONS
#===============================================================================
#-------------------------------------------------------------------------------
#   usage
#-------------------------------------------------------------------------------
def usage():
    print("""%s config.json""" % sys.argv[0])
    exit(1)
#-------------------------------------------------------------------------------
#   main
#-------------------------------------------------------------------------------
def main():
    if len(sys.argv) != 2:
        usage()
    lm = LifeMachine()
    lm.from_json(sys.argv[1])
    uin = 'y'
    while uin != 'n':
        lm.step_forward()
        uin = input('next? [y/n]: ')

#===============================================================================
#   SCRIPT
#===============================================================================
if __name__ == '__main__':
    main()