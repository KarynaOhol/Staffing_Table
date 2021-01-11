from view.console.division_view import division_menu
from view.console.staff_units_view import staff_unit_menu
from view.console.disribution_view import distribution_menu
from view.console.disribution_view import calc


def start_menu():
    while True:
        try:
            print("___________________________________________________________________________\n")
            print("1. Divisions")
            print("2. Staff Units")
            print("3. Unit Distribution")
            print("4. Calculate salary for staff unit")
            res = int(input("Select type to work with( 0 to go back): "))
            if res == 1:
                division_menu()
            elif res == 2:
                staff_unit_menu()
            elif res == 3:
                distribution_menu()
            elif res == 4:
                calc()
            elif res == 0:
                return
            else:
                print("Incorrect input")
        except:
            print("Error")


start_menu()
