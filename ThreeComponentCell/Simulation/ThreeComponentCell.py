
from cc3d import CompuCellSetup
        

from ThreeComponentCellSteppables import ThreeComponentCellSteppable

CompuCellSetup.register_steppable(steppable=ThreeComponentCellSteppable(frequency=1))


CompuCellSetup.run()
