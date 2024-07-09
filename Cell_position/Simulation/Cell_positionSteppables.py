from cc3d.core.PySteppables import *
import numpy as np
import pandas as pd

class Cell_positionSteppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        """
        Called before MCS=0 while building the initial simulation
        """
        
        
        cell1 = self.newCell(self.A)
        cell2 = self.newCell(self.A)
        cell3 = self.newCell(self.A)
        cell4 = self.newCell(self.A)
        self.cellField[17:37,20:40,80:100] = cell1
        cell1.targetVolume = cell1.volume
        cell1.lambdaVolume = 2
        
        # self.cellField[110:120,45:55,50:60] = cell2
        # cell2.targetVolume = cell2.volume
        # cell2.lambdaVolume = 2
        
        # self.cellField[165:195,130:160,25:45] = cell3
        # cell3.targetVolume = cell3.volume
        # cell3.lambdaVolume = 2
        
        # self.cellField[180:240,170:250,60:90] = cell4
        # cell1.targetVolume = cell4.volume
        # cell1.lambdaVolume = 2
        
        #------------------------------------------------------------#
        self.PositionDict={'t':[],'cellID':[],'xCOM':[],'yCOM':[],'zCOM':[]}

    def step(self, mcs):
        """
        Called every frequency MCS while executing the simulation
        
        :param mcs: current Monte Carlo step
        """
        for cell in self.cell_list:
            cid,xcom,ycom,zcom = cell.id,cell.xCOM,cell.yCOM,cell.zCOM
            self.PositionDict['t'].append(mcs)
            self.PositionDict['cellID'].append(cid)
            self.PositionDict['xCOM'].append(xcom)
            self.PositionDict['yCOM'].append(ycom)
            self.PositionDict['zCOM'].append(zcom)

            print("cell.id=",cell.id)

    def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """
        df = pd.DataFrame(self.PositionDict)
        df.to_csv('~/Desktop/Cell_Position_3D.csv')

    def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS
        """
