
from cc3d import CompuCellSetup
        

from CellTrainSteppables import CellTrainSteppable

CompuCellSetup.register_steppable(steppable=CellTrainSteppable(frequency=1))


CompuCellSetup.run()
