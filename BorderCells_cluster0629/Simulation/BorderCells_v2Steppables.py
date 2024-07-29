from cc3d.core.PySteppables import *
import numpy as np
from random import uniform

class BorderCells_AF_1Steppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)
        
    
    def create_BC_PC_cluster(self,x0,y0,R1,R2):
        eps = 1e-10
        
        lambdaS = 2.5
        lambdaV = 2.0
        lambdaS_pc = 2.5
        
        bc1  = self.newCell(self.BC)
        bc2 =  self.newCell(self.BC)
        bc3  = self.newCell(self.BC)
        bc4 =  self.newCell(self.BC)
        bc5  = self.newCell(self.BC)
        bc6 =  self.newCell(self.BC)
        BCList = [bc1,bc2,bc3,bc4,bc5,bc6]
        
        pc1 = self.newCell(self.PC)
        pc2 = self.newCell(self.PC)
        
        nc1  = self.newCell(self.NC)
        nc2 =  self.newCell(self.NC)
        
        self.cellField[0:1000,150:300,0] = nc1
        self.cellField[0:1000,0:150,0]   = nc2
        
        
        for i in range(x0-R1,x0+R1):
            for j in range(y0-R1,y0+R1):
                d = np.sqrt((j-y0)**2 + (i-x0)**2)
                if d < R1:
                    theta = np.arctan2((j-y0),(i-x0)) + np.pi
                    idx = int(np.ceil((theta * 3)/np.pi))
                    self.cellField[i,j,0] = BCList[idx-1]
                   
        
        
        for i in range(x0-R2,x0+R2):
            for j in range(y0-R2,y0+R2):
                d = np.sqrt((j-y0)**2 + (i-x0)**2)
                if d < R2:
                    if i < x0:
                        self.cellField[i,j,0] = pc1
                        
                    else:
                        self.cellField[i,j,0] = pc2
                        
         

        for cell in BCList + [nc1,nc2]:
            cell.targetVolume = cell.volume 
            cell.targetSurface = cell.surface
            cell.lambdaVolume  = lambdaV
            cell.lambdaSurface = lambdaS
       
        for cell in [pc1,pc2]:
            cell.targetVolume = cell.volume 
            cell.targetSurface = cell.surface
            cell.lambdaVolume  = lambdaV
            cell.lambdaSurface = lambdaS_pc
       
    def ecad_adhesion_2(self):
        #-----------implementing gain and loss of adhesion overtime on ECad-----------#
        # constant value of adhesion increase on ECad
        omega = 0.05 

        alpha = 0.2
        alpha_BC = 0.5
        alpha_NC = 0.0005
        beta = 0.02
        beta_BC = 0.01
        beta_NC = 0.001
        gamma = 0.01
        gamma_BC = 0.01
        gamma_NC = 0.01
        molden_PCi = 0
        molden_PCj = 0
        molden_BCi = 0
        molden_BCj = 0
        molden_NCi = 0
        molden_NCj = 0
        
        for cell in self.cell_list:
            if cell.type == self.PC:
                total_ECad_adhesion_ij = 0
                celli_surface = cell.surface
                for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                    molden_PCi = self.adhesionFlexPlugin.getAdhesionMoleculeDensity(cell,"ECad")
                    if neighbor:
                        molden_PCj = self.adhesionFlexPlugin.getAdhesionMoleculeDensity(neighbor,"ECad")
                        print(f'PC_i{molden_PCi}')
                        print(f'PC_j{molden_PCj}')
                        area_ij = common_surface_area
                        ECad_adhesion_ij = area_ij*molden_PCj
                    
                    else:
                        ECad_adhesion_ij = 0
                        pass
                    total_ECad_adhesion_ij += ECad_adhesion_ij
                    print(f'PC_total_ECad_adhesion_ij:{total_ECad_adhesion_ij}')
                    print(f'PC_celli_surface: {celli_surface}')
                molden_new = molden_PCi + alpha - gamma*molden_PCi - beta*molden_PCi/celli_surface*total_ECad_adhesion_ij
                molden_PCi = self.adhesionFlexPlugin.setAdhesionMoleculeDensity(cell,"ECad",molden_new)
                print(f'PC_cell_id:{cell.id},molden_new: {molden_new}')

        # for cell in self.cell_list_by_type(self.BC):
            elif cell.type == self.BC:
                total_ECad_adhesion_ij = 0
                celli_surface = cell.surface
                for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                    molden_BCi = self.adhesionFlexPlugin.getAdhesionMoleculeDensity(cell,"ECad")
                    if neighbor:
                        molden_BCj = self.adhesionFlexPlugin.getAdhesionMoleculeDensity(neighbor,"ECad")
                        print(f'BC_i{molden_BCi}')
                        print(f'BC_j{molden_BCj}')
                        area_ij = common_surface_area
                        ECad_adhesion_ij = area_ij*molden_BCj
                    
                    else:
                        ECad_adhesion_ij = 0
                        pass
                    total_ECad_adhesion_ij += ECad_adhesion_ij
                    print(f'BC_total_ECad_adhesion_ij:{total_ECad_adhesion_ij}')
                    print(f'BC_celli_surface: {celli_surface}')
                molden_new = molden_BCi + alpha_BC - gamma_BC*molden_BCi - beta_BC*molden_BCi/celli_surface*total_ECad_adhesion_ij
                molden_BCi = self.adhesionFlexPlugin.setAdhesionMoleculeDensity(cell,"ECad",molden_new)
                print(f'BC_cell_id:{cell.id},molden_new: {molden_new}')

            elif cell.type == self.NC:
                total_ECad_adhesion_ij = 0
                celli_surface = cell.surface
                for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                    molden_NCi = self.adhesionFlexPlugin.getAdhesionMoleculeDensity(cell,"ECad")
                    if neighbor:
                        molden_NCj = self.adhesionFlexPlugin.getAdhesionMoleculeDensity(neighbor,"ECad")
                        print(f'NC_i{molden_NCi}')
                        print(f'NC_j{molden_NCj}')
                        area_ij = common_surface_area
                        ECad_adhesion_ij = area_ij*molden_NCj
                    
                    else:
                        ECad_adhesion_ij = 0
                        pass
                    total_ECad_adhesion_ij += ECad_adhesion_ij
                    print(f'BC_total_ECad_adhesion_ij:{total_ECad_adhesion_ij}')
                    print(f'BC_celli_surface: {celli_surface}')
                molden_new = molden_NCi + alpha_NC - gamma_NC*molden_NCi - beta_NC*molden_NCi/celli_surface*total_ECad_adhesion_ij
                molden_NCi = self.adhesionFlexPlugin.setAdhesionMoleculeDensity(cell,"ECad",molden_new)
                print(f'NC_cell_id:{cell.id},molden_new: {molden_new}')
      
    
    def start(self):
        """
        Called before MCS=0 while building the initial simulation
        """
        self.create_BC_PC_cluster(100,150,40,20)
        
        
        
        
    def step(self, mcs):
        """
        Called every frequency MCS while executing the simulation
        
        :param mcs: current Monte Carlo step
        """
        
        if mcs == 100:
            for cell in self.cell_list_by_type(self.BC):
                print('cell type = ',cell.type)
                cd = self.chemotaxisPlugin.addChemotaxisData(cell, "ATTR")
                cd.setLambda(100.0)
        
        self.ecad_adhesion_2()

    #--------------------------------------------------------------------#
        

    def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """

    def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS
        """
