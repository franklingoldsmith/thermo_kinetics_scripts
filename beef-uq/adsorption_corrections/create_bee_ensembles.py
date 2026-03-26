import numpy as np
from os import path
import pandas as pd
from tree import RX




def parse_input(species):
    script_dir = '../thermo/beef-ensembles/'
    inputfile = str(script_dir) + str(species) + '_bee.txt'
    fpath = path.abspath(inputfile)
    data = pd.read_csv(fpath, sep="\t", header=0)
    perturbation = data.iloc[:, 1].to_numpy()
    return perturbation

all_children = RX.get_all_children()
for child in all_children:
    species_list = child.get_all_species()
    array_list = []     
    for species in species_list:
        filename = species
        array_list.append(parse_input(filename))

    stacked = np.stack(array_list, axis=0)
    avg = np.mean(stacked, axis=0)

    output_file = 'beef-ensembles/' + str(child) + '_bee.txt'
    column_names = ['averaged_values']
    df = pd.DataFrame(avg, columns=[column_names])
    df.to_csv(output_file, sep="\t", index=False)
