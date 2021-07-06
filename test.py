import industrial_robot

def initialize():
    """Take user input to initialize the environment for planning simulation.
    """

    
    while True:
        
        # Initialize number of parts in bins. Max is 5 of each part
        try:
            r_b, b_b, b_s, g_r = [int(x) for x in input('Number of red battery/blue battery/blue sensor/green regulator is bins [0-5]: ').split()]
        except ValueError:
            print('Not enough values given.')
            continue

        if r_b == 0 and b_b == 0 and b_s == 0 and g_r == 0:
            print('Kit has no parts... exit')
            exit()
        elif 0 < r_b < 5 or 0 < b_b < 5 or 0 < b_s < 5 or 0 < g_r < 5: # exceptions to handle user inputs.
            print('Please enter numbers from 1 to 5.')
            continue

        # If any of the bins do not contain a given part, then don't ask the user where he parts are stored
        if r_b != 0:
            rb_bin = [int(input('Bin for red batteries (1, 2, 3, 4, 5, 6, 7, 8): '))]
        if b_b != 0:
            bb_bin = [int(input('Bin for blue batteries (1, 3, 4, 5, 6, 7, 8): '))]
        if  b_s != 0:
            bs_bin = [int(input('Bin for  blue sensors (3, 4, 5, 6, 7, 8): '))]
        if g_r != 0:
            gr_bin = [int(input('Bin for green regulators (3, 4, 5, 6, 7): '))]

        # Automated Guided Vehicles (agv), Kit Station (ks), Assembly Station 1/2 (as1, as2)
        agv = [int(input('AVG to use for kitting [1-4]: '))]
        agv_loc = [input(f'Current location of agv{agv} [ks, as1, as2]: ')]
        station = [input('Station to deliver parts [as1, as2]: ')]
        r_k, b_k, b_k, g_k = [int(x) for x in input('Number of red battery/blue battery/blue sensor/green regulator in the kit [0-5]: ')]


# initialize()
robot = industrial_robot.indusrial_robot('Shon', 1.2, ['s', 'a'])
robot.pick_up('red battery', 'bin 1')