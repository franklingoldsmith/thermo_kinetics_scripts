from pathlib import Path
from node import Node

'''
Here the adsorption correction tree is represented by a set of nested Node
objects. Each Node object requires a name, which adsorbate species show up
at the level of that node, and at now lower levels, and a list of child nodes.

node = Node(node_name,[list of species], child_nodes)
'''

RX = Node('RX', None,[
    Node('RXbridged-bidentate',None,[
        Node('CXRCX',None,[
            Node('C=X=R-C-XR2','XCCHXCH2',None),
            Node('R2C-X-R-C-XR2','XCH2CH2XCH2',None),
            Node('RC=X-R=C-XR','XCHCHXCH',None),
            Node('RC-X=R-C-XR2','XCHCHXCH2',None),
            Node('RC=X-R-C-XR2','XCHCH2XCH2',None),
            Node('RC-X=R=C-XR','XCHCXCH',None),
            Node('RC-X=R=C=X','XCHCXC',None),
            Node('C#X-R-C-XR2','XCCH2XCH2',None),
            Node('C#X-R=C-XR','XCHCHXC',None),
            Node('C#X-R-C#X','XCCH2XC',None),
            Node('RC=X-R-C=XR','XCHCH2XCH',None),
            Node('C#X-R-C=XR','XCHCH2XC',None),
            ]),
        Node('CXROX',None,
             Node('RC-X=R-O-X','XCHCHXO',None),
             ),
        Node('OXROX',None,
             Node('O-X-C-O-X',['XOC(O)XO','H2C(XO)XO'],None),
             ),
        ]),
    Node('RXbidentate',None,[
        Node('CXCX',None,[
            Node('C-XC-X','XCXC',None),
            Node('C=XRC=XR','XCHXCH',None),
            Node('C-XR2C-XR2',['XCH2XCH2','CH3XCHXCH2'],None),
            Node('C-XR2C=XR',['XCH2XCH','XCH2XCOH','XCHXCHCH3'],None),
            Node('C-XRC=X','XCHXC',None),
            Node('C=XRC-XR','XCHXCO',None),
            Node('C#XC-XR','XCXCCH2',None),
            Node('C#XC-XR2',['XCXCH2','XCXCHCH3'],None),
            Node('C#XC=XR','XCXCCH3',None),
            Node('C-XR2C-XR','XCH2XCCH2',None),
            Node('C-XRC-XR','XCHXCCH3',None),
            ]),
        Node('NXCX',None,[
            Node('inv(C=XRN=X)',['XCHXN','XNXCOH'],None),
            Node('inv(C-XR2N=X)','XCH2XN',None),
            Node('inv(C-XR2N-XR)','XCH2XNH',None),
            Node('inv(C=XRN-XR)',['XCHXNH','OHXCXNH'],None),
            Node('inv(C-XRN-X)','XCHXN',None),
            Node('inv(C-XRN=X)',['XNXCO','XNXCNH'],None),
            Node('inv(C-XRN-XR)',['NHXCXNH','XNHXCO'],None),
            ]),
        Node('CXNX',None,[
            Node('C=XRN=X',['XCHXN','XNXCOH'],None),
            Node('C-XR2N=X','XCH2XN',None),
            Node('C-XR2N-XR','XCH2XNH',None),
            Node('C=XRN-XR',['XCHXNH','OHXCXNH'],None),
            Node('C-XRN-X','XCHXN',None),
            Node('C-XRN=X',['XNXCO','XNXCNH'],None),
            Node('C-XRN-XR',['NHXCXNH','XNHXCO'],None),
            ]),
        Node('CXOX',None,[
            Node('C=XRO-X','XCHXO',None),
            Node('C-XR2O-X','XCH2XO',None),
            Node('C-XRO-X','XOXCNH',None),
            ]),
        Node('NXNX',None,[
            Node('N-XRN-XR',['XNHXNH','CH3XNXNOH'],None),
            Node('N-XRN=X',['XNHXN','XNXNCH3'],None),
            ]),
        Node('NXOX',None,[
            Node('N-XRO-X','XOXNH',None),
            Node('N[+]=XR[-]O-X','XOXNO',None),
            ]),
        Node('OXOX','XOXO',None),
        ]),
    Node('RXsingle-chemisorbed',None,[
        Node('CX','XCN',[
            Node('CqX','XC',None),
            Node('C#XR','XCH',[
                Node('C#XCR3',['XCCH3','XCCH2CH3','XCCH2OH'],None),
                Node('C#XN',['XCNO','XCNH2'],None),
                Node('C#XOR','XCOH',None),
                Node('C#XCR2',['XCCHCH2','XCCHO'],None),
                ]),
            Node('C=XR2','XCH2',[
                Node('C=XRCR3',['CH3XCCH3','CH3XCOH','XCHCH2CH3','XCHCH3'],None),
                Node('C=XROR',['XCHOH','CH3XCOH'],None),
                Node('C=XRN',['XCHNH2','OHXCNH2','NH2XCNH2'],None),
                Node('C=XRCR2',['XCHCHCH2','XCHCHO'],None),
                ]),
            Node('C=X(=R)',None,[
                Node('C=X(=C)',['XCCO','XCCCH2','XCCH2'],None),
                Node('C=X(=NR)','XCNH',None),
                ]),
            Node('C-XR3',None,[
                Node('C-XR2CR3',['XCH2CH2CH3','XCH2CH2OH','XCH2CH3','CH3XCHCH3','CH3XCHOH'],None),
                Node('C-XR2N','XCH2NH2',None),
                Node('C-XR2OR',['XCH2OH','CH3XCHOH'],None),
                ]),
            Node('C-XR2',None,[
                Node('C-XRO',['XCHO','XCOOH','CH3XCO','XCCHO','CH3CH2XCO'],None),
                Node('C-XRCR2',['CH2XCCH3','CH2XCOH','XCHCCH2','XCHCH2','XCHCHCH3'],None),
                Node('C-XRNR',['XCHNH','OHXCNH','NH2XCNH'],None),
                Node('C-XRN',['OXCNH2','NH2XCNH'],None),
                ]),
            ]),
        Node('NX',None,[
            Node('N#X','XN',None),
            Node('N=XR','XNH',[
                Node('N=XC-R','XNCH3',None),
                Node('N=XN','XNNH2',None),
                Node('N=XOR','XNOH',None),
                Node('N=XC#R','XNCN',None),
                ]),
            Node('N-XR2','XNH2',[
                Node('N-XRCR3','XNHCH3',None),
                Node('N-XRNR2','XNHNH2',None),
                Node('N-XROR', 'XNHOH',None),
                Node('N-XRNR','XNHNO',None),
                Node('N-XRCR','XNHCHO',None),
                Node('N[+]-XR[-]R',['XNO2','OXNNH'],None),
                Node('N[+]=XR[-]R',['HXNO','CH3NXNOH','CH3XNNOH'],None),
                ]),
            Node('N-XR','XNO',[
                Node('N-XCR2','XNCH2',None),
                Node('N-XNR',['XNNH','XNNCH3'],None),
                Node('N-XCR',['XNCNH','XNCO'],None),
                ]),
            ]),
        Node('OX',None,[
            Node('O=X','XO',None),
            Node('O-XR','XOH',[
                Node('O-XCR3',['XOCH3','XOCH2CH3','XOCH2OH'],None),
                Node('O-XCR2',['XOCHCH2','HC(O)XO','XOC(OH)O'],None),
                Node('O-XN','XONH2',None),
                Node('O-XOR','XOOH',None),
                ]),
            ]),
        ]),
    Node('RXvdW',None,[
        Node('(CR4)X','CH4X',[
            Node('(CR3CR3)X',['CH3CH3X','CH3CH2CH3X','CH3CH2OHX'],None),
            Node('(CR3N)X','CH3NH2X',None),
            Node('(CR3OR)X',['CH3OHX','CH3OCH3X','CH3OCH2OHX','H2C(OH)OHX'],None),
            ]),
        Node('(CR3)X',None,[
            Node('(CR2N)X','CH2NHX',None),
            Node('(CR2CR)X',['CH2CH2X','CH3CHCH2X','CH2CCH2X'],None),
            Node('(CR2O)X',['CH2COX','CH2OX','OC(OH)OHX','CH3CHOX','HCOOHX'],None),
            ]),
        Node('(CR2)X',None,[
            Node('(CRN)X','NCOHX',None),
            Node('(CRCR)X',['CHCHX','CHCCH3X'],None),
            ]),
        Node('(NR3)X','NH3X',[
            Node('(NN)X',['NH2NH2X','NH2NCH3CH3X'],None),
            Node('(NO)X','H2NOHX',None),
            Node('(NC)X','OCHNH2X',None),
            ]),
        Node('(NR2)X',None,
             Node('(N=C)X',['OCNHX','NHCNHX'],None),
             ),
        Node('(OR2)X','H2OX',
             Node('(OROR)X','HOOHX',None),
             ),
        Node('(OR)X',None,
             Node('(ONR)X',None,[
                 Node('(ONOR)X','ONOHX',None),
                 Node('(ONN)X',['ONNH2X','ONNCH3CH3X'],None),
                 ]),
             ),
        ]),
    ])

# a check that there exists a file for each species in the tree
all_spec = RX.get_all_species()
for spec in all_spec:
    file = Path('../thermo/dft-data/' + str(spec) + '.dat')
    if file.exists():
        pass
    else:
        print('couldn\'t find: ', file)
