'''
Here is a class that is used to represent nodes in a tree like
data structure. Each node has a data element attached to it: 'species'
and has a list of child nodes. The methods of this class allow for descending
the tree to find all children from all levels below, and to find all
species attached to a given node and from all levels below
'''

class Node:
    def __init__(self, name, species, children):
        self.name = name
        self.species = species
        self.children = children

    def __repr__(self):
        return self.name

    def get_all_species(self):
        species = None
        all_children = self.get_all_children()
        if self.species:
            species = make_list(self.species)
        else:
            species = []
        if all_children:
            for child in all_children:
                if child.species:
                    childspec = make_list(child.species)
                    for spec in childspec:
                        species.append(spec)
        return species

    def get_all_children(self):
        all_children = None
        if self.children:
            all_children = make_list(self.children)
            found_all = False
            while not found_all:
                new_children = []
                for children in all_children:
                    if children.children:
                        gchildren = make_list(children.children)
                        for gchild in gchildren:
                            if gchild not in all_children:
                                new_children.append(gchild)
                                all_children.append(gchild)

                if len(new_children) == 0:
                    found_all = True
        return all_children


def make_list(l):
    if not isinstance(l,list):
        l = [l]
    return l
