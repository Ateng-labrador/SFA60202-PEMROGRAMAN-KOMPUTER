# https://en.wikipedia.org/wiki/Double_pendulum
import string
from typing import List

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


from source.double_pendulum import DoublePendulum

def animate(i):
    """
    Melakukan pembuatan animasi
    """
    time_template = 'time = %.1fs'
    dt = .05
    tail_length = 15
    return_arr = []
    for double_pendulum,ax_data in pendula_axes:
        _, line, tail_line, time_text= ax_data
        frame_x, frame_y = double_pendulum.get_frame_coordinates(i)
        # garis utama 
        line.set_data(frame_x, frame_y)
        # membuat jejak pada ujung bandul
        start = max(0,i - tail_length + 1)
        trail_x = []
        trail_y = []
        for j in range(start, i + 1):
             fx, fy = double_pendulum.get_frame_coordinates(j)

             trail_x.append(fx[-1])
             trail_y.append(fy[-1])
        tail_line.set_data(trail_x , trail_y)

        time_text.set_text(time_template % (dt*i))
        return_arr.extend([
            line,
            tail_line,
            time_text,
        ])
    return return_arr

def create_axes(
        fig: "matplotlib.figure.Fugure",
        pendula: list["DoublePendulum"],
    ) -> List["matplotlib.axes._subplots.AxesSubplot"]:
    """
    Pembuatan sumbu dan jejak pada bandul
    """
    axes = []
    longest_double_pendulum = max(pendula, key=lambda x: x.max_length)
    for i in range(len(pendula)):
        color = f'#FF0000'
        ax = _create_individual_axis(
            longest_double_pendulum=longest_double_pendulum,
            fig=fig,
            i=i
        )
        # garis utama
        line, = ax.plot([],[], 'o-',lw=2,color = color)
        # garis jejak pada bandul ke dua
        tail_line, = ax.plot([],[],'-',lw=1,color=color, alpha=0.6)
        time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
        axes.append((ax,line,tail_line,time_text))
    return axes

def _create_individual_axis(
            longest_double_pendulum: "DoublePendulum",
            fig: "matplotlib.figure.Figure",
            i: int
        ) -> None:
        """
        Pembuatan grid
        """
        ax = fig.add_subplot(
            111,
            autoscale_on = False,
            xlim = (
                -longest_double_pendulum.max_length,
                longest_double_pendulum.max_length
            ),
            ylim = (
                -longest_double_pendulum.max_length,
                longest_double_pendulum.max_length
            ),
        )
        ax.set_aspect('equal')
        ax.grid()
        return ax

if __name__ == "__main__":
    fig = plt.figure()
    pendula = DoublePendulum.create_double_pendula(num_pendula = 1)
    axes = create_axes(fig=fig,pendula=pendula)
    pendula_axes = list(zip(pendula, axes))

    ani = animation.FuncAnimation(
        fig,
        animate,
        np.arange(1, len(pendula[0].y)),
        interval = 25,
        blit = True
    )
    plt.show()

