import curves


if __name__ == '__main__':

    curve = curves.Curve("Test", "x", "y", ["une courbe", "une deuxième", "une troisième lol"])
    #curve.curve_style("superman")
    curve.plot_data([1, 2, 3, 5], [[1, 4, 5, 2], [10, 2, 5, 5], [45, 2, 25, 0]])
