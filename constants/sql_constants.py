CREATE_DISTRIBUTION_TABLE = """ CREATE TABLE IF NOT EXISTS distribution (
                                    divisions_id integer(10) NOT NULL,
                                    staff_units_id integer(10) NOT NULL, 
                                    FOREIGN KEY(divisions_id) REFERENCES divisions(id),
                                    FOREIGN KEY(staff_units_id) REFERENCES staff_units(id)
                                    ); """
CREATE_DIVISIONS_TABLE = """CREATE TABLE IF NOT EXISTS divisions (
                                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                    name varchar(255) NOT NULL UNIQUE, 
                                    Percentage1 integer(10), 
                                    type  varchar(255) NOT NULL
                                    );"""
CREATE_STAFF_UNITS_TABLE = """CREATE TABLE IF NOT EXISTS staff_units (
                                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                                    percentage2 integer(10), 
                                    vacation integer(10),
                                    position varchar(255) NOT NULL, 
                                    salary double(10) NOT NULL
                                     );"""
SELECT_DIVISION_BY_ID = """SELECT * FROM divisions WHERE id = ?"""
SELECT_DIVISION_BY_NAME = """SELECT * FROM divisions WHERE name = ?"""
SELECT_DIVISION = """SELECT * FROM divisions"""
INSERT_DIVISION = """INSERT INTO divisions( name, Percentage1, type) VALUES ( ?, ?, ?);"""
DELETE_DIVISION = """DELETE FROM divisions WHERE id = ?"""
UPDATE_DIVISION = """UPDATE divisions SET name = ?, Percentage1 = ?, type= ? WHERE id = ?;"""
UPDATE_DIVISION_NAME = """UPDATE divisions SET name = ? WHERE id = ?;"""
UPDATE_DIVISION_PERSENTAGE = """UPDATE divisions SET Percentage1 = ? WHERE id = ?;"""
UPDATE_DIVISION_TYPE = """UPDATE divisions SET type= ? WHERE id = ?;"""

SELECT_STAFF_UNIT_BY_ID = """SELECT * FROM staff_units WHERE id = ?"""
SELECT_STAFF_UNIT = """SELECT * FROM staff_units"""
INSERT_STAFF_UNIT = """INSERT INTO staff_units( percentage2, vacation, position,salary) VALUES ( ?, ?, ?,?);"""
DELETE_STAFF_UNIT = """DELETE FROM staff_units WHERE id = ?"""
UPDATE_STAFF_UNIT = """UPDATE staff_units SET percentage2 = ?, vacation = ?, position= ?,salary=? WHERE id = ?;"""
UPDATE_STAFF_PERSENTAGE = """UPDATE staff_units SET percentage2 = ? WHERE id = ?;"""
UPDATE_STAFF_VACATION = """UPDATE staff_units SET vacation = ? WHERE id = ?;"""
UPDATE_STAFF_POSITION = """UPDATE staff_units SET position= ? WHERE id = ?;"""
UPDATE_STAFF_SALARY = """UPDATE staff_units SET salary=? WHERE id = ?;"""

SELECT_DIVISION_BY_UNIT_ID = """SELECT divisions.id, divisions.name,divisions.Percentage1,divisions.type FROM divisions JOIN 
                                distribution ON divisions.id = distribution.divisions_id
                                WHERE distribution.staff_units_id = ?"""
SELECT_STAFF_UNITS_BY_DIVISION_ID = """SELECT staff_units.id, staff_units.percentage2,staff_units.vacation,staff_units.position,
                                staff_units.salary FROM staff_units JOIN 
                                distribution ON staff_units.id = distribution.staff_units_id
                                WHERE distribution.divisions_id = ?"""

SELECT_DISTRIBUTION = """SELECT 
                            d2.id, d2.name,d2.Percentage1,d2.type, staff_units.id,
                            staff_units.percentage2,staff_units.vacation,staff_units.position,
                            staff_units.salary 
                        FROM staff_units
                        JOIN  distribution d on staff_units.id = d.staff_units_id 
                        JOIN  divisions d2 on d.divisions_id = d2.id """

INSERT_DISTRIBUTION = """INSERT INTO distribution( divisions_id, staff_units_id) VALUES ( ?, ?);"""
DELETE_DISTRIBUTION = """DELETE FROM distribution WHERE staff_units_id = ?"""
UPDATE_DISTRIBUTION = """UPDATE distribution SET divisions_id = ? WHERE staff_units_id = ?;"""
