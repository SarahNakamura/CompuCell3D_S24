from cc3d.core.PySteppables import *
import numpy as np

class CellTrainNarrowSteppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)
        
    def create_circular_cell(self,cx,cy,radius,cellType):
        rad_square = radius**2
        cell1 = self.newCell(eval('self.'+cellType))
        x_min, x_max = cx - radius, cx + radius
        y_min, y_max = cy - radius, cy + radius

        for i in range(x_min,x_max):
            for j in range(y_min,y_max):
                dist_square = (cx-i)**2 + (cy-j)**2
                if dist_square <= rad_square:
                    self.cellField[j,i,0] = cell1
     
        # cell1.targetVolume = cell1.volume
        # cell1.targetSurface = cell1.surface
        # cell1.lamdaVolume = 2
        # cell1.lambdaSurface = 2
        return cell1

    def start(self):
        """
        Called before MCS=0 while building the initial simulation
        """
        cell1 = self.create_circular_cell(60,20,15,'B')
        cell2 = self.create_circular_cell(60,20,5,'N')
        cell3 = self.create_circular_cell(60,50,15,'B')
        cell4 = self.create_circular_cell(60,50,5,'N')
        
        cell1.targetVolume = cell1.volume
        cell1.lambdaVolume  = 2
        cell2.targetVolume = cell2.volume
        cell2.lambdaVolume  = 5
        cell3.targetVolume = cell3.volume
        cell3.lambdaVolume  = 2
        cell4.targetVolume = cell4.volume
        cell4.lambdaVolume  = 5       
        
        self.reassign_cluster_id(cell1, 1)
        self.reassign_cluster_id(cell2, 1)
        self.reassign_cluster_id(cell3, 2)
        self.reassign_cluster_id(cell4, 2)
        
        cell1.targetSurface = cell1.surface
        cell1.lambdaSurface  = 10
        cell2.targetSurface = 2*np.pi*((cell2.volume/np.pi)**(1/2))
        cell2.lambdaSurface  = 10
        cell3.targetSurface = cell3.surface
        cell3.lambdaSurface  = 10
        cell4.targetSurface = 2*np.pi*((cell4.volume/np.pi)**(1/2))
        cell4.lambdaSurface  = 10

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
