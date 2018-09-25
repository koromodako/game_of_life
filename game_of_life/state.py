'''
file: state.py
date: 2018-09-25
purpose:

'''
# ==============================================================================
# IMPORTS
# ==============================================================================
from copy import deepcopy
# ==============================================================================
# CLASSES
# ==============================================================================
class State:
    '''[summary]
    '''
    @staticmethod
    def count_neigh(cs, r, c):
        '''[summary]
        '''
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
        '''[summary]
        '''
        ns = State(deepcopy(cs.mat))
        for r in range(cs.rc):
            for c in range(cs.cc):
                bef = cs.mat[r][c]
                neigh = State.count_neigh(cs, r, c)
                for rule in rules:
                    aft = rule.match(bef, neigh)
                    if aft is not None:
                        ns.mat[r][c] = aft
        return ns

    def __init__(self, state_mat):
        '''[summary]
        '''
        self.rc = len(state_mat)
        self.cc = len(state_mat[0])
        self.mat = state_mat

    def jsonify(self):
        '''[summary]
        '''
        return self.mat

    def equal(self, other):
        '''[summary]
        '''
        if other.rc != self.rc:
            return False
        if other.cc != self.cc:
            return False
        for r in range(self.rc):
            for c in range(self.cc):
                if other.mat[r][c] != self.mat[r][c]:
                    return False
        return True

    def stringify(self, add_grid=True):
        '''[summary]
        '''
        text = ''
        for r in range(self.rc):
            if add_grid:
                text += '+' + '-+' * self.cc + '\n|'
            for c in range(self.cc):
                text += '.' if self.mat[r][c] == 0 else 'X'
                if add_grid:
                    text += '|'
            text += '\n'
        if add_grid:
            text += '+' + '-+' * self.cc + '\n\n'
        return text
