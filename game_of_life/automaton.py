'''
file: automaton.py
date: 2018-09-25
purpose:

'''
# ==============================================================================
# IMPORTS
# ==============================================================================
from time import sleep
from ruamel.yaml import YAML
from game_of_life.rule import Rule
from game_of_life.state import State
# ==============================================================================
# CLASSES
# ==============================================================================
class Automaton:
    '''[summary]
    '''
    def __init__(self):
        '''[summary]
        '''
        self.current_state = None
        self.rules = None

    def _step_forward(self, n=1):
        '''[summary]
        '''
        while n > 0:
            n -= 1
            next_state = State.next_state(self.current_state, self.rules)
            if self.current_state.equal(next_state):
                return False
            self.current_state = next_state
        return True

    def run(self, step_by_step, add_grid, delay):
        '''[summary]
        '''
        if self.current_state is None:
            return

        while True:
            print(self.current_state.stringify(add_grid))

            if not self._step_forward():
                break

            if step_by_step:
                if input('next step? [Y/n]: ') == 'n':
                    break
            else:
                sleep(delay)

    def load(self, fpath):
        yml = YAML(typ='safe')
        conf = yml.load(fpath)
        self.current_state = State(conf['seed'])
        self.rules = [Rule(r) for r in conf['rules']]

    def dump(self, fpath):
        conf = {
            'rules': [r.jsonify() for r in self.rules],
            'seed': self.current_state.jsonify()
        }
        yml = YAML(typ='safe')
        yml.default_flow_style = False
        yml.dump(conf, fpath)
