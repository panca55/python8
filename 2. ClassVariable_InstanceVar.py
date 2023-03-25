class Hero: # template
    # Class variable / variabel static
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # isinstance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah +=1
        print(f"Membuat hero {inputName}")

hero1 = Hero("sniper", 100, 10, 11)
print(Hero.jumlah)
hero2 = Hero("mirana", 200, 10, 8)
print(Hero.jumlah)
hero3 = Hero("ucup", 1000, 100,200)
print(Hero.jumlah)

