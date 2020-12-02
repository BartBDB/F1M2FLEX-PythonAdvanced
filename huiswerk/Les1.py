class huiswerk:

    _tijd = "te lang"
    _speed = 0.1

    def _init_(self, tijd):
        self._tijd = tijd

    def Test(self):
        print("Dit is een test.")
        print("De tijd die ik hieraan heb besteed is:", self._tijd)


instanceHuiswerk = huiswerk()

print(huiswerk._speed)
instanceHuiswerk.Test()

print(instanceHuiswerk._speed)