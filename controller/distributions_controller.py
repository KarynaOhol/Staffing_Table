import _sqlite3
from entity.divisions import Division
from entity.staff_units import StaffUnits
from entity.distribution import Distribution
from controller.divisions_controller import DivisionsController
from controller.staff_units_controller import StaffUnitsController
import constants.sql_constants as cs


def create_table(cur):
    try:
        cur.execute(cs.CREATE_DISTRIBUTION_TABLE)
    except Exception as e:
        print(e)


class DistributionsController:
    def __init__(self):
        self.con = _sqlite3.connect("staffing.db")
        self.cur = self.con.cursor()
        create_table(self.cur)

    def get_division_by_unit_id(self, id):
        self.cur.execute(cs.SELECT_DIVISION_BY_UNIT_ID, (id,))
        arr = self.cur.fetchall()
        id = arr[0][0]
        name = arr[0][1]
        persentage_one = arr[0][2]
        type = arr[0][3]
        return Division(name, persentage_one, type, id)

    def get_units_by_division_id(self, id):
        self.cur.execute(cs.SELECT_STAFF_UNITS_BY_DIVISION_ID, (id,))
        arr = self.cur.fetchall()
        staff_units = []
        for rec in arr:
            temp = StaffUnits(rec[1], rec[2], rec[3], rec[4], rec[0])
            staff_units.append(temp)
        return staff_units

    def create(self, staff_units_id, divisions_id):
        self.cur.execute(cs.INSERT_DISTRIBUTION, (divisions_id, staff_units_id))
        self.con.commit()

    def delete(self, staff_units_id):
        self.cur.execute(cs.DELETE_DISTRIBUTION, (staff_units_id,))
        self.con.commit()

    def update(self, staff_units_id, divisions_id):
        self.cur.execute(cs.UPDATE_DISTRIBUTION, (divisions_id, staff_units_id))
        self.con.commit()

    def all_distributions(self):
        self.cur.execute(cs.SELECT_DISTRIBUTION)
        arr = self.cur.fetchall()
        distributions = []
        for rec in arr:
            div = Division(rec[1], rec[2], rec[3], rec[0])
            stf = StaffUnits(rec[5], rec[6], rec[7], rec[8], rec[4])
            dist = Distribution(div, stf)
            distributions.append(dist)
        return distributions

    def calculate_salary_for_unit(self, staff_units_id):
        stf_ctrl = StaffUnitsController()
        stf_unit = stf_ctrl.get_by_id(staff_units_id)
        div = self.get_division_by_unit_id(staff_units_id)
        salary = stf_unit.salary * (1 + (div.persentage_one * 0.01) + (stf_unit.persentage_two * 0.01))
        return "SALARY for " + stf_unit.position + "    " + str(salary)

    def __del__(self):
        self.cur.close()
        self.con.close()
