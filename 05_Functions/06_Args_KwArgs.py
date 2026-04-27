
def chai(*ingedients , **extra):
    print(f"Ingridients {ingedients}")
    print(f"Extras {extra}")

chai('Irani', 'Ginger', sweeter = "Honey", foam = "yes")

def chai2(*ingedients , **extra):
    print(f"Ingridients {ingedients}")
    print(f"Extras {extra}")

chai2('Irani', 'Ginger')

