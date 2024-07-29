
from cc3d import CompuCellSetup
        

from BorderCells_v2Steppables import BorderCells_AF_1Steppable



CompuCellSetup.register_steppable(steppable=BorderCells_AF_1Steppable(frequency=1))


CompuCellSetup.run()
