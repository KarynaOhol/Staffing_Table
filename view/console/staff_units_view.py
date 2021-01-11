from controller.staff_units_controller import StaffUnitsController
from entity.staff_units import StaffUnits

stf_ctrl = StaffUnitsController()


def all_staff_units():
    try:
        for r in stf_ctrl.all_units():
            print(r)
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def find_staff_unit():
    try:
        id = int(input("Enter id "))
        print(stf_ctrl.get_by_id(id))
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def add_staff_unit():
    try:
        print("Enter staff_unit data:")
        persentage_one= int(input("Enter persentage for harmful working conditions "))
        vacation = int(input("Enter vacation "))
        position = input("Enter position ")
        salary = int(input("Enter salary "))
        stf_ctrl.create(StaffUnits(persentage_one, vacation, position, salary))
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def edit_staff_unit():
    try:
        id = int(input("Enter id "))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("1.Change persentage")
        print("2.Change vacation")
        print("3.Change position")
        print("4.Change salary")
        res = int(input("What do you want to do?( 0 to go back): "))
        if res == 1:
            persentage_one = int(input("Enter persentage for harmful working conditions "))
            stf_ctrl.update_persentage(id, persentage_one)
        elif res == 2:
            vacation = int(input("Enter vacation "))
            stf_ctrl.update_vacation(id, vacation)
        elif res == 3:
            position = input("Enter position ")
            stf_ctrl.update_position(id, position)
        elif res == 4:
            salary = int(input("Enter salary "))
            stf_ctrl.update_salary(id, salary)
        elif res == 0:
            return
        else:
            print("Incorrect input")

    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def delete_staff_unit():
    try:
        id = int(input("Enter id "))
        stf_ctrl.delete(id)
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def staff_unit_menu():
    while True:
        try:
            print("___________________________________________________________________________\n")
            print("1. See all")
            print("2. Find by id")
            print("3. Add new")
            print("4. Edit by id")
            print("5. Delete by id")
            res = int(input("What do you want to do?( 0 to go back): "))
            if res == 1:
                all_staff_units()
            elif res == 2:
                find_staff_unit()
            elif res == 3:
                add_staff_unit()
            elif res == 4:
                edit_staff_unit()
            elif res == 5:
                delete_staff_unit()
            elif res == 0:
                return
            else:
                print("Incorrect input")
        except:
            print("Error")
