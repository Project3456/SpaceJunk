class Space:
    def __init__(self, name, fuel, inventory = None):
        self.name = name
        self.fuel = fuel if isinstance(fuel, int) and 0 <= fuel <= 100 else 50
        self.inventory = {}

    def show_status(self):
        return f"Корабль: {self.name},Топливо:{self.fuel},Мусор:{self.inventory}"

    def collect_junk(self,junk):
        if self.fuel >= 10:
            self.fuel -= 5
            self.inventory["metal"] = 0 + 1
            self.inventory["plastic"] = 0 + 1
            return f"Корабль: {self.name}, собрал обломок, топлива {self.fuel}!"
        else:
            return "Недостаточно топлива!"
    
    def trade_junk(self):
        if self.inventory["metal"] >= 1 and self.inventory["plastic"] >= 1 or self.inventory["metal"] >= 2 or self.inventory["plastic"] >= 2:
            self.inventory.pop("metal")
            self.inventory.pop("plastic")
            self.fuel += 10
            return f"{self.name} - Сдал мусор и получил 10 топлива количиство топлива: {self.fuel}"
        else:
            return f"У {self.name} - Недостаточно мусора"
        
    def add_rare_item(self):
        if self.fuel >= 15:
            self.fuel -= 15
            self.inventory["rare_item"] = 1
            return f"Корабль: {self.name} - Получил Rare придмет за 15 топливо! {self.inventory}"
        else:
            return "Недостаточно топлива для обмена на Rare"
        
    def check_inventory(self):
        count_metal = self.inventory["metal"]
        return f"У корабля {self.name} количиство: {count_metal} тип: metal"
        
        count_plastic = self.inventory["plastic"]
        return f"У корабля {self.name} количиство: {count_plastic} тип: plastic"
    
        count_rare = self.inventory["rare_item"]
        return f"У корабля {self.name} количиство: {count_rare} тип: rare_item"
            
## test
ship = Space("Звезда", 50)
print(ship.collect_junk("обломок"))
print(ship.show_status())
print(ship.check_inventory())
print(ship.trade_junk())
print(ship.add_rare_item())

