""" DEMO text adventure game """
from text_adventure_parser.parser import Parser
from text_adventure_parser.parse_result import ParseResult

from demo_game.player import Player
from demo_game.room import Room

verbs = ['exit', 'go', 'get', 'put', 'inventory', 'look']

nouns = ['gold', 'north', 'south', 'east', 'west']

shorthands = {
    'i': 'inventory',
    'n': 'go north', 's': 'go south', 'e': 'go east', 'w': 'go west'
}

class Game:
    """ Demo game object"""
    def __init__(self):
        self.parser = Parser(verbs, nouns, shorthands)
        self.player = Player()
        self.arena = [[Room("You are in an small hut", [], ['gold'])]]
    @property
    def current_room(self) -> Room:
        return self.arena[0][0]
    def handle_user_command(self, command:str):
        result: ParseResult = parser.parse(command)
        print(result)

def main():
    """ The game loop """
    print('Welcome to the game brave adventurer!')
    game = Game()

    while True:
        print(game.current_room.description)
        print(game.current_room.exits)
        print(game.current_room.items)

        command = input('\nWhat now?\n')
        game.handle_user_command(command)
    
