import random
import subprocess
import time
x = ['₁','₂','₃','₄','₅','₆','₇','₈','₉']
y = ['₁','₂','₃','₄','₅','₆','₇','₈','₉']
class TicTacToe:
    def __init__(self,player1,player2):
        self.p1 = player1
        self.p2 = player2
    def gameneeds(self):
        cnt=0
        for i in range(0,len(x),3):
            print(' '*20,f'{x[i]} ┃ {x[i+1]} ┃ {x[i+2]}')
            cnt+=1
            if cnt < 3:
                print(' '*20,'━━┃━━━┃━━')
        print()
    def randomplayer(self):
        player_select = random.choice([self.p1,self.p2])
        if player_select == self.p1:
            first = self.p1
        else:
            first = self.p2
        return first

    def play_game(self):
        choosen_list = []
        if self.randomplayer() == self.p1:
            first_player = self.p1
            second_player = self.p2
        else:
            first_player = self.p2
            second_player = self.p1
        while True:
            print()
            subprocess.run('cls',shell=True)
            self.gameneeds()
            print()
            while True:
                print(f'Player {first_player} choice - X')
                print('-'*20)
                p1_select = input('Make a move: ')
                print()
                if p1_select not in choosen_list:
                    if p1_select.isdigit() and 0 < int(p1_select) < 10:
                        x[int(p1_select)-1] = 'X'
                        choosen_list.append(p1_select)
                        subprocess.run('cls',shell=True)
                        self.gameneeds()
                        break
                    else:
                        subprocess.run('cls',shell=True)
                        self.gameneeds()
                        print('Enter valid input.')
                        print()
                else:
                    subprocess.run('cls',shell=True)
                    self.gameneeds()
                    print('Entered input Already Used. Choose another input')                    
                    print()
            if (x[0] == x[1] == x[2] == 'X') or (x[0] == x[3] == x[6] == 'X') or (x[0] == x[4] == x[8] == 'X') or (x[2] == x[4] == x[6] == 'X'):
                print()
                print('--->','*'*5,first_player,'Won the Match','*'*5,'<---')
                print()
                break
            elif (x[6] == x[7] == x[8] == 'X') or (x[2] == x[5] == x[8] == 'X') or (x[1] == x[4] == x[7] == 'X') or (x[3] == x[4] == x[5] == 'X'):
                print()
                print('--->','*'*5,first_player,'Won the Match','*'*5,'<---')
                print()
                break
            else:
                cnt = 0
                for i in y:
                    if i in x:
                        cnt+=1
                if cnt == 0:
                    print()
                    print('--->','*'*5,'GAME WAS TIE','*'*5,'<---')
                    print()
                    break
            while True:
                print(f'Player {second_player} choice - O')
                print('-'*20)
                p2_select = input('Make a Move: ')
                print()
                if p2_select not in choosen_list:
                    if p2_select.isdigit() and 0 < int(p2_select) < 10:
                        x[int(p2_select)-1] = 'O'
                        choosen_list.append(p2_select)
                        break
                    else:
                        subprocess.run('cls',shell=True)
                        self.gameneeds()
                        print('Enter valid input.')
                        print()
                else:
                    subprocess.run('cls',shell=True)
                    self.gameneeds()
                    print('Entered input Already Used. Choose another input')
                    print()
            if (x[0] == x[1] == x[2] == 'O') or (x[0] == x[3] == x[6] == 'O') or (x[0] == x[4] == x[8] == 'O') or (x[2] == x[4] == x[6] == 'O'):
                print()
                print('--->','*'*5,second_player,'Won the Match','*'*5,'<---')
                print()
                break
            elif (x[6] == x[7] == x[8] == 'O') or (x[2] == x[5] == x[8] == 'O') or (x[1] == x[4] == x[7] == 'O') or (x[3] == x[4] == x[5] == 'O'):
                print()
                print('--->','*'*5,second_player,'Won the Match','*'*5,'<---')
                print()
                break
            else:
                cnt = 0
                for i in y:
                    if i in x:
                        cnt+=1
                if cnt == 0:
                    print()
                    print('--->','*'*5,'GAME WAS TIE','*'*5,'<---')
                    print()
                    break
move = 1
while True:
    print(' '*move,'Welcome to TIC-TAC-TEO --->')
    move+=1
    if move==20:
        time.sleep(1)
        subprocess.run('cls',shell=True)
        break
    time.sleep(0.1)
    subprocess.run('cls',shell=True)
print()
print('~'*20,'TIC-TAC-TEO','~'*20)
play1 = input('Enter Player 1 name: ').upper()
play2 = input('Enter Player 2 name: ').upper()
object = TicTacToe(play1,play2)
print()
print('~'*20,'TIC-TAC-TEO','~'*20)
print()
object.play_game()
print()
while True:
    play_again = input('Do you want to play again ? (Yes / No): ').capitalize()
    print()
    if play_again == 'Yes':
        x = ['₁','₂','₃','₄','₅','₆','₇','₈','₉']
        y = ['₁','₂','₃','₄','₅','₆','₇','₈','₉']
        object.play_game()    
    elif play_again == 'No':
        break
    else:
        print('Please enter Yes or No, to Play.')
        print()