
from cc3d import CompuCellSetup
        

from ThreeComponentCell_2Steppables import ThreeComponentCell_2Steppable

CompuCellSetup.register_steppable(steppable=ThreeComponentCell_2Steppable(frequency=1))


CompuCellSetup.run()
