from matplotlib import pyplot as plt
from src.super_curves.SuperStyle.main_style import Global


class Superman(Global):

    def __init__(self, colors):

        super(Superman, self).__init__("#151A23", "#7E8A97", "white", "seaborn-dark")
        self.superstyle = "superman"
        self.colors = colors

    def neon_curve(self, x, y_list):
        n_lines = 10
        diff_linewidth = 0.5
        alpha_value = 0.05

        for n in range(1, n_lines + 1):
            for i in range(len(y_list)):
                plt.plot(x, y_list[i], linewidth=2 + (diff_linewidth * n),
                         alpha=alpha_value, color=self.colors[self.superstyle][i])
