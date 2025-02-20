import numpy as np
from family_list import reaction_families as fams
from functions import *

fam_path = '/home/kirk/Projects/development/RMG/RMG-database/input/kinetics/families/'
Delta_a = 0.1
Delta_E0 = 15
N_members = 10

fam_lines, E0_list, E0_lines, a_list, a_lines = parse_rules(fam_path,fams) 
make_directories(fams)
check_lengths(E0_list,a_list)
sobol = np.asarray(generate_sobol_set(a_list,E0_list,N_members))
for k in range(N_members):
    n, m = 0, 0
    for fam_num, lines in enumerate(fam_lines):
        new_lines = []
        for num, line in enumerate(lines):
            if n < len(E0_lines) and num == E0_lines[n] and '    E0' in line:
                E0 = E0_list[n]
                perturb = Delta_E0 - 2 * Delta_E0 * sobol[k,2*n]
                new_E0 = E0 + perturb
                newline = '        E0 = ({}, \'kJ/mol\'),\n'.format(str(new_E0))
                new_lines.append(newline)
                n += 1
            elif m < len(a_lines) and num == a_lines[m] and '    alpha' in line:
                a = a_list[m]
                perturb = Delta_a - 2 * Delta_a * sobol[k,2*m+1]
                new_a = a + perturb
                newline = '        alpha = {},\n'.format(str(new_a))
                new_lines.append(newline)
                m += 1
            else:
                new_lines.append(line)
        new_fname = fams[fam_num] +'/rules_{}.py'.format(str(k))
        with open(new_fname,'w') as f:
            f.writelines(new_lines)
        if k == 0:
            old_fname = fams[fam_num] + '/rules.py'
            with open(old_fname,'w') as f:
                f.writelines(lines)

