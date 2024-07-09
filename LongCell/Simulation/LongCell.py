
from cc3d import CompuCellSetup
        

from LongCellSteppables import LongCellSteppable

CompuCellSetup.register_steppable(steppable=LongCellSteppable(frequency=1))


CompuCellSetup.run()
