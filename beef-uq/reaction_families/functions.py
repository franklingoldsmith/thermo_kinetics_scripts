from torch.quasirandom import SobolEngine
import os

def parse_rules(fam_path,reaction_families):
    fam_lines, E0_list, E0_lines, a_list, a_lines = [], [], [], [], []
    for fam in reaction_families:
        with open(fam_path + fam + '/rules.py','r') as f:
            lines = f.readlines()
        fam_lines.append(lines)
        for num, line in enumerate(lines):
            if line.startswith('        E0'):
                E0 = float(line.split('(')[1].split(',')[0])
                unit = line.split('\'')[1]
                if unit == 'kcal/mol':
                    E0 *= 4.184
                E0_list.append(E0)
                E0_lines.append(num)
            elif line.startswith('        alpha'):
                a_list.append(float(line.split()[2].split(',')[0]))
                a_lines.append(num)
    return fam_lines, E0_list, E0_lines, a_list, a_lines

def generate_sobol_set(a_list,E0_list,N_members):
    dim = len(a_list) + len(E0_list)
    sobol=SobolEngine(dimension=dim,scramble=True,seed = 100)
    x_sobol=sobol.draw(N_members)
    return x_sobol

def check_lengths(list1,list2):
    l1 = len(list1)
    l2 = len(list2)
    if l1 != l2:
        raise Exception('The number of  list entries found between the two lists is not equal')

def make_directories(fams):
    for fam in fams:
        if not os.path.exists(fam):
            os.mkdir(fam)


