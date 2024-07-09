from cc3d.core.PySteppables import *
import numpy as np

class Tumor2D_part_1Steppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        """
        Called before MCS=0 while building the initial simulation
        """
        
        for cell in self.cell_list:
            cell.targetVolume = cell.volume
            cell.lambdaVolume = 2
            cell.targetSurface = 2*np.pi*np.sqrt(cell.volume/np.pi)
            cell.lambdaSuface = 1.0
            
            for cnbr,csa in self.get_cell_neighbor_data_list(cell):
                try:
                    print(nbr.id)
                except:
                    print('oops')
        #---------------------------------------------------#
        

    def step(self, mcs):
        """
        Called every frequency MCS while executing the simulation
        
        :param mcs: current Monte Carlo step
        """

        for cell in self.cell_list:

            print("cell.id=",cell.id)
        # for nbr,csa in self.get_cell_neighbor_data_list(self.fetch_cell_by_id(30)):
                # nbr.type = 3
        # for nbr,csa in self.get_cell_neighbor_data_list(self.fetch_cell_by_id(30)):
            # nbr.targetVolume = 25
            # nbr.lambdaVolume = 2
        # for nbr,csa in self.get_cell_neighbor_data_list(self.fetch_cell_by_id(30)):
            # try:
                # nbr.lambdaVolume = 0
            # except:
                # print('oops')
        # for nbr,csa in self.get_cell_neighbor_data_list(self.fetch_cell_by_id(30)):
            # nbr.targetVolume += 1
        
        

    def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """

    def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS
        """
