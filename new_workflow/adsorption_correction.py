from adsorbate import Adsorbate
from gas import Gas
import numpy as np
import scipy
from treelib import Tree
import copy
import textwrap


class Group:

    def __init__(self,
                 group_name,
                 adsorbate_list,
                 gas_list,
                 slab_dict,
                 connectivity_string,
                 group_long_description=' ',
                 group_short_description=None,
                 ):

        self.group_name = group_name
        self.slab_dict = slab_dict
        self.connectivity_string = connectivity_string

        self.adsorbate_list = adsorbate_list
        self.gas_list = gas_list

        self.group_long_description = group_long_description
        self.avg_list = [ads.adsorbate_name for ads in self.adsorbate_list]
        if group_short_description is None:
            self.group_short_description = 'Averaged from: '\
                + str(self.avg_list)
        else:
            self.group_short_description = group_short_description
        return

    def get_group_correction(self):
        dH_list, dS_list = [], []
        dcP_array = np.zeros([7, len(self.adsorbate_list)])
        for i, ads in enumerate(self.adsorbate_list):
            Qa, Sa, Ha, cPa = ads.get_thermo()
            gas = self.gas_list[i]
            Qg, Sg, Hg, cPg = gas.get_thermo()
            dH_list.append(float(Ha[0] - Hg[0]))
            if np.abs(dH_list[-1]) > 1000:
                print(ads.adsorbate_name,
                      " has an adsorption correction over",
                      "1000 kJ/mol")
            dS_list.append(1e3*(Sa[0] - Sg[0]))
            temps = gas.temperatures
            desired_temps = [300, 400, 500, 600, 800, 1000, 1500]
            count = 0
            for j, T in enumerate(temps):
                if T in desired_temps:
                    ctmp = np.round(1e3*(float(cPa[j] - cPg[j])), 3)
                    dcP_array[count, i] = ctmp
                    count += 1
        if not dH_list:
            print('There is no data for the group: ', self.group_name)
        dH = np.round(np.mean(dH_list), 3)
        dS = np.round(np.mean(dS_list), 3)
        dcP = np.round(np.mean(dcP_array, axis=1), 3)
        return dH, dS, dcP

    def get_RMG_group_entry(self, idx=0):
        dH, dS, dcP = self.get_group_correction()
        str_dcP = '{}'.format(", ".join(map(str, dcP)))
        str_T = '300, 400, 500, 600, 800, 1000, 1500'
        shortdesc = self.group_short_description
        longdesc = self.group_long_description
        lines = 'entry(\n'
        lines += '    index = {},\n'.format(str(idx))
        lines += '    label = \"{}\",\n'.format(str(self.group_name))
        lines += '    group=\n'
        lines += '\"\"\"'
        lines += self.connectivity_string
        lines += '\"\"\",\n'
        lines += '    thermo=ThermoData(\n'
        lines += '        Tdata=([' + str_T + '], \'K\'),\n'
        lines += '        Cpdata=([' + str_dcP + '], \'J/(mol*K)\'),\n'
        lines += '        H298=({}, \'kJ/mol\'),\n'.format(str(dH))
        lines += '        S298=({}, \'J/(mol*K)\'),\n'.format(str(dS))
        lines += '    ),\n'
        lines += 'shortDesc=u\"\"\"{}\"\"\",\n'.format(textwrap.fill(shortdesc, 80))
        lines += 'longDesc=u\"\"\"{}\n'.format(textwrap.fill(longdesc, 80))
        lines += '\"\"\",\n'
        lines += '    metal = \"{}\",\n'.format(self.slab_dict['metal'])
        lines += '    facet = \"{}\",\n'.format(self.slab_dict['facet'])
        lines += ')\n\n'
        return lines


class AdsorptionCorrectionTree:

    def __init__(self,
                 tree_dict,
                 group_lib,
                 adsorbate_lib=None,
                 gas_lib=None,
                 reference_dict=None,
                 slab_dict=None,
                 group_long_description=' ',
                 group_short_description=None,
                 P_ref=1.0E5,  # Pa
                 NASA7_T_switch=1000.0,  # K
                 twoD_gas_cutoff_frequency=100.0,
                 ):
        self.tree_dict = tree_dict
        self.group_lib = group_lib
        self.adsorbate_lib = adsorbate_lib
        self.gas_lib = gas_lib
        self.slab_dict = slab_dict
        self.reference_dict = reference_dict
        self.P_ref = P_ref
        self.NASA_T_switch = NASA7_T_switch
        self.twoD_cutoff_frequency = twoD_gas_cutoff_frequency
        self.group_long_description = group_long_description
        self.group_short_description = group_short_description
        self._construct_tree()
        self._assign_group_data()
        self._load_Ads_and_Gas()
        self._add_Group_object_as_data()
        self._get_tree_str()
        return

    def _construct_tree(self):
        self.tree = Tree()
        self.tree.create_node("RX", "RX")
        self._dict_to_tree(self.tree, "RX", self.tree_dict)

    def _dict_to_tree(self, tree, parent, dictionary):
        for key, value in dictionary.items():
            tree.create_node(key, key, parent=parent)
            if isinstance(value, dict):
                self._dict_to_tree(tree, key, value)
            else:
                tree.create_node(value, f"{key}_{value}", parent=key)

    def _assign_group_data(self):
        for node_id in self.tree.expand_tree():
            group_data = self.group_lib[node_id]
            self.tree[node_id].data = group_data
            pass

    def _load_Ads_and_Gas(self):
        self.adsorbate_list = []
        cutoff = self.twoD_cutoff_frequency
        for ads_dict in self.adsorbate_lib:
            ads = Adsorbate(ads_dict,
                            self.reference_dict,
                            self.slab_dict,
                            P_ref=self.P_ref,
                            NASA7_T_switch=self.NASA_T_switch,
                            twoD_gas_cutoff_frequency=cutoff)
            self.adsorbate_list.append(ads)
        self.gas_list = []
        for gas_dict in self.gas_lib:
            gas = Gas(gas_dict, self.reference_dict,
                      P_ref=self.P_ref,
                      NASA7_T_switch=self.NASA_T_switch)
            self.gas_list.append(gas)

    def _add_Group_object_as_data(self):
        for node_id in self.tree.expand_tree():
            adsorbate_names = self.tree[node_id].data['adsorbates']
            gas_names = self.tree[node_id].data['gas_precursors']
            con_str = self.tree[node_id].data['connectivity_string']
            subtree = self.tree.subtree(node_id)
            for subnode_id in subtree.expand_tree():
                if subnode_id == node_id:  # skip self
                    continue
                tmpgasnames = subtree[subnode_id].data['gas_precursors']
                tmpadsnames = subtree[subnode_id].data['adsorbates']
                gas_names.extend(tmpgasnames)
                adsorbate_names.extend(tmpadsnames)

            adsorbate_list = []
            for name in adsorbate_names:
                for ads in self.adsorbate_list:
                    if ads.adsorbate_name == name:
                        adsorbate_list.append(ads)
            gas_list = []
            for name in gas_names:
                for gas in self.gas_list:
                    if gas.gas_name == name:
                        gas_list.append(gas)

            self._check_data_passed_to_group(gas_names,
                                             gas_list,
                                             adsorbate_names,
                                             adsorbate_list,
                                             node_id)
            longdesc = self.group_long_description
            shortdesc = self.group_short_description
            group = Group(group_name=node_id,
                          adsorbate_list=adsorbate_list,
                          gas_list=gas_list,
                          slab_dict=self.slab_dict,
                          connectivity_string=con_str,
                          group_long_description=longdesc,
                          group_short_description=shortdesc,
                          )
            self.tree[node_id].data['Group'] = group
        return

    def _check_data_passed_to_group(self,
                                    gas_names,
                                    gas_list,
                                    adsorbate_names,
                                    adsorbate_list,
                                    node_id):
        try:
            assert len(adsorbate_names) == len(adsorbate_list)
        except AssertionError:
            print("ads ERROR")
            print(node_id)
            print(len(adsorbate_names), len(adsorbate_list))
            print(adsorbate_names)
        try:
            assert len(gas_names) == len(gas_list)
        except AssertionError:
            print("gas ERROR")
        try:
            assert len(gas_list) == len(adsorbate_list)
        except AssertionError:
            print('adslist and gaslist not equal')
            print(len(gas_list), len(adsorbate_list))

    def get_first_entry(self):
        lines = []
        lines += 'entry(\n'
        lines += '    index = 1,\n'
        lines += '    label = "RX",\n'
        lines += '    group=\n'
        lines += '\"\"\"\n'
        lines += '1 R  ux\n'
        lines += '2 * X ux\n'
        lines += '\"\"\",\n'
        lines += '    thermo=None,\n'
        lines += '    shortDesc=u"""Anything adsorbed anyhow.\"\"\",\n'
        lines += '    longDesc=u\"\"\"\n'
        lines += '\"\"\",\n'
        lines += '    metal = \"{}\",\n'.format(self.slab_dict['metal'])
        lines += '    facet = \"{}\",\n'.format(self.slab_dict['facet'])
        lines += ')\n\n'
        return lines

    def write_RMG_adsorption_correction_file(self,
                                             filename,
                                             file_title=' ',
                                             file_long_description=' ',
                                             file_short_description=' ',
                                             ):
        shortdesc = file_short_description
        longdesc = file_long_description
        lines = []
        lines += '#!/usr/bin/env python\n# encoding: utf-8\n'
        lines += 'name = \"{}\"\n'.format(str(file_title))
        lines += 'shortDesc = u"""{}\n"""\n'.format(textwrap.fill(shortdesc, 80))
        lines += 'longDesc = u"""\n'
        lines += '{}\n'.format(str(longdesc))
        lines += '"""\n'
        entry1 = self.get_first_entry()
        lines.extend(entry1)
        for i, node_id in enumerate(self.tree.expand_tree()):
            if node_id != 'RX':
                tmpgroup = self.tree[node_id].data['Group']
                entry_str = tmpgroup.get_RMG_group_entry(idx=i+1)
                lines.extend(entry_str)
        tree_str = self._get_tree_str()
        lines.extend(tree_str)
        with open(filename, 'w') as f:
            f.writelines(lines)

    def _get_tree_str(self):
        lines = ''
        lines += 'tree(\n'
        lines += '\"\"\"\n'
        for node_id in self.tree.expand_tree():
            level = self.tree.level(node_id)
            spaces = ''.join([' ' for _ in range(4 * level)])
            level_str = 'L{}: '.format(str(level+1))
            group_str = self.tree[node_id].tag
            lines += spaces + level_str + group_str + '\n'
        lines += '\"\"\",\n'
        lines += ')\n'
        return lines


class AdsorptionCorrectionTreeEnsemble(AdsorptionCorrectionTree):
    def __init__(self,
                 tree_dict,
                 group_lib,
                 adsorbate_lib=None,
                 gas_lib=None,
                 reference_dict=None,
                 slab_dict=None,
                 ensemble_energies_array=None,
                 reference_ensemble=None,
                 ensemble_scale=0.683,
                 group_long_description=' ',
                 group_short_description=' ',
                 P_ref=100000,
                 NASA7_T_switch=1000,
                 twoD_gas_cutoff_frequency=100):

        super().__init__(tree_dict,
                         group_lib,
                         copy.deepcopy(adsorbate_lib),
                         gas_lib,
                         copy.deepcopy(reference_dict),
                         slab_dict,
                         group_long_description,
                         group_short_description,
                         P_ref,
                         NASA7_T_switch,
                         twoD_gas_cutoff_frequency)

        self.ensemble_energies_array = ensemble_energies_array
        self.ref_ensemble = reference_ensemble
        self.ensemble_scale = ensemble_scale
        self.original_ads_list = copy.deepcopy(self.adsorbate_list)
        self.original_ref_dict = copy.deepcopy(self.reference_dict)
        self.EOF_uncertainty = self.original_ref_dict['EOF_uncertainty']
        self.rydberg_to_eV = 13.6056980659

    def write_files(
            self,
            directory="./",
            file_prefix="database",
            max_members=None,
            ):
        names = [ads.adsorbate_name for ads in self.adsorbate_list]
        ref_names = list(self.ref_ensemble.keys())
        if max_members:
            N_members = max_members
        else:
            N_members = len(self.ensemble_energies_array[names[0]])
        sampler = scipy.stats.qmc.Sobol(d=1, scramble=True, seed=12)
        for i in range(N_members):
            for j, name in enumerate(names):
                dE = self.ensemble_energies_array[name][i]
                dE *= self.rydberg_to_eV * self.ensemble_scale
                oldE = self.original_ads_list[j].dft_energy[0]
                newE = oldE - dE
                self.adsorbate_list[j].dft_energy[0] = newE
            for j, name in enumerate(ref_names):
                dE = self.ref_ensemble[name][i]
                dE *= self.rydberg_to_eV * self.ensemble_scale
                oldE = self.original_ref_dict['reference_energies'][name]
                EOF_perturbation = sampler.random()[0, 0]
                EOF_perturbation *= 2 * self.EOF_uncertainty[name]
                EOF_perturbation -= self.EOF_uncertainty[name]
                newE = oldE - dE + EOF_perturbation
                self.reference_dict['reference_energies'][name] = newE
            """ loop to do same for refs"""
            name = directory + file_prefix + "_{}.py".format(str(i))
            self.write_RMG_adsorption_correction_file(name)
        self.adsorbate_list = self.original_ads_list
        self.reference_dict = self.original_ref_dict
        return None
