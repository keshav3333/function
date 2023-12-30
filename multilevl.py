class Gparent:
    property1 = 'house'
    def __init__(self,name):
        self.name = name

class parent(Gparent):
    property2 = 'car'

class child(parent):
    property3 =  'bike' 

obj = child('sunil')

