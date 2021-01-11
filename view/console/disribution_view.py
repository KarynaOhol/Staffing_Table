from controller.distributions_controller import DistributionsController
from entity.distribution import Distribution

dst_ctrl = DistributionsController()


def all_distributions():
    try:
        for r in dst_ctrl.all_distributions():
            print(r)
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def find_division_by_unit():
    try:
        id = int(input("Enter  unit id "))
        print(dst_ctrl.get_division_by_unit_id(id))
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")

def find_units_by_division_id():
    try:
        id = int(input("Enter division id "))
        for r in dst_ctrl.get_units_by_division_id(id):
            print(r)
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def add_distribution():
    try:
        print("Enter distribution data:")
        div_id = int(input("Enter division id "))
        stf_id = int(input("Enter staff unit id "))
        dst_ctrl.create(stf_id,div_id)
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def edit_distribution():
    try:
        stf_id = int(input("Enter staff unit id "))
        div_id = int(input("Enter new division id "))
        dst_ctrl.update(stf_id, div_id)
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def delete_distribution_by_unit_id():
    try:
        id = int(input("Enter staff unit id "))
        dst_ctrl.delete(id)
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")

def calc():
    try:
        id = int(input("Enter staff unit id "))
        print(dst_ctrl.calculate_salary_for_unit(id))
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def distribution_menu():
    while True:
        try:
            print("___________________________________________________________________________\n")
            print("1. See all")
            print("2. Find division by unit id")
            print("3. Find units by division id")
            print("4. Add new")
            print("5. Edit division by unit id")
            print("6. Delete by unit id")
            res = int(input("What do you want to do?( 0 to go back): "))
            if res == 1:
                all_distributions()
            elif res == 2:
                find_division_by_unit()
            elif res == 3:
                find_units_by_division_id()
            elif res == 4:
                add_distribution()
            elif res == 5:
                edit_distribution()
            elif res == 6:
                delete_distribution_by_unit_id()
            elif res == 0:
                return
            else:
                print("Incorrect input")
        except:
            print("Error")
