import json
import warnings
from matplotlib import pyplot as plt
from src.super_curves.SuperStyle import superman, ironman


class Curve:

    def __init__(self, title, xlabel, ylabel, labels, vlabels=None):
        '''
        :param title: Graph Title
        :param xlabel: x axis label
        :param ylabel: y axis label
        :param labels: show labels
        :param vlabels: vertical labels
        '''

        self.title = title
        self.labels = labels
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.vlabel = vlabels
        self.crv_style = '-'  # default style
        self.superstyle = "superman"
        self.file = open('src/super_curves/data/colors.json', 'r')
        self.colors = json.load(self.file)

        # Super style applied
        self.SP = None

    def curve_style(self, superstyle, crv_style=None):
        '''
        :superstyle: define the global style of the graph (superman/ironman)
        By default: superstyle is superman
        :crv_style: define how curves must be draw (solid/dashed...)
        By default: crv_style are solid
        '''

        if crv_style is not None:
            self.crv_style = crv_style

        del self.SP
        plt.rcParams.update(plt.rcParamsDefault)
        if superstyle == "superman":
            self.superstyle = "superman"
            self.SP = superman.Superman(self.colors)
        else:
            self.superstyle = "ironman"
            self.SP = ironman.IronMan(self.colors)

    def plot_v_lines(self, x, ymin, ymaxs, colors, style):

        if self.SP == None:
            self.SP = superman.Superman(self.colors)

        for i in range(len(x)):
            plt.vlines(x[i], ymin[i], ymaxs[i], colors[i], label=self.vlabel[i], linestyles=style[i], linewidth=2)

    def plot_data(self, x, y_list):

        if self.SP == None:
            self.SP = superman.Superman(self.colors)

        if len(self.crv_style) != len(y_list):
            warnings.warn("Different size for crv_style and y_list", DeprecationWarning)

        for i in range(len(y_list)):
            print(x)
            print(y_list[i])
            print(self.colors["superman"][i])

            try:
                plt.plot(x, y_list[i], label=self.labels[i], color=self.colors[self.superstyle][i])
            except IndexError:
                plt.plot(x, y_list[i], color=self.colors[self.superstyle][i])
                warnings.warn(f"You forgot to labelize your curve number: {i}", UserWarning)

        '''plt.scatter(x, y, marker='o', c=self.color)
        plt.scatter(x2, y2, marker='o', c='#FFFFFF')'''
        # plt.hlines(17000, 0, 350, color='#FFEE00', label='Plafond de sustentation')

        plt.legend(facecolor="black", frameon=True)
        plt.title(self.title, fontsize=15, style="italic")
        plt.xlabel(self.xlabel, loc='center', fontsize=10)
        plt.ylabel(self.ylabel, loc='center', fontsize=10)

        self.SP.neon_curve(x, y_list)

        plt.grid(which='both', b=True, color="0.5")

        plt.grid(which='minor', b=True, color="0.2", alpha=0.5)

        plt.show()
