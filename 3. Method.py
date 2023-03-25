class Hero: # template
    # Class variable / variabel static
    jumlah_hero = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # isinstance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero +=1
        print(f"Membuat hero {inputName}")
        
    # void function, method tanpa return, tanpa argument
    def siapa(self):
        print(f"saya adalah {self.name}")
    # method dengan argument, tanpa return
    def healthUp(self, HPup):
        self.health += HPup
    def getHealth(self):
        return self.health

hero1 = Hero("sniper", 100, 10, 11)
print(Hero.jumlah_hero)
hero2 = Hero("mirana", 200, 10, 8)
print(Hero.jumlah_hero)
hero3 = Hero("ucup", 1000, 100,200)
print(Hero.jumlah_hero)

hero1.siapa()
hero1.healthUp(20)
hero1.getHealth()

print(hero1.__dict__)