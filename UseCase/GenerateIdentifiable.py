import random
import string

special_characters = ['"','!','@','#','$','%','^','&','*','(',')','-','+','?','_','=','<','>','/']

class GenerateIdentifiable:
    def __init__(self):
        self.list = []

    def createId(self): 
        self.list.clear()
        for x in range(12):
            chooser = random.randint(1,3)
            if chooser == 1:
                randomizerlet = random.choice(string.ascii_letters)
                x = randomizerlet 
                self.list.append(str(x))
            elif chooser == 2:
                randomizernum = random.randint(1,9)
                x = randomizernum
                self.list.append(str(x))  
            elif chooser ==3:
                randomizerchar = random.choice(special_characters)
                x = randomizerchar 
                self.list.append(str(x))

        final = ''.join(self.list)
        return final

    def createNumber(self):
        self.list.clear()
        for x in range(12):
            randomizernum = random.randint(1,9)
            x = randomizernum
            self.list.append(str(x))  

        final = ''.join(self.list)
        return final
