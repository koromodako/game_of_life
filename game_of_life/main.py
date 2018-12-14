#!/usr/bin/env python3
# -!- encoding:utf8 -!-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    file: life.py
#    date: 2017-07-12
#  author: koromodako
# purpose:
#       Un petit jeu de la vie pour délirer
# license:
#       GPLv3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   IMPORT
#-------------------------------------------------------------------------------
from pathlib import Path
from argparse import ArgumentParser
from game_of_life import __banner__
from game_of_life.automaton import Automaton
#===============================================================================
#   FUNCTIONS
#===============================================================================
def parse_args():
    '''[summary]
    '''
    parser = ArgumentParser(description="Runs Conway's Game Of Life on given configuration file.")
    parser.add_argument('--step-by-step', '-s', action='store_true', help="Step-by-step execution.")
    parser.add_argument('--add-grid', '-g', action='store_true', help="Draw a grid.")
    parser.add_argument('--delay', '-d', type=float, default=0.5, help="Delay between two steps.")
    parser.add_argument('config', type=Path, help="Configuration file.")
    return parser.parse_args()
#-------------------------------------------------------------------------------
#   main
#-------------------------------------------------------------------------------
def main():
    print(__banner__)
    args = parse_args()
    lm = Automaton()
    lm.load(args.config)
    lm.run(args.step_by_step,
           args.add_grid,
           args.delay)
#===============================================================================
#   SCRIPT
#===============================================================================
if __name__ == '__main__':
    main()
