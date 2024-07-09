from cc3d.core.PySteppables import *
import numpy as np

class LongCellSteppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        """
        Called before MCS=0 while building the initial simulation
        """
        L = 20
        cell1 = self.newCell(self.E)
        cell2 = self.newCell(self.B)
        cell3 = self.newCell(self.N)
        cell4 = self.newCell(self.B)
        cell5 = self.newCell(self.E)
        
        self.cellField[30:30+L,30:30+L,0] = cell1
        self.cellField[30+L:30+2*L,30:30+L,0] = cell2
        self.cellField[30+2*L:30+3*L,30:30+L,0] = cell3
        self.cellField[30+3*L:30+4*L,30:30+L,0] = cell4
        self.cellField[30+4*L:30+5*L,30:30+L,0] = cell5
        cell1.targetVolume = cell1.volume
        cell1.lambdaVolume  = 2
        cell2.targetVolume = cell2.volume
        cell2.lambdaVolume  = 2
        cell3.targetVolume = cell3.volume
        cell3.lambdaVolume  = 2
        cell4.targetVolume = cell4.volume
        cell4.lambdaVolume  = 2
        cell5.targetVolume = cell5.volume
        cell5.lambdaVolume  = 2
        
        self.reassign_cluster_id(cell1, 1)
        self.reassign_cluster_id(cell2, 1)
        self.reassign_cluster_id(cell3, 1)
        self.reassign_cluster_id(cell4, 1)
        self.reassign_cluster_id(cell5, 1)
        
        cell1.targetSurface = 4*L
        cell1.lambdaSurface  = 2
        cell2.targetSurface = 4*L
        cell2.lambdaSurface  = 2
        cell3.targetSurface = 4*L
        cell3.lambdaSurface  = 2
        cell4.targetSurface = 4*L
        cell4.lambdaSurface  = 2
        cell5.targetSurface = 4*L
        cell5.lambdaSurface  = 2
        
        cell6 = self.newCell(self.E)
        cell7 = self.newCell(self.B)
        cell8 = self.newCell(self.N)
        cell9 = self.newCell(self.B)
        cell10 = self.newCell(self.E)
        
        self.cellField[30:30+L,55:55+L,0] = cell6
        self.cellField[30+L:30+2*L,55:55+L,0] = cell7
        self.cellField[30+2*L:30+3*L,55:55+L,0] = cell8
        self.cellField[30+3*L:30+4*L,55:55+L,0] = cell9
        self.cellField[30+4*L:30+5*L,55:55+L,0] = cell10
        cell6.targetVolume = cell6.volume
        cell6.lambdaVolume  = 2
        cell7.targetVolume = cell7.volume
        cell7.lambdaVolume  = 2
        cell8.targetVolume = cell8.volume
        cell8.lambdaVolume  = 2
        cell9.targetVolume = cell9.volume
        cell9.lambdaVolume  = 2
        cell10.targetVolume = cell10.volume
        cell10.lambdaVolume  = 2
        
        self.reassign_cluster_id(cell6, 2)
        self.reassign_cluster_id(cell7, 2)
        self.reassign_cluster_id(cell8, 2)
        self.reassign_cluster_id(cell9, 2)
        self.reassign_cluster_id(cell10, 2)
        
        cell6.targetSurface = 4*L
        cell6.lambdaSurface  = 2
        cell7.targetSurface = 4*L
        cell7.lambdaSurface  = 2
        cell8.targetSurface = 4*L
        cell8.lambdaSurface  = 2
        cell9.targetSurface = 4*L
        cell9.lambdaSurface  = 2
        cell10.targetSurface = 4*L
        cell10.lambdaSurface  = 2
        


    def step(self, mcs):
        """
        Called every frequency MCS while executing the simulation
        
        :param mcs: current Monte Carlo step
        """

        for cell in self.cell_list:

            print("cell.id=",cell.id)

    def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """

    def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS
        """
