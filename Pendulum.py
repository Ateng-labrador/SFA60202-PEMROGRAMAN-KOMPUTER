from typing import Tuple

from scipy import constants
import numpy as np
import pandas as pd


class Pendulum:
    """

    Kerangka dasar untuk membuat pendulum

    Untuk membuat kerangka pendulum yang mempunyai
    atribut panjang L dan massa m


    Atribut penting
    -> self.L, self.m -> panjang dan massa
    -> self.theta, self.dtheta -> array sudut dan kecepatan sudut
    -> self.x, self.y -> posisi ujung bandul sepanjang waktu

    metode:
    calculate_path : menghitung lintasan koordinat
    dari bandul berdasarkan sudut dan perubahan

    get_max : mengambil nilai maksimum dari posisi x
    dan y bandul

    """
    def __init__(self, L: float = 1.0,
                 m: float = 1.0) -> None:
        self.L = L
        self.m = m
    
    def calcu_path(self,
                   theta: float,
                   dtheta: float,
                   x0: float = 0,
                   y0: float = 0) -> None:
        """
        Menghitung jalur untuk membuat sebuah pendulum

        menerima array theta dan dtheta,menghitung
        posisi bandul
        """
        self.theta = theta
        self.dtheta = dtheta
        # parameter awal
        # x = x_0 + L*sin(theta)
        # y = y_0 + L*cos(theta)
        self.x = self.L*np.sin(self.theta) + x0
        self.y = self.L*np.cos(self.theta) + y0
        self.df = {
            "theta": self.theta,
            "dtheta": self.dtheta,
            "x": self.x,
            "y": self.y
        }

    """
    Mengambil nilai maksimum diambil untuk menentukan batas plotting
    """
    
    def get_max_x(self) -> float:
        """
        Mengambil nilai maksmum x
        """
        return float(np.abs(max(self.x)))
    
    
    def get_max_y(self) -> float:
        """
        Mengambil nilai maksimum y
        """
        return float(np.abs(max(self.y)))
    

    def get_max_coordinates(self) -> Tuple[float,float]:
        """
        Mengambil nilai maksimum semua nilai max
        """
        return (self.get_max_x(),self.get_max_y())
    
   


