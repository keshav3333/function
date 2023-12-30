class Sbi:
    branch = 'palamaner'
    ifsc   = 'sbi00026'
    manager = 'Jagan'
    loc     = 'chittoor'

    def __init__(self,name,mob,acc,pan,bal):
        self.name = name
        self.mobile = mob
        self.account = acc
        self.pan = pan
        self.balance = bal

    def credit(self,amt):
        self.balance+=amt

    def debit(self,amt):
        self.balance-=amt
    
    def update_mob(self,mob):
        self.mobile = mob

    @classmethod 
    def change_mgr(cls,new):
        cls.manager = new
        
    @staticmethod
    def add(a,b):
        return a+b


chandra = Sbi('nara chandra',8990125643,77091234,'CBNT00000W',1)
lokesh  = Sbi('nara lokesh',8901263789,77091235,'CBNT00001Y',2)