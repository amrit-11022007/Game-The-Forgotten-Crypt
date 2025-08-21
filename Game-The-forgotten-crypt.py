#The Forgotten Crypt

import random

class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []
    
    def add_item(self, item):
        self.inventory.append(item)
        print(f'{item} added to inventory')

class NPC:
    def __init__(self, name, dialogue, has_item = False, item = None):
        self.name = name
        self.dialogue = dialogue
        self.has_item = has_item
        self.item = item

    def talk(self):
        print(f"{self.name}: {self.dialogue}")
        if self.has_item and self.item:
            print(f"{self.name} gives you {self.item}")

direction = ['east', 'west', 'north', 'south']
track_visit = {'Awakening_cell': True, 'Old_hallway': False}

global player
player = Player()
npc_1 = NPC("Unknown", "Ah...another lost soul. Few walk this path twice")
npc_2 = NPC("Unknown", "You see those three stones, breaking the correct one will give you a key to open the door. Choosing wrong one will damage you and reset the combination.", True, "Sacred Stone")
# fallen_soldier = NPC()


def intro():
    global name
    name = str(input('What is your name: '))

    print(f'--WAKES UP--', end='')
    input()
    print('Your head throbs. The air is damp and heavy. Moss grows between ancient stones. A faint torch flickers nearby. You remeber nothing - just the feeling that you must escape.')
    input()
    return Awakening_cell()

def Awakening_cell():
    
    print('What do you want to do?', end='')
    
    while True:
        pick = str(input("[Pick Torch], [Go north]")).lower()
        if pick == "pick torch":
            player.add_item('Torch')
            print(f'{name} got the torch', end='')
            input()
            break
        elif pick == "go north":
            break
        print('please enter correct input')
    return Old_hallway()

def Old_hallway():
    print(f'{name} enters the old hallway', end='')
    input()

    if track_visit['Old_hallway'] == False:
        print('The hallway stretches into darkness. The walls are covered in worn carving of fogotten gods. Dust clouds rise with every steps.')
        track_visit['Old_hallway'] = True
    if "Torch" in player.inventory:
        pass
    else:
        print("It's too dark, you cannot proceed without torch.")
        input()
        print(f'{name} goes back to Awakening Cell')
        return Awakening_cell()
    print('A strong presence can be felt', end='')
    input()
    npc_1.talk()
    input()
    print(f'{name} flashed the torch but found a fallen note.', end='')
    input()
    print(f'{name} readed the note', end='')
    input()
    print('"I have cities but no house, forests but no trees, rivers but no water."')
    while True:
        ans = str(input("What I am?: ")).lower()
        if ans == "map":
            print(f'A door open, {name} moves forward', end='')
            input()
            break
        print('wrong answer')
    return hall_of_wispers()

def hall_of_wispers():
    print("A narrow room with walls that seem to breathe. Whispers echo with no source. Three glowing stones are visible.")
    input()
    npc_2.talk()
    input()
    print(f"{name} received the sacred stone")
    player.add_item("Sacred Stone")
    stones = ['poison', 'key', 'poison']
    random.shuffle(stones)

    while True:
        choice = input("choose a stone(1,2,3): ")
        if choice not in ['1','2','3']:
            print('Invalid choice!')
            continue
        result = stones[int(choice)-1]
        if result == 'key':
            print("You found the hidden Key")
            player.add_item('Key')
            input()
            print(f'{name} opened the door.')
            break
        else:
            player.health -= 20
            print('Poison Gas!!! you lost 20 health')
            input()
            print(f'you have {player.health} left')
            input()
            if player.health <= 0:
                print("GAME OVER!!")
                return intro()
            stones = ['poison', 'key', 'poison']
            random.shuffle(stones)
    return guard_room()
 
def guard_room():
    print("A shadowy armored figure slumps against the wall. A broken spear in his hand. Eyes glow faintly red. It stirs when you approach.",end='')
    input()
    mood = '''What do you want to do?
    press 'a' to greet.
    press 'b' to give the sacred stone to it.
    press 'c' to fight with it.'''
    print(mood)

    while True:
        player_choice = input("Enter: ").lower()
        if player_choice == 'a':
            print('Do not fear me prisoner. I remeber what they made me for')
            continue
        elif player_choice == 'b':
            item = player.inventory.pop()
            print(f"{name} gives the {item} to soldier", end='')
            input()
            print("He open the final gate")
            break
        elif player_choice == 'c':
            print(f"He fucked {name} badly", end='')
            input()
            print("GAME OVER!!")
            return intro()
    return relic_chamber()

def relic_chamber():
    print("A grand chamber with floating relic. A voice booms..", end='')
    input()
    print('"You have three questions. only by answering them all can you claim the relic. Fail, and the chamber collapses."', end='')
    input()
    while True:
        ans_1 = input("I speak without a mouth and hear without ear. What am I? : ")
        ans_2 = input("Who gave you the key : ")
        ans_3 = input("I am always in front of you but can't seen: ")
        if ans_1 == "echo" and ans_2 == "ghost" and ans_3 == 'future':
            print("You got the relic and got out of the forgotten crypt.")
            print("GAME OVER!! YOU WON!!")
            break
        else:
            print("GAME OVER!! THE CHAMBER FELL AND YOU DIED")
            restart = input("Do you want to play again(y/n)? :  ")
            if restart == 'y':
                return intro()
            else:
                break

intro()