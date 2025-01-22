#!/usr/bin/env python 
# encoding: utf-8 

name = "Surface Adsorption Corrections"
shortDesc = u""
longDesc = u"""
Changes due to adsorbing on a surface.
Here, Pt(111)
Note: "-h" means "horizontal"
"""

entry( 
    index = 1,
    label = "R*",
    group= 
"""
1 R u0
2 X u0
""",
    thermo=None,
    shortDesc=u"""Anything adsorbed anyhow.""",
    longDesc=u"""
   R
   x
***********
This node should be empty, ensuring that one of the nodes below is used.
""",
)

entry( 
    index = 1,
    label = "CR2CCR3",
    group = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {9,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 R u0 p0 c0 {1,S}
7 R u0 p0 c0 {3,S}
8 R u0 p0 c0 {3,S}
9 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.21, 7.01, 10.5, 12.58, 14.58, 15.4, 16.09], 'J/(mol*K)'),
        H298=(-322.09, 'kJ/mol'),
        S298=(-224.56, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2CCH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 2,
    label = "CR2COR",
    group = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 R u0 p0 c0 {3,S}
5 R u0 p0 c0 {3,S}
6 R u0 p0 c0 {1,S}
7 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.44, 6.26, 7.2, 7.7, 8.15, 8.31, 8.42], 'J/(mol*K)'),
        H298=(-293.92, 'kJ/mol'),
        S298=(-153.64, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH2COH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 3,
    label = "CR3CO",
    group = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 R u0 p0 c0 {2,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {2,S}
7 X u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.03, 2.39, 4.05, 5.19, 6.51, 7.15, 7.8], 'J/(mol*K)'),
        H298=(-279.61, 'kJ/mol'),
        S298=(-160.67, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3CO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 4,
    label = "CRCCR2",
    group = 
"""
1 C u0 p0 c0 {3,D} {4,S} {7,S}
2 C u0 p0 c0 {3,D} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,D}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {2,S}
7 X u0 p0 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.41, 3.72, 7.67, 10.5, 13.84, 15.47, 16.78], 'J/(mol*K)'),
        H298=(-272.91, 'kJ/mol'),
        S298=(-184.12, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 5,
    label = "CRCR2-mono",
    group = 
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 C  u0  p0 c0 {2,D} {5,S} {6,S}
4 R  u0  p0 c0 {2,S}
5 R  u0  p0 c0 {3,S}
6 R  u0  p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.58, 7.63, 9.78, 11.32, 13.19, 14.22, 15.4], 'J/(mol*K)'),
        H298=(-268.02, 'kJ/mol'),
        S298=(-179.96, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCH2-mono single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 6,
    label = "CRCRCR3-mono",
    group = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 R u0 p0 c0 {1,S}
5 R u0 p0 c0 {1,S}
6 R u0 p0 c0 {1,S}
7 R u0 p0 c0 {2,S}
8 R u0 p0 c0 {3,S}
9 X u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.38, -0.31, 1.59, 3.09, 5.07, 6.19, 7.41], 'J/(mol*K)'),
        H298=(-283.9, 'kJ/mol'),
        S298=(-170.29, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCHCH3-mono single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 7,
    label = "CRCO-mono",
    group = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 R u0 p0 c0 {2,S}
5 X u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-8.55, -4.82, -2.31, -0.6, 1.49, 2.62, 3.75], 'J/(mol*K)'),
        H298=(-304.39, 'kJ/mol'),
        S298=(-153.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CHCO-mono double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 8,
    label = "COOR",
    group = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {4,S}
4 R u0 p0 c0 {3,S}
5 X u0 p0 c0 {1,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.1, 3.6, 5.13, 6.12, 7.27, 7.86, 8.41], 'J/(mol*K)'),
        H298=(-294.57, 'kJ/mol'),
        S298=(-154.05, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from COOH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 9,
    label = "RCO-mono",
    group = 
"""
1 X  u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 R  u0  p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.42, 8.26, 10.63, 12.12, 13.7, 14.49, 15.43], 'J/(mol*K)'),
        H298=(-266.93, 'kJ/mol'),
        S298=(-163.88, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HCO-mono single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry( 
    index = 10,
    label = "CR3CR2CO",
    group = 
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 C u0 p0 c0 {1,D} {2,S} {10,S}
5 R u0 p0 c0 {2,S}
6 R u0 p0 c0 {2,S}
7 R u0 p0 c0 {3,S}
8 R u0 p0 c0 {3,S}
9 R u0 p0 c0 {3,S}
10 X u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.18, 2.59, 4.42, 5.64, 7.01, 7.65, 8.17], 'J/(mol*K)'),
        H298=(-265.84, 'kJ/mol'),
        S298=(-173.89, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from CH3CH2CO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)



    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.32, 3.63, 5.87, 7.37, 9.08, 9.94, 10.77], 'J/(mol*K)'),
        H298=(-285.22, 'kJ/mol'),
        S298=(-171.81, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)