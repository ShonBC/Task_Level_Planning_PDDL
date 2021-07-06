import subprocess

# root directory of the planner
planner_folder = '/home/luna/Desktop/popf-tif-clp'
# domain file
domain_file = planner_folder + '/bwdomain-exercise.pddl'
# problem file
problem_file = planner_folder + '/bwdomains-exercise.pddl'
# planner binary to execute on domain and problem files
planner = f'{planner_folder}/planner/debug/popf/popf3-clp {domain_file} {problem_file}'

def initialize():
    
    while True:
        
        # Initialize number of parts in bins. Max is 5 of each part
        r_b, b_b, b_s, g_r = [int(x) for x in input('Number of red battery/blue battery/blue sensor/green regulator is bins [0-5]: ').split()]

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
        agv_loc = [int(input(f'Current location of {agv} [ks, as1, as2]: '))]
        station = [int(input('Station to deliver parts [as1, as2]: '))]
        r_k, b_k, b_k, g_k = [int(x) for x in input('Number of red battery/blue battery/blue sensor/green regulator in the kit [0-5]: ')]

if __name__ == '__main__':
    # bash command execution from Python
    planner_cmd = ['bash', '-c', planner]
    process = subprocess.Popen(planner_cmd, stdout=subprocess.PIPE)
    for line in process.stdout:
        # print(line)
        if "b'0" in str(line):
            result = str(line)[str(line).find('(') + 1:str(line).find(')')]
            print(result)
    process.wait()

    print(process.returncode)





with open('rwa2-problem.pddl', 'a') as f:
    f.write('user input to append to file\n')