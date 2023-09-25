

class Link():
    def __init__(self, name, health, armor, power , weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power 
        self.weapon = weapon

    def print_info(self):
        print('greet the hero ->', self.name)
        print('Heathlevel:', self.health)
        print('armor', self.armor)
        print('power', self.power)
        print('Weapon', self.weapon)
    
    def strike(self, enemy):
        print(
            '-> STRIKEE' + self.name + 'is atacking' + enemy.name + 'With a strike forceof ' + str(self.power) + 'using a ' + self.weapon + '\n')
        
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        
        print(
            enemy.name + 'is reeling . \n Armor class down to '
            + str(enemy.armor) + ', and health level is up to ' +
            str(enemy.health) + '\n')

        


knight = Link('linkle', 50, 25, 20, 'épée de legende')

knight.print_info()

ganondorf = Link('ganon', 20, 5, 5, 'espadon')
ganondorf.print_info()

knight.strike(ganondorf)