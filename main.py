from industrial_robot import Industrial
from ground_robot import Ground
from gantry_robot import Gantry

'''
Need to add decorators for attributes that are private/public.

Integrate PDDL to call class methods.

Take user inputs to modify PDDL problem file.

'''

if __name__ == '__main__':

    gnd = Ground('Shon', 2.0, ['s', 'a'], 1.0, 'NIST')
    print(gnd)

    g_robot = Gantry('Shon', 2.0, ['s', 'a'], 1.0, 2.0, 10, 11, 'NIST')
    print(g_robot)

    robot = Industrial('Shon', 2.0, ['s', 'a'], 'NIST')
    print(robot)