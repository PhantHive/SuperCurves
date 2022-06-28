from src.super_curves import curves

if __name__ == '__main__':

    # SUPERMAN STYLE

    curve_super = curves.Curve("Style: SUPERMAN", "x", "y", ["une courbe", "une deuxième", "une troisième lol"])
    #curve.curve_style("superman")
    curve_super.curve_style("superman")
    curve_super.plot_data([1, 2, 3, 5], [[1, 4, 5, 2], [10, 2, 5, 5], [45, 2, 25, 0], [5, 2, 7, 0]])


    # IRON MAN STYLE

    curve_iron = curves.Curve("Style: IRON MAN", "x", "y", ["une courbe", "une deuxième", "une troisième lol"])
    # curve.curve_style("superman")
    curve_iron.curve_style("ironman")
    curve_iron.plot_data([1, 2, 3, 5], [[1, 4, 5, 2], [10, 2, 5, 5], [45, 2, 25, 0], [5, 2, 7, 0]])


