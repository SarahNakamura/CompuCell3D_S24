
from cc3d import CompuCellSetup
        

from CellTrainNarrowSteppables import CellTrainNarrowSteppable

CompuCellSetup.register_steppable(steppable=CellTrainNarrowSteppable(frequency=1))


CompuCellSetup.run()
