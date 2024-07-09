
from cc3d import CompuCellSetup
        

from Chemotaxis_1Steppables import Chemotaxis_1Steppable

CompuCellSetup.register_steppable(steppable=Chemotaxis_1Steppable(frequency=1))


CompuCellSetup.run()
