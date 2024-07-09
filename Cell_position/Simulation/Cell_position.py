
from cc3d import CompuCellSetup
        

from Cell_positionSteppables import Cell_positionSteppable

CompuCellSetup.register_steppable(steppable=Cell_positionSteppable(frequency=1))


CompuCellSetup.run()
