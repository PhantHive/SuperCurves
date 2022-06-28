from matplotlib import pyplot as plt
from src.super_curves.SuperStyle.main_style import Global


class IronMan(Global):

    def __init__(self, colors):

        super(IronMan, self).__init__("#352713", "#D6D2C4", "white", "seaborn-dark")
        self.superstyle = "ironman"
        self.colors = colors

    def neon_curve(self, x, y_list):
        n_lines = 10
        diff_linewidth = 0.1
        alpha_value = 0.2

        for n in range(1, n_lines + 1):
            for i in range(len(y_list)):
                plt.plot(x, y_list[i], linewidth=2 + (diff_linewidth * n),
                         alpha=alpha_value, color=self.colors[self.superstyle][i])


