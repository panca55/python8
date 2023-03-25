class Hero:
    def __init__(self, name, health, attackPower, armorPoint):
        self.name = name
        self.hp = health
        self.attack = attackPower
        self.armor = armorPoint
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attack)
    def diserang(self,lawan, AP_lawan):
        print(f"{self.name} diserang {lawan.name}")
        attack_diterima = AP_lawan / self.armor
        print(f"Serangan terasa : {str(attack_diterima)}")
        self.hp -= attack_diterima
        print(f"Darah {self.name} tersisa {str(self.hp)}")

wawan = Hero("Wawan", 1000, 200, 150)
ujang = Hero("Ujang", 2000, 50, 250)

wawan.serang(ujang)