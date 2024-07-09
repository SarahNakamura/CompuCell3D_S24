from cc3d.core.PySteppables import *
import numpy as np



class ConstraintInitializerSteppable(SteppableBasePy):
    def __init__(self,frequency=1):
        SteppableBasePy.__init__(self,frequency)

    def start(self):
        cx,cy = 256,256

        for cell in self.cell_list:
            xcom,ycom = cell.xCOM, cell.yCOM
            
            dist_from_center = np.sqrt((cx-xcom)**2 + (cy-ycom)**2)
            if dist_from_center > 80:
                cell.type = 3
            elif dist_from_center > 30:
                    cell.type = 2
            else:
                    cell.type = 1

            cell.targetVolume = cell.volume
            cell.lambdaVolume = 2.0
            cell.targetSurface = cell.surface
            cell.lambdaSurface = 2.0
         
        
        
class GrowthSteppable(SteppableBasePy):
    def __init__(self,frequency=1):
        SteppableBasePy.__init__(self, frequency)

    def step(self, mcs):
    
        for cell in self.cell_list_by_type(self.A):
            cell.targetVolume += 0.1       

        # # alternatively if you want to make growth a function of chemical concentration uncomment lines below and comment lines above        

        # field = self.field.CHEMICAL_FIELD_NAME
        
        # for cell in self.cell_list:
            # concentrationAtCOM = field[int(cell.xCOM), int(cell.yCOM), int(cell.zCOM)]

            # # you can use here any fcn of concentrationAtCOM
            # cell.targetVolume += 0.01 * concentrationAtCOM       

        
class MitosisSteppable(MitosisSteppableBase):
    def __init__(self,frequency=1):
        MitosisSteppableBase.__init__(self,frequency)

    def step(self, mcs):
        
        p_kill = 0.8 #macrophage killing the tumor cell

        cells_to_divide=[]
        try:
            for cell in self.cell_list_by_type(self.A):
                for cnbr,csa in self.get_cell_neighbor_data_list(cell):
                    if cnbr.type == 3:
                        if np.random.rand() < p_kill:
                            cell.targetVolume = 0
                            cell.lambdaVolume = 2
                        else:
                            cnbr.targetVolume = 0
                            cnbr.lambdaVolume = 2
                
                    
                if cell.volume>600:
                    cells_to_divide.append(cell)
        except:
            print('NonType Found!')

        for cell in cells_to_divide:

            self.divide_cell_random_orientation(cell)
            # Other valid options
            # self.divide_cell_orientation_vector_based(cell,1,1,0)
            # self.divide_cell_along_major_axis(cell)
            self.divide_cell_along_minor_axis(cell)

    def update_attributes(self):
        # reducing parent target volume
        self.parent_cell.targetVolume /= 2.0                  

        self.clone_parent_2_child()            

        # for more control of what gets copied from parent to child use cloneAttributes function
        # self.clone_attributes(source_cell=self.parent_cell, target_cell=self.child_cell, no_clone_key_dict_list=[attrib1, attrib2]) 
        
        # if self.parent_cell.type==1:
            # self.child_cell.type=2
        # else:
            # self.child_cell.type=1

        
# class DeathSteppable(SteppableBasePy):
    # def __init__(self, frequency=1):
        # SteppableBasePy.__init__(self, frequency)

    # def step(self, mcs):
        # if mcs == 1000:
            # for cell in self.cell_list:
                # if cell.type==1:
                    # cell.targetVolume=0
                    # cell.lambdaVolume=100

        