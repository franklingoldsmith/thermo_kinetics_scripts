import numpy as np
import pandas as pd
import os

Name='adsorptionPt111'
N_members=2


key1 = '    label' 
key2 = 'H298'
labels=[]
H298_lines = []
original_filename="".join((Name,".py"))


with open(original_filename,'r') as f:
    original_lines = f.readlines()

for i, line in enumerate(original_lines):
    if line.startswith(key1) and "\"RX\"" not in line:
        old=line.strip()
        bits=line.split(" = ")
        label = bits[1].replace(",","").replace("\n","").replace('"',"")
        labels.append(label)
    if key2 in line and '#' not in line:
        H298_lines.append(i)

beef_data = np.zeros([N_members,len(labels)])
for i in range(len(labels)):
    filename='beef-ensembles/' + str(labels[i]) + '_bee.txt'
    data=pd.read_csv(filename, sep="\t", header=0)
    beef_data[:,i]=data.iloc[0:N_members,0]

for i in range(N_members):
    new_lines = []
    spec = 0
    for j, line in enumerate(original_lines):
        if j in H298_lines:
            H = float(line.split('(')[1].split(',')[0])
            unit = line.split('\'')[1].split('\'')[0]
            if unit != 'kJ/mol':
                raise Exception("unit for the enthalpy of {} is not in kJ/mol".format(str(labels[spec])))
            perturbation = beef_data[i,spec]
            changed_H=np.round(H+float(perturbation),2)
            spec +=1
            new_str ='        H298=({}, \'kJ/mol\'),\n'.format(str(changed_H))
            new_lines.append(new_str)
        else:
            new_lines.append(original_lines[j])

    newname = Name + '_{}.py'.format(str(i))
    with open(newname,'w') as f:
        f.writelines(new_lines)
