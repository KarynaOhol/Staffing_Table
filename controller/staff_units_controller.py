import _sqlite3
from entity.staff_units import StaffUnits
import constants.sql_constants as cs


def create_table(cur):
    try:
        cur.execute(cs.CREATE_STAFF_UNITS_TABLE)
    except Exception as e:
        print(e)


class StaffUnitsController:
    def __init__(self):
        self.con = _sqlite3.connect("staffing.db")
        self.cur = self.con.cursor()
        create_table(self.cur)

    def get_by_id(self, id):
        self.cur.execute(cs.SELECT_STAFF_UNIT_BY_ID, (id,))
        arr = self.cur.fetchall()
        id = arr[0][0]
        persentage_two = arr[0][1]
        vacation = arr[0][2]
        position = arr[0][3]
        salary = arr[0][4]
        return StaffUnits(persentage_two, vacation, position, salary, id)

    def create(self, staff_units):
        self.cur.execute(cs.INSERT_STAFF_UNIT, (staff_units.persentage_two, staff_units.vacation,
                                                staff_units.position, staff_units.salary))
        self.con.commit()

    def delete(self, id):
        self.cur.execute(cs.DELETE_STAFF_UNIT, (id,))
        self.con.commit()

    def update(self, id, staff_units):
        self.cur.execute(cs.UPDATE_STAFF_UNIT, (staff_units.persentage_two, staff_units.vacation,
                                                staff_units.position, staff_units.salary, id))
        self.con.commit()

    def update_vacation(self, id, vacation):
        self.cur.execute(cs.UPDATE_STAFF_VACATION, (vacation, id))
        self.con.commit()

    def update_position(self, id, position):
        self.cur.execute(cs.UPDATE_STAFF_POSITION, (position, id))
        self.con.commit()

    def update_persentage(self, id, persentage):
        self.cur.execute(cs.UPDATE_STAFF_PERSENTAGE, (persentage, id))
        self.con.commit()

    def update_salary(self, id, salary):
        self.cur.execute(cs.UPDATE_STAFF_SALARY, (salary, id))
        self.con.commit()

    def all_units(self):
        self.cur.execute(cs.SELECT_STAFF_UNIT)
        arr = self.cur.fetchall()
        staff_units = []
        for rec in arr:
            temp = StaffUnits(rec[1], rec[2], rec[3], rec[4], rec[0])
            staff_units.append(temp)
        return staff_units

    def __del__(self):
        self.cur.close()
        self.con.close()
