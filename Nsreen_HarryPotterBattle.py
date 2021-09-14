spells = ('AvadaKedavra','Crucio','Imperio','Sheild','Reducto','Fiendfyre','Nebulus','Taboo','Expulso','Confringo')
H_spell = ('AvadaKedavra','Crucio','Imperio','Sheild','Reducto','Fiendfyre','Nebulus')
power ={'AvadaKedavra':100 ,'Crucio':40 ,'Imperio':20 ,'Sheild':0 ,'Reducto':60 ,'Fiendfyre':50 ,'Nebulus':40 ,'Taboo':80 ,'Expulso':60,'Confringo':55}
H_power = {'AvadaKedavra':100 ,'Crucio':40 ,'Imperio':20 ,'Sheild':0 ,'Reducto':60 ,'Fiendfyre':50 ,'Nebulus':40 }


# noinspection PyStatementEffect
class Spell():

    def __init__(self,spell , power):
        self.spell = spell
        self.power = power[spell]


class wizard(Spell):
    def __init__(self, health, energy ,sheild):
        self.health = health
        self.energy = energy
        self.sheild =sheild



Harry = wizard(100,500,3)
Voldmart = wizard(100,500,3)

while Harry.health !=0 or Voldmart.health !=0 :
    print("Enter The Two Spells (Harry then Voldmort) : ")
    h_spell, v_spell = raw_input('').split()

    h_power = power[h_spell]
    v_power = power[v_spell]
    print(h_power, v_power)
    if h_spell == 'Sheild':
        Harry.sheild =Harry.sheild -1
    elif v_spell == 'Sheild':
        Voldmart.sheild =Voldmart.sheild-1

    Harry.health = Harry.health - v_power
    Harry.energy = Harry.energy - h_power
    Voldmart.health = Voldmart.health - h_power
    Voldmart.energy = Voldmart.energy - v_power
    print ("Harry's Health, Energy And Sheild equal :")
    print (Harry.health , Harry.energy , Harry.sheild)
    print("Voldmart's Health, Energy And Sheild equal :")
    print(Voldmart.health, Voldmart.energy, Voldmart.sheild)
    if Harry.health ==0:
        print ("Voldmart Is The Winner")
        break
    elif Voldmart.health == 0:
        print ("Harry Is The Winner")
        break