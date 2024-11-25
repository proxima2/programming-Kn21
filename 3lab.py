import random

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = [random.randint(1, 9) for _ in range(5)]

    def play_card(self):
        return self.cards.pop() if self.cards else None

    def take_card(self, card):
        self.cards.insert(0, card)

    def has_cards(self):
        return len(self.cards) > 0

    def __str__(self):
        return f"{self.name}: {self.cards}"


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.table = []

    def check_end_condition(self):
        return sum(self.table) >= 20 or not self.player1.has_cards() or not self.player2.has_cards()

    def play_turn(self, current_player, opponent):
        card = current_player.play_card()
        if not card:
            return False
        
        print(f"{current_player.name} put {card}")
        self.table.append(card)

        if len(self.table) > 1 and self.table[-1] == self.table[-2]:
            opponent.take_card(self.table.pop())
            print(f"{opponent.name} takes {card}")

        return True

    def start(self):
        print(f"Initial STATE: {self.player1} --- {self.player2} --- Table: {self.table}")
        current_player, opponent = self.player1, self.player2

        while not self.check_end_condition():
            if not self.play_turn(current_player, opponent):
                break
            print(f"STATE: {self.player1} --- {self.player2} --- Table: {self.table}")
            current_player, opponent = opponent, current_player
            
        print("Game Over!")
        print(f"Final STATE: {self.player1} --- {self.player2} --- Table: {self.table}")

        if sum(self.table) % 2 == 0:
            winner = self.player1.name
        else:
            winner = self.player2.name
        print(f"Winner: {winner}")

player_1 = Player("Player 1")
player_2 = Player("Player 2")
game = Game(player_1, player_2)
game.start()
