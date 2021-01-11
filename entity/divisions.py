class Division:

    def __init__(self, name, persentage_one, type, id=0):
        self.id = id
        self.name = name
        self.persentage_one = persentage_one
        self.type = type

    def __str__(self):
        return """
        DIVISION:
                NAME: """ + self.name + """
                PERSENTAGE per irregular worker day: """ + str(self.persentage_one) + """
                TYPE: """ + self.type
