#!/usr/bin/env python
# encoding: utf-8

name = "Surface Adsorption Corrections Pt(111)"
shortDesc = u"Surface adsorption corrections Pt(111)"
longDesc = u"""
Changes in thermophysical properties due to adsorption on a surface, here Pt(111). Adsorption corrections are based on DFT calculations performed by Katrin Blondal and 
Bjarne Kreitz (Brown University). The computational methods and details are explained in Kreitz, Blöndal, Goldsmith et al. ACS Catal, 2022, 12,
11137-11151 (https://doi.org/10.1021/acscatal.2c03378) and Kreitz, Goldsmith et al., Angew. Chem. Int. Ed., 2023, 62, e202306514 (https://onlinelibrary.wiley.com/doi/10.1002/anie.202306514). 
The calculation of the adsorption corrections is explained in detail in the SI. 
If you use these adsorption corrections database in your work, please cite the publications mentioned above. 

TODO: Update adsorption corrections for N containing molecules. 
"""

entry(
    index = 1,
    label = "RX",
    group=
"""
1 R  ux
2 * X ux
""",
    thermo=None,
    shortDesc=u"""Anything adsorbed anyhow.""",
    longDesc=u"""
   R
   X
***********
This node should be empty, ensuring that one of the nodes below is used.


The group could well be defined as:

    1 R ux
    2 * Xux

but then it is identical with the R*vdW node, and the database tests
do not like that. It should be OK, because things would check the
tree in order, and if there *was* a bond it would match either
R*bidentate or R*single_chemisorbed and thus not R*vdW.
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 1,
#    label = "R-*",
#    group =
#"""
#1 * X u0 p0 c0 {2,S}
#2 R  u0 p0 c0 {1,S}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([-2.46, -1.45, -0.78, -0.33, 0.18, 0.46, 0.74], 'cal/(mol*K)'),
#        H298=(-58.54, 'kcal/mol'),
#        S298=(-26.39, 'cal/(mol*K)'),
#    ),
#    shortDesc=u"""Came from H single-bonded on Pt(111)""",
#    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -2.479 eV.
#            Linear scaling parameters: ref_adatom_H = -2.479 eV, psi = 0.00000 eV, gamma_H(X) = 1.000.
#
#   R
#   |
#***********
#
#""",
#    metal = "Pt",
#    facet = "111",
#)

### This doesn't have a place in the tree, so I'm commenting it out. -- RHW
# entry(
#     index = 2,
#     label = "(R2)*",
#     group =
# """
# 1 * X u0 p0 c0
# 2 R  u0 p0 c0 {3,S}
# 3 R  u0 p0 c0 {2,S}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([0.92, 0.95, 0.97, 0.98, 0.98, 0.99, 0.99], 'cal/(mol*K)'),
#         H298=(-1.45, 'kcal/mol'),
#         S298=(-7.73, 'cal/(mol*K)'),
#     ),
#     shortDesc=u"""Came from H2 physisorbed on Pt(111)""",
#     longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#             DFT binding energy: -0.054 eV.
#             Linear scaling parameters: ref_adatom_H = -2.479 eV, psi = -0.05448 eV, gamma_H(X) = 0.000.
#             The two lowest frequencies, 14.0 and 24.4 cm-1, where replaced by the 2D gas model.
#
#   R-R
#    :
# ***********
#""",
#    metal = "Pt",
#    facet = "111",
# )

entry(
    index = 3,
    label = "(OR2)X",
    group =
"""
1 * X u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 R  u0 p[0,1,2] c0 {2,S}
4 R  u0 p[0,1,2] c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.39, 8.41, 8.91, 9.16, 9.4, 9.51, 9.6], 'J/(mol*K)'),
        H298=(-49.08, 'kJ/mol'),
        S298=(-123.53, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged H2OX, HOOHX, CH3OHX, HCOOHX, CH3CH2OHX, CH3OCH3X, CH3OCH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.   
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method.    

 RO-R
   :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 4,
    label = "O-XR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.67, 8.28, 9.16, 9.7, 10.33, 10.68, 11.17], 'J/(mol*K)'),
        H298=(-194.2, 'kJ/mol'),
        S298=(-157.49, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XOCH3, XOH, XOCH2CH3, HOC(O)XO, HC(O)XO, XOCHCH2, XOOH, XOCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 5,
    label = "(OROR)X",
    group =
"""
1 * X u0 p0 c0
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 p0 c0 {2,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.32, 7.23, 7.68, 7.95, 8.29, 8.51, 8.71], 'J/(mol*K)'),
        H298=(-63.01, 'kJ/mol'),
        S298=(-110.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HOOHX physisorbed on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            
            The two lowest frequencies, 12.0 and 47.7 cm-1, where replaced by the 2D gas model.  
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method.           
            
 RO-OR
   :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 6,
    label = "OXOX",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.69, 12.02, 13.4, 13.87, 13.89, 13.63, 13.13], 'J/(mol*K)'),
        H298=(-107.21, 'kJ/mol'),
        S298=(-167.43, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XOXO, twice single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   O--O
   |  |
***** *****
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 7,
    label = "O-XOR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.21, 11.38, 11.38, 11.02, 10.19, 9.56, 8.77], 'J/(mol*K)'),
        H298=(-134.04, 'kJ/mol'),
        S298=(-120.71, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XOOH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   OR
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 8,
    label = "O=X",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 O  u0 p2 c0 {1,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.44, 0.14, 1.49, 2.26, 3.07, 3.45, 3.84], 'J/(mol*K)'),
        H298=(-382.56, 'kJ/mol'),
        S298=(-140.6, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   O
   ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 9,
    label = "O-XN",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 N  u0 p1 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.23, 4.15, 5.77, 6.69, 7.58, 7.95, 8.26], 'J/(mol*K)'),
        H298=(-128.14, 'kJ/mol'),
        S298=(-134.71, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   NR2
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 10,
    label = "O-XCR3",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.44, 2.24, 2.93, 3.54, 4.49, 5.18, 6.35], 'J/(mol*K)'),
        H298=(-182.55, 'kJ/mol'),
        S298=(-149.81, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XOCH3, XOCH2CH3, and XOCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 11,
    label = "(NR3)X",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S} {4,S} {5,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.37, 5.63, 6.99, 7.84, 8.8, 9.28, 9.75], 'J/(mol*K)'),
        H298=(-102.99, 'kJ/mol'),
        S298=(-139.16, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
     NR3
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 12,
    label = "N-XR2",
    group =
"""
1 * X u0 p0 c0 {2,[S,D]}
2 N u0 px cx {1,[S,D]} {3,[S,D]} {4,S}
3 R u0 px c0 {2,[S,D]}
4 R u0 px cx {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.13, 8.26, 10.06, 11.14, 12.25, 12.75, 13.24], 'J/(mol*K)'),
        H298=(-210.52, 'kJ/mol'),
        S298=(-174.57, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

     NR2
     |
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 13,
    label = "N=XR",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 R  u0 px c0 {2,S}
""",
   thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.43, 6.4, 8.43, 9.48, 10.34, 10.65, 11.14], 'J/(mol*K)'),
        H298=(-324.83, 'kJ/mol'),
        S298=(-167.02, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

    NR
    ||
***********
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 14,
#    label = "N#X",
#    group =
#"""
#1 * X u0 p0 c0 {2,T}
#2 N  u0 p1 c0 {1,T}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([-0.93, -0.2, 0.19, 0.42, 0.66, 0.78, 0.9], 'cal/(mol*K)'),
#        H298=(-103.33, 'kcal/mol'),
#        S298=(-32.92, 'cal/(mol*K)'),
#    ),
#    shortDesc=u"""Came from XN triple-bonded on Pt(111)""",
#    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -4.352 eV.
#            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = 0.00000 eV, gamma_N(X) = 1.000.
#
#    N
#   |||
#***********
#""",
#    metal = "Pt",
#    facet = "111",
#)

entry(
    index = 15,
    label = "(NO)X",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S}
3 O  u0 p2 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.4, 5.22, 6.26, 6.89, 7.57, 7.89, 8.19], 'J/(mol*K)'),
        H298=(-89.92, 'kJ/mol'),
        S298=(-131.24, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R2N-OR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 16,
#    label = "(NRO)*",
#    group =
#"""
#1 * X u0 p0 c0
#2 N  u0 p1 c0 {3,D} {4,S}
#3 O  u0 p2 c0 {2,D}
#4 R  u0 p0 c0 {2,S}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([7.95, 11.63, 13.59, 14.61, 15.38, 15.61, 15.88], 'J/(mol*K)'),
#        H298=(-173.61, 'kJ/mol'),
#        S298=(-171.34, 'J/(mol*K)'),
#    ),
#    shortDesc=u"""Came from HNO* averaged on Pt(111)""",
#    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
#            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
#            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
#            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
#            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
#    RN=O
#     :
#***********
#""",
#    metal = "Pt",
#    facet = "111",
#)

entry(
    index = 17,
    label = "N-XROR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.06, 11.67, 13.55, 14.62, 15.71, 16.24, 16.71], 'J/(mol*K)'),
        H298=(-192.37, 'kJ/mol'),
        S298=(-189.5, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHOH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R-N-OR
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 18,
    label = "N-XR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 R  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.48, 6.03, 7.43, 8.23, 9.04, 9.41, 9.83], 'J/(mol*K)'),
        H298=(-217.64, 'kJ/mol'),
        S298=(-161.94, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
     NR
     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 19,
    label = "N-XRO-X",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.91, 11.47, 14.33, 15.65, 16.31, 16.24, 16.06], 'J/(mol*K)'),
        H298=(-155.87, 'kJ/mol'),
        S298=(-186.75, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from HXNO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

  R-N--O
   ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 20,
    label = "N=XOR",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([9.02, 13.02, 14.81, 15.51, 15.68, 15.48, 15.38], 'J/(mol*K)'),
        H298=(-301.49, 'kJ/mol'),
        S298=(-178.28, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNOH double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 RO-N
    ||
***********
""",
    metal = "Pt",
    facet = "111",
)
entry(
    index = 21,
    label = "(NN)X",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S}
3 N  u0 p1 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.76, 4.0, 5.34, 6.18, 7.1, 7.55, 8.01], 'J/(mol*K)'),
        H298=(-121.85, 'kJ/mol'),
        S298=(-150.77, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
            
  R2N-NR2
     :            
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 22,
    label = "(N=C)X",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,D}
3 C  u0 p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.54, 7.09, 7.44, 7.69, 8.0, 8.18, 8.34], 'J/(mol*K)'),
        H298=(-107.27, 'kJ/mol'),
        S298=(-122.2, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

    RN=CR
     :
***********
""",
    metal = "Pt",
    facet = "111",
)


#entry(
#    index = 23,
#    label = "(NN)*",
#    group =
#"""
#1 * X u0 p0 c0
#3 N  u0 p1 c0 {3,T}
#4 N  u0 p1 c0 {2,T}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([2.62, 3.77, 4.27, 4.45, 4.43, 4.3, 4.09], 'cal/(mol*K)'),
#        H298=(-6.31, 'kcal/mol'),
#        S298=(-15.27, 'cal/(mol*K)'),
#    ),
#    shortDesc=u"""Came from NN physisorbed on Pt(111)""",
#    longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#            DFT binding energy: -0.109 eV.
#            Linear scaling parameters: ref_adatom_N = -4.352 eV, psi = -0.10949 eV, gamma_N(X) = 0.000.
#            The two lowest frequencies, 6.3 and 24.2 cm-1, where replaced by the 2D gas model.
#
#  N#N
#   :
#***********
#"""
#)

entry(
    index = 24,
    label = "N-XRNR2",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,S} {6,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.08, 10.33, 12.3, 13.56, 14.96, 15.68, 16.38], 'J/(mol*K)'),
        H298=(-180.56, 'kJ/mol'),
        S298=(-188.53, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHNH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R-N-NR2
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 25,
    label = "N-XNR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 N  u0 p1 c0 {2,D} {4,S}
4 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.46, 7.33, 9.01, 10.01, 11.0, 11.42, 11.88], 'J/(mol*K)'),
        H298=(-171.76, 'kJ/mol'),
        S298=(-164.09, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   NR
  ||
   N
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 26,
    label = "N=XN",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 N  u0 p1 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([11.22, 15.36, 17.05, 17.49, 16.95, 16.18, 15.43], 'J/(mol*K)'),
        H298=(-257.11, 'kJ/mol'),
        S298=(-174.76, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNNH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   NR2
   |
   N
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 27,
    label = "N-XRN-XR",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.54, 11.61, 13.0, 13.54, 13.6, 13.36, 12.88], 'J/(mol*K)'),
        H298=(-126.39, 'kJ/mol'),
        S298=(-165.74, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

  RN-NR
   | |
***********
""",
    metal = "Pt",
    facet = "111",
)
entry(
    index = 28,
    label = "N-XRCR3",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {1,S} {2,S} {7,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.5, 7.94, 10.13, 11.59, 13.27, 14.16, 15.24], 'J/(mol*K)'),
        H298=(-226.05, 'kJ/mol'),
        S298=(-193.75, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHCH3 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R-N-CR3
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 29,
    label = "N-XCR2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {1,S} {2,D}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.6, 9.95, 11.83, 12.98, 14.21, 14.82, 15.56], 'J/(mol*K)'),
        H298=(-220.39, 'kJ/mol'),
        S298=(-182.78, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   CR2
  ||
   N
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 30,
    label = "N=XC-R",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S}
3 N  u0 p1 c0 {1,D} {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.25, 9.23, 10.95, 12.07, 13.39, 14.14, 15.15], 'J/(mol*K)'),
        H298=(-360.49, 'kJ/mol'),
        S298=(-178.8, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNCH3 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R3C-N
     || 
***********
""",
    metal = "Pt",
    facet = "111",
)


### Leads to AtomTypeError: Unable to determine atom type for atom O-, which has 3 single bonds, 0 double bonds to C, 0 double bonds to O, 0 double bonds to S, 0 triple bonds, 0 benzene bonds, 0 lone pairs, and 2 charge.
### And is not in the tree anyway, so commenting out. RHW
# entry(
#     index = 31,
#     label = "N-*O2",
#     group =
# """
# 1 * X u0  p0 c0 {2,S}
# 2 N  u0  p0 c+1 {1,S} {3,S} {4,D}
# 3 O  u0  p2 c-1 {2,S}
# 4 O  u0  p2 c0 {2,D}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([1.92, 2.12, 2.17, 2.17, 2.13, 2.09, 2.04], 'cal/(mol*K)'),
#         H298=(34.56, 'kcal/mol'),
#         S298=(-33.93, 'cal/(mol*K)'),
#     ),
#     shortDesc=u"""Came from ON-O single-bonded on Pt(111)""",
#     longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#             Linear scaling parameters: ref_adatom_N = 0.525 eV, psi = -0.86302 eV, gamma_N(X) = 0.333.
#             The two lowest frequencies, -33.2 and 55.1 cm-1, where replaced by the 2D gas model.
#
#  O-N=O
#    |
# ***********
# """,
#    metal = "Pt",
#    facet = "111",
# )

entry(
    index = 32,
    label = "CqX",
    group =
"""
1 * X u0 p0 c0 {2,Q}
2 C  u0 p0 c0 {1,Q}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.34, -3.34, -1.0, 0.42, 1.97, 2.73, 3.51], 'J/(mol*K)'),
        H298=(-657.91, 'kJ/mol'),
        S298=(-133.84, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XC quadruple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   C
 ||||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 33,
    label = "C-XC-X",
    group =
"""
1 * X u0  p0 c0 {3,D}
2 X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,D} {4,D}
4 C  u0  p0 c0 {2,D} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.31, 7.38, 9.53, 10.71, 11.76, 12.14, 12.4], 'J/(mol*K)'),
        H298=(-613.35, 'kJ/mol'),
        S298=(-163.77, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXC double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  C==C
 ||  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 34,
    label = "C=X(=R)",
    group =
"""
1 * X  u0  p0 c0 {2,D}
2 C   u0  p0 c0 {1,D} {3,D}
3 R!H u0  px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.94, 6.26, 8.08, 9.18, 10.4, 11.04, 11.77], 'J/(mol*K)'),
        H298=(-429.79, 'kJ/mol'),
        S298=(-168.79, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCCH2, XCCCH2, XCCO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
  ||
   C
  ||
***********

Because the C atom bonded to the surface only has one ligand
not two, it is not a child of the C=*R2 node
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 35,
    label = "C#XCR3",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,T} {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.91, 1.58, 4.18, 6.07, 8.47, 9.86, 11.63], 'J/(mol*K)'),
        H298=(-594.9, 'kJ/mol'),
        S298=(-174.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCCH3, XCCH2CH3, XCCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 36,
    label = "C#XR",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.12, 2.73, 5.33, 7.1, 9.21, 10.37, 11.81], 'J/(mol*K)'),
        H298=(-571.12, 'kJ/mol'),
        S298=(-176.66, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH, XCCH3, XCOH, XCCHCH2, XCCH2CH3, XCCHO, XCCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 37,
    label = "C=XRC=XR",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,D} {3,S} {6,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.41, -0.06, 4.05, 6.96, 10.38, 12.03, 13.24], 'J/(mol*K)'),
        H298=(-221.27, 'kJ/mol'),
        S298=(-175.96, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXCH double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R-C--C-R
  ||  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 38,
    label = "C=XR2",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.24, 3.87, 6.15, 7.64, 9.38, 10.32, 11.42], 'J/(mol*K)'),
        H298=(-370.06, 'kJ/mol'),
        S298=(-174.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2, CH3XCCH3, CH3XCOH, XCHCH2CH3, XCHCH3, XCHCHCH2, XCHCHO, XCHOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R-C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 39,
    label = "C-XR2C-XR2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {4,S}
8 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.94, 10.72, 13.46, 15.04, 16.54, 17.1, 17.33], 'J/(mol*K)'),
        H298=(-124.09, 'kJ/mol'),
        S298=(-192.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2XCH2 and CH3XCHXCH2 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C--CR2
   |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 40,
    label = "C-XR3",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.16, 2.29, 4.74, 6.49, 8.69, 9.93, 11.24], 'J/(mol*K)'),
        H298=(-212.02, 'kJ/mol'),
        S298=(-176.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2CH2CH3, XCH2CH2OH, XCH2CH3, XCH2CHCH2, XCH2CHO, XCH3, CH3XCHCH3, CH3XCHOH, XCH2OH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 41,
    label = "(CR3CR3)X",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
8 R  u0 px c0 {3,S}
9 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([9.04, 9.93, 10.39, 10.67, 10.97, 11.11, 11.2], 'J/(mol*K)'),
        H298=(-29.6, 'kJ/mol'),
        S298=(-137.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH3CH3X, CH3CH2CH3X, CH3CH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R3C-CR3
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 42,
    label = "(CR4)X",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 R  u0 px c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.55, 9.48, 9.93, 10.16, 10.36, 10.44, 10.48], 'J/(mol*K)'),
        H298=(-41.27, 'kJ/mol'),
        S298=(-125.91, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH4X, CH3CH3X, CH3CH2CH3X, CH3CH2OHX, CH3OHX, CH3OCH3X, CH3OCH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  R3C-R
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 43,
    label = "C-XRN=X",
    group =
"""
1 X u0  p0 c0 {3,S}
2 * X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,S} {5,D}
4 N  u0  p1 c0 {2,D} {3,S}
5 R!H u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.84, 9.2, 10.96, 11.87, 12.58, 12.74, 12.69], 'J/(mol*K)'),
        H298=(-261.47, 'kJ/mol'),
        S298=(-188.76, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
   R== C--N
       | ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 44,
    label = "C=X(=NR)",
    group =
"""
1 * X u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 N  u0  p1 c0 {2,D} {4,S}
4 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.69, 8.35, 10.08, 11.19, 12.37, 12.85, 13.09], 'J/(mol*K)'),
        H298=(-213.22, 'kJ/mol'),
        S298=(-158.37, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

    NR
   ||
    C
   ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 45,
    label = "C#XN",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 N  u0 p1 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.55, 5.56, 6.5, 6.97, 7.34, 7.44, 7.62], 'J/(mol*K)'),
        H298=(-432.07, 'kJ/mol'),
        S298=(-161.89, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
***********
   NR2
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)


## Not present in the tree
# entry(
#     index = 46,
#     label = "C=*O",
#     group =
# """
# 1 * X u0  p0 c0 {2,D}
# 2 C  u0  p0 c0 {1,D} {3,D}
# 3 O  u0  p2 c0 {2,D}
# """,
#     thermo=ThermoData(
#         Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#         Cpdata=([1.81, 2.37, 2.68, 2.88, 3.05, 3.1, 3.08], 'cal/(mol*K)'),
#         H298=(-41.06, 'kcal/mol'),
#         S298=(-38.09, 'cal/(mol*K)'),
#     ),
#     shortDesc=u"""Came from CO-f double-bonded on Pt(111)""",
#     longDesc=u"""Calculated by Katrin Blondal at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb). Based on DFT calculations by Jelena Jelic at KIT.
#             DFT binding energy: -1.480 eV.
#             Linear scaling parameters: ref_adatom_C = -6.750 eV, psi = 1.89529 eV, gamma_C(X) = 0.500.
#
#    O
#   ||
#    C
#   ||
# ***********
# """,
#    metal = "Pt",
#    facet = "111",
# )

entry(
    index = 47,
    label = "C#XOR",
    group =
"""
1 * X u0 p0 c0 {2,T}
2 C  u0 p0 c0 {1,T} {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.83, 9.83, 11.9, 12.95, 13.69, 13.91, 14.43], 'J/(mol*K)'),
        H298=(-463.49, 'kJ/mol'),
        S298=(-187.54, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCOH triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   OR
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 48,
    label = "C-XR2C=XR",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,D} {3,S} {7,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.74, 6.17, 9.66, 11.87, 14.28, 15.41, 16.39], 'J/(mol*K)'),
        H298=(-330.81, 'kJ/mol'),
        S298=(-214.97, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCHXCH2, XCH2XCOH, XCHXCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C--CR
   |  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 49,
    label = "C-XR2CR3",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {3,S}
8 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.39, 3.93, 6.35, 8.02, 10.07, 11.2, 12.43], 'J/(mol*K)'),
        H298=(-214.46, 'kJ/mol'),
        S298=(-192.28, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2CH2CH3, XCH2CH2OH, XCH2CH3, CH3XCHCH3, CH3XCHOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
 R-C-CR3
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "(CR2N)X",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 N  u0 p1 c0 {2,D}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.41, 6.41, 7.92, 8.61, 8.94, 8.88, 8.61], 'J/(mol*K)'),
        H298=(-65.98, 'kJ/mol'),
        S298=(-134.58, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

  R2C=NR
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "C-XR2N",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 N  u0 p1 c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.28, -0.6, 1.5, 3.09, 5.17, 6.35, 7.61], 'J/(mol*K)'),
        H298=(-239.47, 'kJ/mol'),
        S298=(-142.63, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   R
   |
 R-C-NR2
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
    label = "(CR2O)X",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 O  u0 p2 c0 {2,D}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.0, 6.87, 7.39, 7.72, 8.09, 8.27, 8.39], 'J/(mol*K)'),
        H298=(-73.08, 'kJ/mol'),
        S298=(-122.36, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged H2COX, HCOOHX, CH3CHOX, OCO2H2X, CH2COX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C=O
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
    label = "C-XR2OR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O  u0 p2 c0 {2,S} {6,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.14, 0.0, 2.2, 3.74, 5.64, 6.69, 7.8], 'J/(mol*K)'),
        H298=(-225.57, 'kJ/mol'),
        S298=(-157.56, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCH2OH, CH3XCHOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

    R
    |
  R-C-OR
    |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 54,
    label = "(CR3N)X",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 N  u0 p1 c0 {2,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.87, 3.1, 4.54, 5.49, 6.55, 7.09, 7.71], 'J/(mol*K)'),
        H298=(-112.54, 'kJ/mol'),
        S298=(-142.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R3C-NR2
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 55,
    label = "(CR3OR)X",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.44, 9.53, 10.02, 10.25, 10.41, 10.45, 10.47], 'J/(mol*K)'),
        H298=(-57.56, 'kJ/mol'),
        S298=(-139.36, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH3OHX, CH3OCH3X, H2CO2H2X, CH3OCH2OHX on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R3C-OR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 56,
    label = "C-XRC=X",
    group =
"""
1 * X u0  p0 c0 {3,S}
2 X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,D} {5,S}
4 C  u0  p0 c0 {2,D} {3,D}
5 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.53, 3.23, 6.15, 7.98, 10.0, 10.99, 11.95], 'J/(mol*K)'),
        H298=(-440.52, 'kJ/mol'),
        S298=(-184.43, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXC single- and double bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 RC--C
  |  ||
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 57,
    label = "C-XRCR2",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 C  u0  p0 c0 {2,D} {5,S} {6,S}
4 R  u0  px c0 {2,S}
5 R  u0  px c0 {3,S}
6 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.29, 4.86, 7.35, 9.04, 10.97, 11.92, 12.82], 'J/(mol*K)'),
        H298=(-288.17, 'kJ/mol'),
        S298=(-182.51, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH2XCCH3, CH2XCOH, XCHCCH2, XCHCH2, XCHCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
  ||
   C-R
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 58,
    label = "C=XRCR3",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,D} {2,S} {7,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {2,S}
7 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.78, 4.72, 6.6, 7.86, 9.39, 10.26, 11.34], 'J/(mol*K)'),
        H298=(-372.23, 'kJ/mol'),
        S298=(-179.04, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH3XCCH3, CH3XCOH, XCHCH2CH3, XCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR3
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 59,
    label = "(CRN)X",
    group =
"""
1 * X u0  p0 c0
2 C  u0  p0 c0 {3,T} {4,S}
3 N  u0  p1 c0 {2,T}
4 R  u0  px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.39, 7.83, 8.07, 8.27, 8.6, 8.83, 8.99], 'J/(mol*K)'),
        H298=(-97.41, 'kJ/mol'),
        S298=(-122.25, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
            
    RC#N
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 60,
    label = "C=XRN=X",
    group =
"""
1 X u0 p0 c0 {3,D}
2 * X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.05, 7.44, 9.68, 11.15, 12.68, 13.22, 13.32], 'J/(mol*K)'),
        H298=(-131.53, 'kJ/mol'),
        S298=(-176.43, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    R
    |
    C-N
   || ||
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 61,
    label = "C-XRNR",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 N  u0  p1 c0 {2,D} {5,S}
4 R  u0  px c0 {2,S}
5 R  u0  px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.12, 2.64, 4.4, 5.55, 6.79, 7.37, 7.91], 'J/(mol*K)'),
        H298=(-289.96, 'kJ/mol'),
        S298=(-151.07, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
  NR
  ||
   C-R
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 62,
    label = "C=XRN-XR",
    group =
"""
1 X u0 p0 c0 {3,D}
2 * X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.85, 8.73, 11.16, 12.73, 14.43, 15.22, 15.97], 'J/(mol*K)'),
        H298=(-319.29, 'kJ/mol'),
        S298=(-194.68, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    R
    |
    C-NR
   || |
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 63,
    label = "C=XRN",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 N  u0 p1 c0 {2,S}
4 R  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.95, 5.05, 6.07, 6.62, 7.15, 7.38, 7.7], 'J/(mol*K)'),
        H298=(-306.99, 'kJ/mol'),
        S298=(-145.07, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   NR2
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 64,
    label = "C-XRO",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 O  u0  p2 c0 {2,D}
4 R  u0  px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.65, 2.4, 4.38, 5.69, 7.2, 7.95, 8.71], 'J/(mol*K)'),
        H298=(-282.27, 'kJ/mol'),
        S298=(-161.1, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged HXCO, OXCOH, CH3XCO, CHXCO, CH3CH2XCO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   R
   |
   C=O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 65,
    label = "C=XRO-X",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.91, 10.27, 12.84, 14.27, 15.45, 15.81, 16.1], 'J/(mol*K)'),
        H298=(-238.17, 'kJ/mol'),
        S298=(-167.73, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  R
  |
  C--O
 ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 66,
    label = "C=XROR",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.05, 2.82, 4.47, 5.52, 6.78, 7.48, 8.24], 'J/(mol*K)'),
        H298=(-325.89, 'kJ/mol'),
        S298=(-146.57, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCHOH and CH3XCOH on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   OR
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 67,
    label = "CX",
    group =
"""
1 * X u0 {2,[S,D,T,Q]}
2 C  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.31, 3.22, 5.55, 7.13, 8.99, 9.99, 11.1], 'J/(mol*K)'),
        H298=(-359.63, 'kJ/mol'),
        S298=(-173.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 68,
    label = "NX",
    group =
"""
1 * X u0 {2,[S,D,T]}
2 N  u0 {1,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.34, 6.5, 8.23, 9.21, 10.12, 10.5, 10.88], 'J/(mol*K)'),
        H298=(-226.68, 'kJ/mol'),
        S298=(-169.61, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 69,
    label = "OX",
    group =
"""
1 * X u0 {2,[S,D]}
2 O  ux {1,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.66, 7.38, 8.31, 8.88, 9.52, 9.88, 10.36], 'J/(mol*K)'),
        H298=(-215.12, 'kJ/mol'),
        S298=(-155.61, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 70,
    label = "RXsingle-chemisorbed",
    group =
"""
1 * X u0 {2,[S,D,T,Q]}
2 R  ux {1,[S,D,T,Q]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.84, 4.02, 6.08, 7.46, 9.09, 9.97, 10.96], 'J/(mol*K)'),
        H298=(-331.96, 'kJ/mol'),
        S298=(-169.67, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 71,
    label = "CXCX",
    group =
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,[S,D,T]}
3 C  u0 {1,[S,D,T]} {4,[S,D,T]}
4 C  u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.88, 5.67, 8.7, 10.62, 12.69, 13.65, 14.5], 'J/(mol*K)'),
        H298=(-353.37, 'kJ/mol'),
        S298=(-192.89, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 72,
    label = "CXNX",
    group =
"""
1 X u0 p0 c0 {3,[S,D,T]}
2 * X u0 p0 c0 {4,[S,D]}
3 C u0 p0 c0 {1,[S,D,T]} {4,[S,D]}
4 N u0 p[0,1] c[0,+1] {2,[S,D]} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.36, 9.29, 11.64, 13.06, 14.42, 14.92, 15.16], 'J/(mol*K)'),
        H298=(-201.39, 'kJ/mol'),
        S298=(-187.87, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)


#Changed the adjacency list because O can only have a single bond to the surface and another atom. 
#Always 2 free electron pairs. BK 2023/1/10
entry(
    index = 73,
    label = "CXOX",
    group =
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,S}
3 C  u0 {1,[S,D,T]} {4,S}
4 O  u0 p2 {2,S} {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.34, 11.93, 14.46, 15.74, 16.6, 16.72, 16.63], 'J/(mol*K)'),
        H298=(-149.6, 'kJ/mol'),
        S298=(-169.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all child nodes on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 74,
    label = "NXNX",
    group =
"""
1 * X u0 {3,[S,D]}
2 X u0 {4,[S,D]}
3 N  u0 {1,[S,D]} {4,[S,D]}
4 N  u0 {2,[S,D]} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.07, 10.54, 12.42, 13.41, 14.15, 14.31, 14.36], 'J/(mol*K)'),
        H298=(-161.84, 'kJ/mol'),
        S298=(-180.98, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 75,
    label = "RXbidentate",
    group =
"""
1 * X  u0 p0 c0 {3,[S,D,T]}
2 X  u0 p0 c0 {4,[S,D,T]}
3 R!H u0 {1,[S,D,T]} {4,[S,D,T]}
4 R!H u0 {2,[S,D,T]} {3,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.59, 6.37, 9.34, 11.19, 13.12, 13.99, 14.74], 'J/(mol*K)'),
        H298=(-330.73, 'kJ/mol'),
        S298=(-190.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all child nodes on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 76,
    label = "RXvdW",
    group =
"""
1 * X u0
2 R  u0
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.25, 8.33, 8.9, 9.23, 9.56, 9.7, 9.8], 'J/(mol*K)'),
        H298=(-56.05, 'kJ/mol'),
        S298=(-125.18, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged of (CR4)*, (CR3)*, and (OR2)* (nitrogen is not included) on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 77,
    label = "NXOX",
    group =
"""
1 * X u0 p0 c0 {3,[S,D]}
2 X u0 p0 c0 {4,S}
3 N  u0 px cx {1,[S,D]} {4,[S,D]}
4 O  u0 p2 c0 {2,S} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.82, 8.98, 11.06, 12.02, 12.53, 12.5, 12.33], 'J/(mol*K)'),
        H298=(-189.95, 'kJ/mol'),
        S298=(-167.0, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
***************
""",
    metal = "Pt",
    facet = "111",
)

#entry(
#    index = 78,
#    label = "O*O*",
#    group =
#"""
#1 * X u0 p0 c0 {3,S}
#2 * X u0 p0 c0 {4,S}
#3 O  u0 p2 c0 {1,S} {4,S}
#4 O  u0 p2 c0 {2,S} {3,S}
#""",
#    thermo=u'O-*O-*',
#    longDesc=u"""Is there really any way to do O*O* besides O-*O-* ?""",
#    metal = "Pt",
#    facet = "111",
#)

###Have not been able to find any examples of when N is triple bonded to the surface and
###has an R group attached.  Redid for no R group below. --EM
#entry(
#    index = 79,
#    label = "N#*R",
#    group =
#"""
#1 * X u0 c-1 {2,T}
#2 N  u0 c+1 {1,T} {3,S}
#3 R  u0 c0  {2,S}
#""",
#    thermo=u'N*',
#    metal = "Pt",
#    facet = "111",
#)

entry(
    index = 79,
    label = "N#X",
    group =
"""
1 * X u0 p0 {2,T}
2 N  u0 p1 {1,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-12.26, -9.29, -7.94, -7.48, -7.74, -8.48, -10.07], 'J/(mol*K)'),
        H298=(31.25, 'kJ/mol'),
        S298=(-173.48, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XN on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    N
   |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 80,
    label = "(CR3)X",
    group =
"""
1 * X  u0
2 C   u0 {3,D} {4,S} {5,S}
3 R!H u0 {2,D}
4 R   u0 {2,S}
5 R   u0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.54, 7.68, 8.34, 8.74, 9.14, 9.32, 9.44], 'J/(mol*K)'),
        H298=(-74.45, 'kJ/mol'),
        S298=(-130.43, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 81,
    label = "(CR2)X",
    group =
"""
1 * X  u0
2 C   u0 {3,T} {4,S}
3 R!H u0 {2,T}
4 R   u0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.69, 1.89, 2.02, 2.13, 2.46, 2.9, 3.96], 'J/(mol*K)'),
        H298=(-59.58, 'kJ/mol'),
        S298=(-115.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CHCHX and CHCCH3X on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  RC#CR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 82,
    label = "(NR2)X",
    group =
"""
1 * X u0 p0 c0
2 N   u0 p1 c0 {3,D} {4,S}
3 R!H u0 px c0 {2,D}
4 R   u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.54, 7.09, 7.44, 7.69, 8.0, 8.18, 8.34], 'J/(mol*K)'),
        H298=(-107.27, 'kJ/mol'),
        S298=(-122.2, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   R=N-R
     :
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 83,
    label = "N-XRN=X",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 N  u0 p1 c0 {1,S} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.59, 9.48, 11.84, 13.29, 14.69, 15.27, 15.84], 'J/(mol*K)'),
        H298=(-197.29, 'kJ/mol'),
        S298=(-196.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

  N-NR
  || |
***********
""",
    metal = "Pt",
    facet = "111",
)
entry(
    index = 84,
    label = "(CRCR)X",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,T} {4,S}
3 C  u0 p0 c0 {2,T} {5,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.69, 1.89, 2.02, 2.13, 2.46, 2.9, 3.96], 'J/(mol*K)'),
        H298=(-59.58, 'kJ/mol'),
        S298=(-115.19, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CHCHX and CHCCH3X on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

  RC#CR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 85,
    label = "C-XR2N=X",
    group =
"""
1 X u0 p0 c0 {3,S}
2 * X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.83, 8.7, 11.5, 13.11, 14.6, 15.19, 15.77], 'J/(mol*K)'),
        H298=(-224.09, 'kJ/mol'),
        S298=(-192.77, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XN single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
 R2C-N
   | ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 86,
    label = "C-XR2N-XR",
    group =
"""
1 X u0 p0 c0 {3,S}
2 * X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.98, 12.61, 15.79, 17.2, 17.95, 17.88, 17.39], 'J/(mol*K)'),
        H298=(-115.14, 'kJ/mol'),
        S298=(-198.77, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XNH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
R2C-NR
   | |
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 87,
    label = "C=X(=C)",
    group =
"""
1 * X u0  p0 c0 {2,D}
2 C  u0  p0 c0 {1,D} {3,D}
3 C  u0  p0 c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.94, 6.26, 8.08, 9.18, 10.4, 11.04, 11.77], 'J/(mol*K)'),
        H298=(-429.79, 'kJ/mol'),
        S298=(-168.79, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCCH2, XCCCH2, XCCO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   C
  ||
   C
  ||
***********

Because the C atom bonded to the surface only has one ligand
not two, it is not a child of the C=*R2 node
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 88,
    label = "C-XR2O-X",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([8.78, 13.6, 16.07, 17.2, 17.75, 17.62, 17.16], 'J/(mol*K)'),
        H298=(-61.03, 'kJ/mol'),
        S298=(-170.27, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XO single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

 R2C--O
   |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 89,
    label = "(CR2CR)X",
    group =
"""
1 * X u0 p0 c0
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {2,D} {6,S}
4 R  u0 px c0 {2,S}
5 R  u0 px c0 {2,S}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.43, 9.04, 9.92, 10.43, 10.9, 11.07, 11.17], 'J/(mol*K)'),
        H298=(-76.74, 'kJ/mol'),
        S298=(-143.86, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged CH2CH2X, CH3CHCH2X, CH2CCH2X on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
 R2C=CR
    :
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 90,
    label = "C=XRC-XR",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 C  u0 p0 c0 {2,S} {3,S} {6,D}
5 R  u0 px c0 {3,S}
6 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-5.37, 0.67, 4.68, 7.31, 10.25, 11.63, 12.69], 'J/(mol*K)'),
        H298=(-396.35, 'kJ/mol'),
        S298=(-202.17, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXCO double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
   RC---C=R
    ||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 91,
    label = "C#XC-XR",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,D}
5 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.41, 8.3, 11.6, 13.47, 15.23, 15.91, 16.41], 'J/(mol*K)'),
        H298=(-440.28, 'kJ/mol'),
        S298=(-204.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXCCH2 twice single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
     C---C=R
    |||  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 92,
    label = "C#XC-XR2",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 R  u0 px c0 {4,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.9, 4.58, 8.22, 10.59, 13.24, 14.53, 15.76], 'J/(mol*K)'),
        H298=(-436.46, 'kJ/mol'),
        S298=(-201.88, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCXCH2 and XCXCHCH3 on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
     C---CR2
    |||  |
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 93,
    label = "C-XR2C-XR",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {2,S} {3,S} {7,D}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {3,S}
7 R!H  u0 px c0 {4,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.18, 10.54, 13.14, 14.74, 16.34, 16.95, 17.2], 'J/(mol*K)'),
        H298=(-179.99, 'kJ/mol'),
        S298=(-191.92, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2CXCH2 single and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  R2C--C=R
    |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 95,
    label = "C-XRC-XR",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,D} {5,S}
4 C  u0 p0 c0 {2,S} {3,D} {6,S}
5 R  u0 px c0 {3,S}
6 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.8, 1.82, 4.66, 6.68, 9.21, 10.78, 13.11], 'J/(mol*K)'),
        H298=(-227.58, 'kJ/mol'),
        S298=(-194.29, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXCCH3 single and single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
 RC==CR
  |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 96,
    label = "C#XC=XR",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,T} {4,S}
4 C  u0 p0 c0 {2,D} {3,S} {5,S}
5 R  u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-2.0, 1.29, 3.27, 4.54, 5.97, 6.69, 7.48], 'J/(mol*K)'),
        H298=(-488.53, 'kJ/mol'),
        S298=(-158.38, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCXCCH3 triple and double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--CR
 ||| ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 97,
    label = "C=X=R-C-XR2",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,D} 
4 R!H  u0 px c0 {3,D} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-3.01, 2.84, 6.84, 9.5, 12.5, 13.99, 15.5], 'J/(mol*K)'),
        H298=(-543.25, 'kJ/mol'),
        S298=(-229.45, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCCHXCH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C=R--CR2
 ||    |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 98,
    label = "R2C-X-R-C-XR2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {3,S}
9 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-1.02, 3.61, 7.1, 9.67, 12.99, 14.82, 16.51], 'J/(mol*K)'),
        H298=(-389.14, 'kJ/mol'),
        S298=(-209.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2CH2XCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
 R2C--R--CR2
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 99,
    label = "RC=X-R=C-XR",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {7,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.06, -1.1, 2.74, 5.57, 9.12, 11.14, 13.63], 'J/(mol*K)'),
        H298=(-612.92, 'kJ/mol'),
        S298=(-200.99, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXCH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC--R==CR
  ||     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 100,
    label = "RC-X=R-C-XR2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 px c0 {3,D} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.12, 6.05, 9.54, 11.64, 13.78, 14.75, 15.73], 'J/(mol*K)'),
        H298=(-426.75, 'kJ/mol'),
        S298=(-227.78, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R--CR2
  |      |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 101,
    label = "RC=X-R-C-XR2",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
8 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-7.57, -2.61, 1.61, 4.87, 9.19, 11.68, 14.45], 'J/(mol*K)'),
        H298=(-529.03, 'kJ/mol'),
        S298=(-222.29, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCH2XCH2 single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC--R--CR2
  ||     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 102,
    label = "RC-X=R=C-XR",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 p0 c0 {3,D} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {7,S}
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.01, 7.65, 10.53, 12.32, 14.26, 15.17, 16.03], 'J/(mol*K)'),
        H298=(-370.79, 'kJ/mol'),
        S298=(-196.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCXCH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R==CR
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 103,
    label = "RC-X=R=C=X",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,D}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 p0 c0 {3,D} {5,D}
5 C  u0 p0 c0 {2,D} {4,D}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.81, 3.88, 6.24, 7.94, 10.04, 11.14, 12.17], 'J/(mol*K)'),
        H298=(-432.93, 'kJ/mol'),
        S298=(-179.15, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCXC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R==C
   |     ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 104,
    label = "O-X-C-O-X",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 C  u0 p0 c0 {3,S} {5,S}
5 O  u0 p2 c0 {2,S} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.33, 6.34, 8.03, 9.06, 10.2, 10.82, 11.57], 'J/(mol*K)'),
        H298=(-354.62, 'kJ/mol'),
        S298=(-179.72, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged OC(XO)XO and H2C(XO)XO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
   O--R--O
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 105,
    label = "RC-X=R-O-X",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,S} {4,D} {6,S}
4 R!H  u0 px c0 {3,D} {5,S}
5 O  u0 p2 c0 {2,S} {4,S}
6 R  u0 px c0 {3,S} 
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.77, 6.69, 9.4, 11.28, 13.55, 14.75, 15.95], 'J/(mol*K)'),
        H298=(-446.49, 'kJ/mol'),
        S298=(-211.15, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXO single and single -bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC==R--O
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 106,
    label = "C-XR2",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {3,D} {4,S}
3 R!H u0  px c0 {2,D}
4 R  u0  px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.32, 3.63, 5.87, 7.37, 9.08, 9.94, 10.77], 'J/(mol*K)'),
        H298=(-285.22, 'kJ/mol'),
        S298=(-171.81, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all children on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 107,
    label = "C=XRCR2",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 C  u0 p0 c0 {1,D} {2,S} {6,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
6 R  u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.82, 4.08, 6.24, 7.7, 9.5, 10.49, 11.57], 'J/(mol*K)'),
        H298=(-379.17, 'kJ/mol'),
        S298=(-179.05, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XCHCHCH2 and XCHCHO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
   |
   C-R
  ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 108,
    label = "C#XCR2",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 C  u0 p0 c0 {1,T} {2,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.45, 2.64, 4.89, 6.54, 8.67, 9.9, 11.29], 'J/(mol*K)'),
        H298=(-565.15, 'kJ/mol'),
        S298=(-180.28, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCCHCH2 and XCCHO triple-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
   |
   C
  |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 109,
    label = "O-XCR2",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,D}
3 O  u0 p2 c0 {1,S} {2,S}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([11.17, 13.37, 14.54, 15.21, 15.91, 16.23, 16.51], 'J/(mol*K)'),
        H298=(-228.04, 'kJ/mol'),
        S298=(-194.23, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged XOCHCH2, HOC(O)XO, HC(O)XO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 

   CR2
   |
   O
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 110,
    label = "CXRCX",
    group =
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,[S,D,T]}
3 C  u0 {1,[S,D,T]} {5,[S,D,T]}
4 C  u0 {2,[S,D,T]} {5,[S,D,T]}
5 R!H  u0 {3,[S,D,T]} {4,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([0.71, 5.77, 9.02, 11.15, 13.56, 14.75, 15.84], 'J/(mol*K)'),
        H298=(-461.69, 'kJ/mol'),
        S298=(-209.35, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all child nodes on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 111,
    label = "RXbridged-bidentate",
    group =
"""
1 * X  u0 {3,[S,D,T]}
2 X  u0 {4,[S,D,T]}
3 R!H ux {1,[S,D,T]} {5,[S,D,T]}
4 R!H ux {2,[S,D,T]} {5,[S,D,T]}
5 R!H ux {3,[S,D,T]} {4,[S,D,T]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.19, 5.91, 8.92, 10.88, 13.11, 14.22, 15.28], 'J/(mol*K)'),
        H298=(-446.4, 'kJ/mol'),
        S298=(-205.52, 'J/(mol*K)'),
    ),
    shortDesc=u"""Averaged from all child nodes on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 112,
    label = "CXROX",
    group =
"""
1 * X u0 {3,[S,D,T]}
2 X u0 {4,S}
3 C  u0 {1,[S,D,T]} {5,[S,D,T]}
4 O  u0 p2 {2,S} {5,S}
5 R!H  u0 px {3,[S,D,T]} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.77, 6.69, 9.4, 11.28, 13.55, 14.75, 15.95], 'J/(mol*K)'),
        H298=(-446.49, 'kJ/mol'),
        S298=(-211.15, 'J/(mol*K)'),
    ),
    shortDesc=u"""Same as child node RC-*=R-O-*""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 113,
    label = "OXROX",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 O  u0 p2 c0 {1,S} {5,S}
4 O  u0 p2 c0 {2,S} {5,S}
5 R!H  u0 px c0 {3,S} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.33, 6.34, 8.03, 9.06, 10.2, 10.82, 11.57], 'J/(mol*K)'),
        H298=(-354.62, 'kJ/mol'),
        S298=(-179.72, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged OC(XO)XO and H2C(XO)XO on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
   O--R--O
   |     |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 114,
    label = "C#X-R-C-XR2",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,T} {4,S} 
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6 R  u0 px c0 {5,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.53, 3.81, 6.89, 9.14, 12.06, 13.73, 15.5], 'J/(mol*K)'),
        H298=(-477.2, 'kJ/mol'),
        S298=(-200.61, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCCH2XCH2 double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R--CR2
 |||    |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 115,
    label = "C#X-R=C-XR",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,S}
3 C  u0 p0 c0 {1,T} {4,S} 
4 R!H  u0 px c0 {3,S} {5,D}
5 C  u0 p0 c0 {2,S} {4,D} {6,S} 
6 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([6.8, 11.4, 13.67, 14.88, 16.0, 16.45, 16.74], 'J/(mol*K)'),
        H298=(-402.33, 'kJ/mol'),
        S298=(-202.29, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCHXC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R==CR
 |||    |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 116,
    label = "C#X-R-C#X",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,T}
3 C  u0 p0 c0 {1,T} {4,S} 
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,T} {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-4.88, 4.76, 10.17, 13.18, 15.82, 16.67, 17.03], 'J/(mol*K)'),
        H298=(-671.16, 'kJ/mol'),
        S298=(-243.65, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCCH2XC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R--C
 |||   |||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 117,
    label = "RC=X-R-C=XR",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {5,D}
3 C  u0 p0 c0 {1,D} {4,S} {6,S}
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,D} {4,S} {7,S} 
6 R  u0 px c0 {3,S}
7 R  u0 px c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.9, 10.63, 13.33, 14.98, 16.74, 17.49, 17.8], 'J/(mol*K)'),
        H298=(-230.02, 'kJ/mol'),
        S298=(-203.94, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCH2XCH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  RC--R--CR
  ||     ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 118,
    label = "C#X-R-C=XR",
    group =
"""
1 * X u0 p0 c0 {3,T}
2 X u0 p0 c0 {5,D}
3 C  u0 p0 c0 {1,T} {4,S} 
4 R!H  u0 px c0 {3,S} {5,S}
5 C  u0 p0 c0 {2,D} {4,S} {6,S} 
6 R  u0 p0 c0 {5,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.0, 5.76, 9.53, 11.98, 14.68, 15.93, 16.88], 'J/(mol*K)'),
        H298=(-457.3, 'kJ/mol'),
        S298=(-222.49, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCH2XC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R--CR
 |||    ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 119,
    label = "C-XRN-X",
    group =
"""
1 X u0 p0 c0 {3,S}
2 * X u0 p0 c0 {5,S}
3 C u0 p0 c0 {1,S} {4,S} {5,D} 
4 R u0 px c0 {3,S}
5 N u0 p2 c0 {2,S} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.49, 2.78, 5.01, 6.52, 8.2, 8.9, 9.19], 'J/(mol*K)'),
        H298=(-107.62, 'kJ/mol'),
        S298=(-172.92, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXN double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
 
  RC=N
   | |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 120,
    label = "(OR)X",
    group =
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 R u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.0, 5.76, 9.53, 11.98, 14.68, 15.93, 16.88], 'J/(mol*K)'),
        H298=(-457.3, 'kJ/mol'),
        S298=(-222.49, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHCH2XC single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
  C--R--CR
 |||    ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 121,
    label = "(ONR)X",
    group =
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 R u0 px c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.71, 6.01, 6.79, 7.3, 7.93, 8.27, 8.56], 'J/(mol*K)'),
        H298=(-137.32, 'kJ/mol'),
        S298=(-141.39, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

    O=NR
     :
***********
""",
    metal = "Pt",
    facet = "111",
)


entry(
    index = 122,
    label = "(ONOR)X",
    group =
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 O u0 p2 c0 {3,S} {5,S}
5 R u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([2.76, 4.56, 5.74, 6.58, 7.69, 8.34, 8.89], 'J/(mol*K)'),
        H298=(-129.45, 'kJ/mol'),
        S298=(-144.39, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   O=N-O-R
     :
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 123,
    label = "(ONN)X",
    group =
"""
1 * X u0 p0 c0
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 N u0 p2 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.68, 6.73, 7.32, 7.66, 8.05, 8.24, 8.4], 'J/(mol*K)'),
        H298=(-141.25, 'kJ/mol'),
        S298=(-139.88, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
   O=N-NR2
     :
***********
""",
    metal = "Pt",
    facet = "111",
)


#entry(
#    index = 124,
#    label = "C#X-R-C=XR",
#    group =
#"""
#1 * X u0  p0 c0 {2,D}
#2 C u0 p0 c0 {1,D} {3,D}
#3 C u0 p0 c0 {2,D} {4,S} {5,S}
#4 R u0 px c0 {3,S}
#5 R u0 px c0 {3,S}
#""",
#    thermo=ThermoData(
#        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
#        Cpdata=([-0.0, 5.76, 9.53, 11.98, 14.68, 15.93, 16.88], 'J/(mol*K)'),
#        H298=(-457.3, 'kJ/mol'),
#        S298=(-222.49, 'J/(mol*K)'),
#    ),
#    shortDesc=u"""Came from XCHCH2XC single-bonded on Pt(111)""",
#    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
#            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
#            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
#            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
#            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
#            See Kreitz et al. 2023 (DOI:10.1021/acscatal.2c03378) for details on the DFT method. 
# # C--R--CR
# |||    ||
#***********
#""",
#    metal = "Pt",
#    facet = "111",
#)

entry(
    index = 125,
    label = "C-XRN-XR",
    group =
"""
1 X u0  p0 c0 {3,S}
2 * X u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,S} {4,S} {5,D}
4 N  u0  p1 c0 {2,S} {3,S} {6,S}
5 R!H u0 px c0 {3,D}
6 R u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.14, 10.45, 12.78, 14.38, 16.14, 16.88, 17.24], 'J/(mol*K)'),
        H298=(-125.07, 'kJ/mol'),
        S298=(-183.71, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   R== C--N-R
       |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 126,
    label = "C-XRO-X",
    group =
"""
1 * X u0  p0 c0 {3,S}
2 X u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,S} {4,S} {5,D}
4 O  u0  p2 c0 {2,S} {3,S}
5 R!H u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.82, 13.64, 15.48, 16.63, 17.68, 17.94, 17.72], 'J/(mol*K)'),
        H298=(-48.31, 'kJ/mol'),
        S298=(-174.32, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   R== C--O
       |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 127,
    label = "N[+]=XR[-]O-X",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 N  u0 p0 c+1 {1,D} {4,S} {5,S}
4 O  u0 p2 c0 {2,S} {3,S}
5 R u0 px c-1 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.73, 6.48, 7.79, 8.39, 8.75, 8.76, 8.6], 'J/(mol*K)'),
        H298=(-224.03, 'kJ/mol'),
        S298=(-147.24, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XOXNO single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

  R[-]--N[+]--O
        ||    |
*******************
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 128,
    label = "C-XRN",
    group =
"""
1 * X u0  p0 c0 {2,S}
2 C  u0  p0 c0 {1,S} {4,D} {3,S}
3 N  u0  p1 c0 {2,S}
4 R  u0  px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([1.32, 3.82, 5.36, 6.32, 7.28, 7.65, 7.96], 'J/(mol*K)'),
        H298=(-296.56, 'kJ/mol'),
        S298=(-153.59, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   NR2
   |
   C=R
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 129,
    label = "N=XC#R",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p1 c0 {1,D} {3,S}
3 C  u0 p0 c0 {2,S} {4,T}
4 R  u0 px c0 {3,T}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-6.99, -4.6, -3.58, -3.07, -2.45, -1.96, -1.14], 'J/(mol*K)'),
        H298=(-329.59, 'kJ/mol'),
        S298=(-142.03, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNCN double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Bjarne Kreitz at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Bjarne Kreitz from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=2.5e-2.
 R#C-N
     ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 130,
    label = "N-XRNR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 N  u0 p1 c0 {2,S} {5,D}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([10.9, 13.86, 15.44, 16.24, 16.8, 16.88, 16.78], 'J/(mol*K)'),
        H298=(-269.13, 'kJ/mol'),
        S298=(-189.56, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHNO single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R-N-NR
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 131,
    label = "N-XRCR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 C  u0 p0 c0 {2,S} {5,D}
4 R  u0 px c0 {2,S}
5 R!H  u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.99, 7.38, 9.54, 11.01, 12.78, 13.75, 14.96], 'J/(mol*K)'),
        H298=(-331.53, 'kJ/mol'),
        S298=(-216.91, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XNHCHO single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R-N-CR2
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 132,
    label = "N[+]=XR[-]R",
    group =
"""
1 * X u0 p0 c0 {2,D}
2 N  u0 p0 c+1 {1,D} {3,S} {4,S}
3 R!H  u0 px c-1 {2,S}
4 R  u0 px c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.73, 5.69, 6.78, 7.4, 8.0, 8.26, 8.45], 'J/(mol*K)'),
        H298=(-148.46, 'kJ/mol'),
        S298=(-147.01, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R-N[+]-R[-]
   ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 133,
    label = "N[+]-XR[-]R",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p0 c+1 {1,S} {3,S} {4,D}
3 R!H  u0 px c-1 {2,S}
4 R!H  u0 px c0 {2,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.22, 9.86, 11.24, 11.96, 12.51, 12.64, 12.64], 'J/(mol*K)'),
        H298=(-221.63, 'kJ/mol'),
        S298=(-163.34, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

 R=N-R[-]
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 134,
    label = "N-XCR",
    group =
"""
1 * X u0 p0 c0 {2,S}
2 N  u0 p1 c0 {1,S} {3,D}
3 C  u0 p0 c0 {2,D} {4,D}
4 R!H  u0 px c0 {3,D}
""",
  thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.42, 1.15, 1.86, 2.23, 2.65, 2.94, 3.41], 'J/(mol*K)'),
        H298=(-269.67, 'kJ/mol'),
        S298=(-145.42, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   CR
  ||
   N
   |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 135,
    label = "(NC)X",
    group =
"""
1 * X u0 p0 c0
2 N  u0 p1 c0 {3,S}
3 C  u0 p0 c0 {2,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.69, 6.03, 6.83, 7.33, 7.91, 8.22, 8.49], 'J/(mol*K)'),
        H298=(-98.68, 'kJ/mol'),
        S298=(-138.5, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
 
  R2N-CR2
     :            
***********
""",
    metal = "Pt",
    facet = "111",
)
entry(
    index = 136,
    label = "NXCX",
    group =
"""
1 * X u0 p0 c0 {3,[S,D,T]}
2 X u0 p0 c0 {4,[S,D]}
3 C u0 p0 c0 {1,[S,D,T]} {4,[S,D]}
4 N u0 p[0,1] c[0,+1] {2,[S,D]} {3,[S,D]}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.36, 9.29, 11.64, 13.06, 14.42, 14.92, 15.16], 'J/(mol*K)'),
        H298=(-201.39, 'kJ/mol'),
        S298=(-187.87, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 137,
    label = "inv(C=XRN=X)",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.05, 7.44, 9.68, 11.15, 12.68, 13.22, 13.32], 'J/(mol*K)'),
        H298=(-131.53, 'kJ/mol'),
        S298=(-176.43, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    R
    |
    C-N
   || ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 138,
    label = "inv(C-XR2N=X)",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,D}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,D} {3,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([3.83, 8.7, 11.5, 13.11, 14.6, 15.19, 15.77], 'J/(mol*K)'),
        H298=(-224.09, 'kJ/mol'),
        S298=(-192.77, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XN single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
 R2C-N
   | ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 139,
    label = "inv(C-XR2N-XR)",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 N  u0 p1 c0 {2,S} {3,S} {7,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {3,S}
7 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.98, 12.61, 15.79, 17.2, 17.95, 17.88, 17.39], 'J/(mol*K)'),
        H298=(-115.14, 'kJ/mol'),
        S298=(-198.77, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCH2XNH single-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
R2C-NR
   | |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 140,
    label = "inv(C=XRN-XR)",
    group =
"""
1 * X u0 p0 c0 {3,D}
2 X u0 p0 c0 {4,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 N  u0 p1 c0 {2,S} {3,S} {6,S}
5 R  u0 p0 c0 {3,S}
6 R  u0 p0 c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([4.85, 8.73, 11.16, 12.73, 14.43, 15.22, 15.97], 'J/(mol*K)'),
        H298=(-319.29, 'kJ/mol'),
        S298=(-194.68, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
    R
    |
    C-NR
   || |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 141,
    label = "inv(C-XRN-X)",
    group =
"""
1 * X u0 p0 c0 {3,S}
2 X u0 p0 c0 {5,S}
3 C u0 p0 c0 {1,S} {4,S} {5,D} 
4 R u0 px c0 {3,S}
5 N u0 p2 c0 {2,S} {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([-0.49, 2.78, 5.01, 6.52, 8.2, 8.9, 9.19], 'J/(mol*K)'),
        H298=(-107.62, 'kJ/mol'),
        S298=(-172.92, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from XCHXN double-bonded on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
 
  RC=N
   | |
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 142,
    label = "inv(C-XRN=X)",
    group =
"""
1 * X u0  p0 c0 {3,S}
2 X u0  p0 c0 {4,D}
3 C  u0  p0 c0 {1,S} {4,S} {5,D}
4 N  u0  p1 c0 {2,D} {3,S}
5 R!H u0 px c0 {3,D}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([5.84, 9.2, 10.96, 11.87, 12.58, 12.74, 12.69], 'J/(mol*K)'),
        H298=(-261.47, 'kJ/mol'),
        S298=(-188.76, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.
   R== C--N
       | ||
***********
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 143,
    label = "inv(C-XRN-XR)",
    group =
"""
1 * X u0  p0 c0 {3,S}
2 X u0  p0 c0 {4,S}
3 C  u0  p0 c0 {1,S} {4,S} {5,D}
4 N  u0  p1 c0 {2,S} {3,S} {6,S}
5 R!H u0 px c0 {3,D}
6 R u0 px c0 {4,S}
""",
    thermo=ThermoData(
        Tdata=([300, 400, 500, 600, 800, 1000, 1500], 'K'),
        Cpdata=([7.14, 10.45, 12.78, 14.38, 16.14, 16.88, 17.24], 'J/(mol*K)'),
        H298=(-125.07, 'kJ/mol'),
        S298=(-183.71, 'J/(mol*K)'),
    ),
    shortDesc=u"""Came from averaged on Pt(111)""",
    longDesc=u"""Calculated by Kirk Badger at Brown University using statistical mechanics (files: compute_NASA_for_Pt-adsorbates.ipynb and compute_NASA_for_Pt-gas_phase.ipynb).
            Based on DFT calculations by Kirk Badger from Brown University. DFT calculations were performed with Quantum Espresso
            using PAW pseudopotentials and the BEEF-vdW functional for an optimized 3x3 supercell (1/9ML coverage)
            following the procedure outlined by Blondal et al (DOI:10.1021/acs.iecr.9b01464). The following settings were applied:
            kpoints=(5x5x1), 4 layers (2 bottom layers fixed), ecutwfc=60 Ry, smearing='mazari-vanderbilt', mixing_mode='local-TF',fmax=1e-2.

   R== C--N-R
       |  |
***********
""",
    metal = "Pt",
    facet = "111",
)

tree(
"""
L1: RX
    L2: RXbridged-bidentate
        L3: CXRCX
            L4: C=X=R-C-XR2
            L4: R2C-X-R-C-XR2
            L4: RC=X-R=C-XR
            L4: RC-X=R-C-XR2
            L4: RC=X-R-C-XR2
            L4: RC-X=R=C-XR
            L4: RC-X=R=C=X
            L4: C#X-R-C-XR2
            L4: C#X-R=C-XR
            L4: C#X-R-C#X
            L4: RC=X-R-C=XR
            L4: C#X-R-C=XR
        L3: CXROX
            L4: RC-X=R-O-X
        L3: OXROX
            L4: O-X-C-O-X
    L2: RXbidentate
        L3: CXCX
            L4: C-XC-X
            L4: C=XRC=XR
            L4: C-XR2C-XR2
            L4: C-XR2C=XR
            L4: C-XRC=X
            L4: C=XRC-XR
            L4: C#XC-XR
            L4: C#XC-XR2
            L4: C#XC=XR
            L4: C-XR2C-XR
            L4: C-XRC-XR
	L3: NXCX
            L4: inv(C=XRN=X)
            L4: inv(C-XR2N=X)
            L4: inv(C-XR2N-XR)
            L4: inv(C=XRN-XR)
            L4: inv(C-XRN-X)
            L4: inv(C-XRN=X)
            L4: inv(C-XRN-XR)
        L3: CXNX
            L4: C=XRN=X
            L4: C-XR2N=X
            L4: C-XR2N-XR
            L4: C=XRN-XR
            L4: C-XRN-X
            L4: C-XRN=X
            L4: C-XRN-XR
        L3: CXOX
            L4: C=XRO-X
            L4: C-XR2O-X
            L4: C-XRO-X
        L3: NXNX
            L4: N-XRN-XR
            L4: N-XRN=X
        L3: NXOX
            L4: N-XRO-X
            L4: N[+]=XR[-]O-X
        L3: OXOX
    L2: RXsingle-chemisorbed
        L3: CX
            L4: CqX
            L4: C#XR
                L5: C#XCR3
                L5: C#XN
                L5: C#XOR
                L5: C#XCR2
            L4: C=XR2
                L5: C=XRCR3
                L5: C=XROR
                L5: C=XRN
                L5: C=XRCR2
            L4: C=X(=R)
                L5: C=X(=C)
                L5: C=X(=NR)
            L4: C-XR3
                L5: C-XR2CR3
                L5: C-XR2N
                L5: C-XR2OR
            L4: C-XR2
                L5: C-XRO
                L5: C-XRCR2
                L5: C-XRNR
                L5: C-XRN
        L3: NX
            L4: N#X
            L4: N=XR
                L5: N=XC-R
                L5: N=XN
                L5: N=XOR
                L5: N=XC#R
            L4: N-XR2
                L5: N-XRCR3
                L5: N-XRNR2
                L5: N-XROR
                L5: N-XRNR
                L5: N-XRCR
                L5: N[+]-XR[-]R
                L5: N[+]=XR[-]R

                
            L4: N-XR
                L5: N-XCR2
                L5: N-XNR
                L5: N-XCR
        L3: OX
            L4: O=X
            L4: O-XR
                L5: O-XCR3
                L5: O-XCR2
                L5: O-XN
                L5: O-XOR
    L2: RXvdW
        L3: (CR4)X
            L4: (CR3CR3)X
            L4: (CR3N)X
            L4: (CR3OR)X
        L3: (CR3)X
            L4: (CR2N)X
            L4: (CR2CR)X
            L4: (CR2O)X
        L3: (CR2)X
            L4: (CRN)X
            L4: (CRCR)X
        L3: (NR3)X
            L4: (NN)X
            L4: (NO)X
            L4: (NC)X
        L3: (NR2)X
            L4: (N=C)X
        L3: (OR2)X
            L4: (OROR)X
        L3: (OR)X
            L4: (ONR)X
                L5: (ONOR)X
                L5: (ONN)X
""",
)
