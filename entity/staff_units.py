import _sqlite3


class StaffUnits:

    def __init__(self, persentage_two, vacation, position, salary, id=0):
        self.id = id
        self.position = position
        self.persentage_two = persentage_two
        self.vacation = vacation
        self.salary = salary

    def __str__(self):
        return """
        STAFF UNIT:
                POSITION: """ + self.position + """
                PERSENTAGE for harmful working conditions: """ + str(self.persentage_two) + """
                SALARY: """ + str(self.salary) + """
                VACATION: """ + str(self.vacation)
