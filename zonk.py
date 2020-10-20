''' Program tests whether Monty Hall problem is real.
link to paradox: https://en.wikipedia.org/wiki/Monty_Hall_problem

Dependency:
    random
    python 3.x.x

How to run:
    python3 zonk.py
'''

import random as r

class gen_obj:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

def gen_gates():
    gates = ['zonk' for x in range(3)]
    gates[r.randint(0,2)] = 'win'
    return gates

def gen_player(change_gate=None):
        if change_gate == None:
            return gen_obj(gate_nr = r.randint(0,2), want_change_gate = bool(r.randint(0,1)))
        else:
            return gen_obj(gate_nr = r.randint(0,2), want_change_gate = bool(change_gate))

def gen_game(gates, player):
    gate = gates[player.gate_nr]
    gates.remove(gate)
    gates.remove('zonk')
    if player.want_change_gate:
        return gates[0]
    else:
        return gate

DEBUG = False
player_change_gate = [ None, True, False ]
wins = None
lose = None
played_games = 10000

print('None means players act randomly and may change gate or not')
print('True means players ALWAYS changes gate')
print('False means players NEVER changes gate\n')

for pcg in player_change_gate:
    wins = 0
    lose = 0
    for e in range(played_games):
        gates = gen_gates()
        player = gen_player(pcg)
        game = gen_game(gates, player)

        if DEBUG:
            print(gates)
            print(player.gate_nr)
            print(player.want_change_gate)
            print("result: %s" % game)

        if game == 'win':
            wins += 1
        else:
            lose += 1
    print(pcg, "/ wins [", 100*wins/played_games, "%], loses [", 100*lose/played_games, "%] ")


