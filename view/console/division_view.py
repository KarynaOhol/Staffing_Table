from controller.divisions_controller import DivisionsController
from entity.divisions import Division

div_ctrl = DivisionsController()


def all_divisions():
    try:
        for r in div_ctrl.all_divisions():
            print(r)
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def find_division():
    try:
        id = int(input("Enter id "))
        print(div_ctrl.get_by_id(id))
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def add_division():
    try:
        print("Enter division data:")
        name = input("Enter name ")
        persentage_one = input("Enter persentage per irregular worker day ")
        type = input("Enter type ")
        div_ctrl.create(Division(name, persentage_one, type))

    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def edit_division():
    try:
        id = int(input("Enter id "))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("1.Change name")
        print("2.Change persentage")
        print("3.Change type")
        res = int(input("What do you want to do?( 0 to go back): "))
        if res == 1:
            name = input("Enter new name ")
            div_ctrl.update_name(id, name)
        elif res == 2:
            persentage_one = int(input("Enter persentage per irregular worker day "))
            div_ctrl.update_persentage(id, persentage_one)
        elif res == 3:
            type = input("Enter type ")
            div_ctrl.update_type(id, type)
        elif res == 0:
            return
        else:
            print("Incorrect input")

    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def delete_division():
    try:
        id = int(input("Enter id "))
        div_ctrl.delete(id)
    except Exception as e:
        print(e)
        print("Oh,no something went wrong...")


def division_menu():
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
                all_divisions()
            elif res == 2:
                find_division()
            elif res == 3:
                add_division()
            elif res == 4:
                edit_division()
            elif res == 5:
                delete_division()
            elif res == 0:
                return
            else:
                print("Incorrect input")
        except:
            print("Error")
