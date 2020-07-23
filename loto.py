import random


class Cards:
    def __init__(self, whose_card):
        self.card = self.card_creation()
        self.whose_card = whose_card

    @staticmethod
    def card_row_creation(start_num, end_num):
        my_set = {num for num in range(start_num, end_num)}
        card_num_list = []
        for i in range(3):
            row_num = random.sample(my_set, 5)
            card_num_list.append(sorted(row_num))
            my_set -= set(row_num)
        return card_num_list

    @staticmethod
    def card_creation():
        card_numbers_player = Cards.card_row_creation(1, 91)
        # print(card_numbers_player)
        pos = [i for i in range(9)]
        rows = []
        for ro in range(3):
            row = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
            positions = sorted(random.sample(pos, 5))
            # print(positions)
            for i, position in enumerate(positions):
                row[position] = str(card_numbers_player[ro][i])
            rows.append(row)
        return rows

    def __str__(self):
        s = ' '
        if self.whose_card == 'Ваша карточка':
            return f'-------{self.whose_card}-------\n {s.join(self.card[0])}\n {s.join(self.card[1])}\n' \
                  f'{s.join(self.card[2])}\n---------------------------'
        elif self.whose_card == 'Карточка компьютера':
            return f'-----{self.whose_card}----\n {s.join(self.card[0])}\n {s.join(self.card[1])}\n' \
                  f'{s.join(self.card[2])}\n----------------------------'
        else:
            return f'-------{self.whose_card}-------\n {s.join(self.card[0])}\n {s.join(self.card[1])}\n' \
                  f'{s.join(self.card[2])}\n---------------------------'


class LotoBarrel:
    @staticmethod
    def random_barrel():
        barrel_bag = [ba for ba in range(1, 91)]
        for barr in range(90):
            barrel = barrel_bag.pop(random.randint(0, len(barrel_bag) - 1))
            yield barrel


game = None
score_comp = 0
score_player = 0
right_answer = 0

while game is None:
    human_player = Cards('Ваша карточка')
    comp_player = Cards('Карточка компьютера')
    bar_gen = LotoBarrel.random_barrel()

    for i in range(90):
        a = next(bar_gen)
        print(f'Round №{i + 1}')
        print(f'New loto barrel is {a} (barrels left {89 - i} )')
        print(human_player)
        print(comp_player)
        answer = input('Do you want to cross out the number? y/n: ')
        print('\n')

        for k in range(len(comp_player.card)):
            for j in range(len(comp_player.card[k])):
                if comp_player.card[k][j] == str(a):
                    comp_player.card[k][j] = ' - '
                    score_comp += 1
                    break
                else:
                    continue

        if answer == 'Y' or answer == 'y':
            right_answer = score_player
            for k in range(len(human_player.card)):
                for j in range(len(human_player.card[k])):
                    if human_player.card[k][j] == str(a):
                        human_player.card[k][j] = ' - '
                        score_player += 1
                        break
                    else:
                        continue
            if right_answer == score_player:
                print(f"You don't have this number! You lose the game!")
                game = 'Game over'
                break
        else:
            for k in range(len(human_player.card)):
                for j in range(len(human_player.card[k])):
                    if human_player.card[k][j] == str(a):
                        print(f"You have this number in your card! You lose the game!")
                        game = 'Game over'
                        break
        if game == 'Game over':
            break
        if (score_comp == 15 or score_player == 15) and score_comp == score_player:
            print(human_player)
            print(comp_player)
            print('The game ended in a draw!')
            game = 'Game over'
            break
        elif score_comp == 15:
            print(human_player)
            print(comp_player)
            print('The computer wins!')
            game = 'Game over'

            break
        elif score_player == 15:
            print(human_player)
            print(comp_player)
            print('Congratulations! You win!')
            game = 'Game over'
            break
print('\nGame over!')
