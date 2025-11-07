from typing import Tuple, List

from Pendulum import Pendulum
from equation import derivative,solve_ode
from scipy import constants
import numpy as np
import pandas as pd

class DoublePendulum:
    """
    Model double pendulum
    """
    tmax = 30.0
    dt = .05
    t = np.arange(0,tmax+dt,dt)
    def __init__(self, L1: int = 1, L2: int = 1, 
                 m1: int = 1 ,m2: int = 1,
                 y0: List[int] = None, 
                 g: float = -1*constants.g) -> None:
        if y0 is None:
            y0 = [90, 0, -10, 0]
        self.pendulum1 = Pendulum(L1, m1)
        self.pendulum2 = Pendulum(L2, m2)
        self.y0 = np.array(np.radians(y0))
        self.g = g


        self._calculate_system()

        self.max_length = self.pendulum1.L + self.pendulum2.L


    def get_frame_x(self, i:int) -> Tuple[int]:
        return (0,self.pendulum1.x[i], self.pendulum2.x[i])
    
    
    def get_frame_y(self, i:int) -> Tuple[int]:
        return (0,self.pendulum1.y[i], self.pendulum2.y[i])
    
    
    def get_frame_coordinates(self, i: int) -> Tuple[Tuple[int]]:
        return (self.get_frame_x(i),self.get_frame_y(i))
    

    def get_max_x(self, i:int) -> float:
        return self.pendulum2.get_max_x()
    

    def get_max_y(self, i:int) -> float:
        return self.pendulum2.get_max_y()
    

    def get_max_coordinates(self) -> float:
        return self.pendulum2.get_max_coordinates()
    
    # membuat bandul
    @classmethod
    def create_double_pendula(cls,num_pendula: int = 1,
                              L1: float = 1.0,
                              L2: float = 1.0,
                              m1: float = 1.0,
                              m2: float = 1.0,
                              intial_theta: float = 90,
                              dtheta: float = .05) -> List["DoublePendulum"]:
        pendula = []
        for _ in range(num_pendula):
            double_pendula = cls(
                L1 = L1,
                L2 = L2,
                m1 = m1,
                m2 = m2,
                y0 = [intial_theta, 0,-10,0]
            )
            pendula.append(double_pendula)

            
        return pendula



    def _calculate_system(self) -> None:
        self.y = solve_ode(
            derivative,
            self.y0,
            self.t,
            self.g,
            self.pendulum1,
            self.pendulum2
        )

        self.pendulum1.calcu_path(
            theta=self.y[:, 0],
            dtheta=self.y[:, 1]
        )

        self.pendulum2.calcu_path(
            theta=self.y[:, 2],
            dtheta=self.y[:, 3],
            x0=self.pendulum1.x,
            y0=self.pendulum1.y
        )
    
        self.w = self.y[:, 1]
        self.df = pd.DataFrame(
            self.y,
            columns = ["theta1","dtheta1","theta2","dtheta2"]
        )
        
    def __repr__(self):
        return f"< DoublePendulum: L1={self.pendulum1.L} m1={self.pendulum1.m} L2={self.pendulum2.L} m2={self.pendulum2.m} y0={self.y0} >"



