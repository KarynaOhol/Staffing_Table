import _sqlite3
from entity.divisions import Division
import constants.sql_constants as cs


def create_table(cur):
    try:
        cur.execute(cs.CREATE_DIVISIONS_TABLE)
    except Exception as e:
        print(e)


class DivisionsController:
    def __init__(self):
        self.con = _sqlite3.connect("staffing.db")
        self.cur = self.con.cursor()
        create_table(self.cur)

    def get_by_id(self, id):
        self.cur.execute(cs.SELECT_DIVISION_BY_ID, (id,))
        arr = self.cur.fetchall()
        id = arr[0][0]
        name = arr[0][1]
        persentage_one = arr[0][2]
        type = arr[0][3]
        return Division(name, persentage_one, type, id)

    def create(self, division):
        self.cur.execute(cs.INSERT_DIVISION, (division.name, division.persentage_one, division.type))
        self.con.commit()

    def delete(self, id):
        self.cur.execute(cs.DELETE_DIVISION, (id,))
        self.con.commit()

    def delete(self, id):
        self.cur.execute(cs.DELETE_DIVISION, (id,))
        self.con.commit()

    def update(self, id, division):
        self.cur.execute(cs.UPDATE_DIVISION, (division.name, division.persentage_one, division.type, id))
        self.con.commit()

    def update_name(self, id, name):
        self.cur.execute(cs.UPDATE_DIVISION_NAME, (name, id))
        self.con.commit()

    def update_persentage(self, id, persentage):
        self.cur.execute(cs.UPDATE_DIVISION_PERSENTAGE, (persentage, id))
        self.con.commit()

    def update_type(self, id, type):
        self.cur.execute(cs.UPDATE_DIVISION_TYPE, (type, id))
        self.con.commit()

    def all_divisions(self):
        self.cur.execute(cs.SELECT_DIVISION)
        arr = self.cur.fetchall()
        divisions = []
        for rec in arr:
            temp = Division(rec[1], rec[2], rec[3], rec[0])
            divisions.append(temp)
        return divisions

    def __del__(self):
        self.cur.close()
        self.con.close()
