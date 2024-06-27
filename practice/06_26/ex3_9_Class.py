# class Car:
#   def __init__(self,a_brand,a_model,a_color):
#     self.brand=a_brand
#     self.model=a_model
#     self.color=a_color
#   def turn_on(self):
#     print(self.brand, self.model,self.color, 'start')
#   def drive(self):
#     print(self.brand, self.model,self.color, 'driving')
#   def turn_off(self):
#     print(self.brand, self.model,self.color, 'stop')
#   def __str__(self):
#     print(f'brand:{self.brand},model:{self.model}, color={self.color}')


# h1 = Car('포르쉐','파나메라','흰색')
# h1.turn_on()
# h1.drive()
# h1.turn_off()
# print(h1)

# h2 = Car('현대','아반떼','검정색')
# h2.turn_on()
# h2.drive()
# h2.turn_off()
#-----------------------------------------------------------------------------
# class Dad:
#   print('아빠 일')

# class Mom:
#   def cook(self):
#     print('엄마 요리')

# class Me(Mom, Dad):
#   pass

# ime = Me()

# ime.work()
# ime.cook()
#------------------------------------------------------------------------------

class Default:
    def __init__(self,a_name,a_hp,a_pow,a_defence):
      self.name=a_name
      self.hp=a_hp
      self.pow=a_pow
      self.defence = a_defence
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0


class Monster(Default):
  def attack(self, target):
    damage = self.pow - target.defence
    target.take_damage(damage)
    print(f'{self.name}이/가 {target.name}을/를 공격! -{damage}')
    print(f'{target.name}의 남은 체력: {target.hp}')
    print('-'*30)


  def info(self):
    print(self.name,self.hp,self.pow,self.defence)
    print('-'*30)

class Player(Default):
  def attack(self, target):
    damage = self.pow - target.defence
    target.take_damage(damage)
    print(f'{self.name}이/가 {target.name}을/를 공격! -{damage}')
    print(f'{target.name}의 남은 체력: {target.hp}')
    print('-'*30)


  def info(self):
    print(self.name,self.hp,self.pow,self.defence)
    print('-'*30)



monster1 = Monster('슬라임',50,20,0)
player1 = Player('태산',200,50,10)

monster1.info()
player1.info()

monster1.attack(player1)

player1.attack(monster1)



