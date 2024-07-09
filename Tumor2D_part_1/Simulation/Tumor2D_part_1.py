
from cc3d import CompuCellSetup
        

from Tumor2D_part_1Steppables import Tumor2D_part_1Steppable

CompuCellSetup.register_steppable(steppable=Tumor2D_part_1Steppable(frequency=1))


CompuCellSetup.run()
