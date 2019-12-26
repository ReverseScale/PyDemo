class Car():
    def __init__(self, colors='白色', types='小轿车'):
        self.colors = colors
        self.types = types
        super().__init__()

    def driver_gun(self):
        return self.colors + self.types + '刷刷刷' + '的跑起来了'

    def driver_blow(self):
        return self.colors + self.types + '滴滴滴' + '的响'

    def driver_exhaust(self):
        return self.colors + self.types + '突突突' + '的排气'


class ElectricCar(Car):
    def __init__(self, colors, types):
        super().__init__(colors, types)

    def driver_exhaust(self):
        return self.colors + self.types + '不会排气'

    def battery_low(self):
        return self.colors + self.types + '我没电了'


red_car = Car(colors='红色', types='大卡车')
print(red_car.driver_gun())
print(red_car.driver_exhaust())

tesla = ElectricCar(colors='灰色', types='小轿车')
print(tesla.driver_gun())
print(tesla.driver_exhaust())
print(tesla.battery_low())