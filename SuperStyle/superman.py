from matplotlib import pyplot as plt


def dark_style():
    # style
    plt.style.use("seaborn-dark")
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#151515'  # bluish dark grey
    for param in ['text.color', 'xtick.color', 'grid.color', 'ytick.color', 'axes.labelcolor']:
        plt.rcParams[param] = 'white'  # very light grey

    plt.grid(color='#2A3459')  # bluish dark grey, but slightly lighter than background

    # ==========================


def neon_curve(x, y_list, colors, superstyle):
    n_lines = 10
    diff_linewidth = 0.5
    alpha_value = 0.05

    for n in range(1, n_lines + 1):
        for i in range(len(y_list)):
            plt.plot(x, y_list[i], linewidth=2 + (diff_linewidth * n),
                     alpha=alpha_value, color=colors[superstyle][i])
