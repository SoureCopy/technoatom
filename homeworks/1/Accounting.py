class Charge:
    def __init__(self, value):
            self._value=float(value)

    @property
    def value(self):
        return round(self._value, 2)

    def __str__(self):
        return str(self.value)

class Account:
    def __init__(self, total=0):
        self._charges=[]
        self._total = round(float(total), 2)

    def __iter__(self):
        return iter(self._charges)

    @property
    def total(self):
        return(self._total)

    @property
    def charges(self):
        return(self._charges)

    def addTransaction(self, charge):
        self._total+=charge.value
        self._charges.append(charge)
        if (self.total<0):
                print("'Total' less then 0, you are a bankrupt")
                print(self)
                raise SystemExit

    def __str__(self):
        return 'Balance: {0}\nCharges: {1}'.format(self.total, ', '.join(map(str, self.charges)))

ch1 = Charge("123")
ch2 = Charge(-122.886)
ac = Account()
print(ac.total)
ch3 = Charge(200)
ac.addTransaction(ch1)
ac.addTransaction(ch2)
ac.addTransaction(ch3)
for ch in ac:
    print(ch)
print(ac.total)
print(ac)