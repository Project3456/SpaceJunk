class Space:
    def __init__(self, name, fuel, inventory = None):
        self.name = name
        self.fuel = fuel if isinstance(fuel, int) and 0 <= fuel <= 100 else 50
        self.inventory = []

    def show_status(self):
        return f"Корабль: {self.name},Топливо:{self.fuel},Мусор:{self.inventory}"

    def collect_junk(self,junk):
        if self.fuel >= 10:
            self.fuel -= 5
            self.inventory.append("junk")
            return f"Корабль: {self.name}, собрал обломок, топлива {self.fuel}!"
        else:
            return "Недостаточно топлива!"


## test
ship = Space("Звезда", 50)
print(ship.collect_junk("обломок"))
print(ship.show_status())
