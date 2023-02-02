from random import*
import gc
class player:
    def init(self, name, aliveness = True, killvotes = 0):
        self.name = name
        self.aliveness = aliveness
        self.killvotes = killvotes

class mafia(player):
    def init(self, name, aliveness = True, killvotes = 0):
        super().init(name, aliveness, killvotes)

    def killvote(self):
        print("Настуапила ночь. кого хотите убить?")
        for i in gc.get_objects():
            if i.aliveness == True:
                print(i)
                alive = []
                alive.append(i)
        choice = input()
        if choice in alive:
            choice.killvotes += 1

class doctor(player):
    def init(self, name, aliveness = True, killvotes = 0):
        super().init(name, aliveness, killvotes)

class commissioner(player):
    def init(self, name, aliveness = True, killvotes = 0):
        super().init(name, aliveness, killvotes)

class innocent(player):
    def init(self, name, aliveness = True, killvotes = 0):
        super().init(name, aliveness, killvotes)


pl = mafia('Andrey')
