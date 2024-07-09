
from cc3d import CompuCellSetup
        

from CC3D_project1Steppables import CC3D_project1Steppable

CompuCellSetup.register_steppable(steppable=CC3D_project1Steppable(frequency=1))


CompuCellSetup.run()
