import socket
import threading
import numpy as np
import csv
import pandas as pd
import pprint as pp
import random

class Board():

    '''well c'mon speedrun this game loooser xd'''

    def __init__(self):
        self.board=np.full((3,3)," ")
        
    def make_move(self, move, mark):
        self.board[int(move[0])][int(move[2])] = mark
    
    def avaliable_move(self):
        avaliables = []
        for row in range(3):
            for indx in range(3):
                if self.board[row][indx] == " ":
                    avaliables.append(f"{row},{indx}")
        return avaliables
        
    def avaliable_move_check(self, move):
        if self.board[int(move[0])][int(move[2])] == " ":
            return True
        return False

    def print_board(self):
        pretty_board = "\n______\n"
        for row in range(3):
            for indx in range(3):
                
                pretty_board += self.board[row][indx] + '|'
            pretty_board += "\n______\n"
        return pretty_board
    
    def __getitem__(self, indx):
        return self.board[indx]


class TTT:
    
    " the tic-tac-toe game "

    def __init__(self):
        self.board = Board()
        self.turn = "Fishie"
        self.status = False
        self.player1 = "Fishie"
        self.player2 = "Player"
    def game_status_checker(self):

        ''' Checks is the game won by someone'''

        #checks rows
        for i in range(3):
            if len(set(self.board[i])) == 1 and " " not in self.board[i]:
                #self.status = True
                return True

        #check for a win along columns
        for j in range(3):
            if len(set(self.board[:,j]))==1 and " " not in self.board[i]:
                #self.status = True
                return True
        # check for a win along diagonals
        if self.board[0][1] == self.board == self.board[1][1] == self.board[2][2] and self.board[0][1] != " ":
              
            #self.status = True
            return True
        if self.board[0][2] == self.board == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            #self.status = True
            return True
        # check for a Draw
        # if not 2 in self.board:
        #     self.status = True
        # else:
        #     return "In Progress"

    def manager(self, client_answer=None):
        #Если ходит сервер то находится лучший ход, игрок - вносится значение хода игрока
        if self.game_status_checker() != True:
            if self.turn == self.player1:
                self.board.make_move(random.choice(self.board.avaliable_move()), "F")
                text = f"Fishie swam!\n{self.board.print_board()}\n Now Your turn:"
                self.turn = "Player"
            elif self.turn == self.player2:
                if client_answer not in self.board.avaliable_move():
                    text = f"You can't make this move!"
                else:
                    self.board.make_move(client_answer, "P")
                    self.turn = 'Fishie'
                    text = f"Player made move\n{self.board.print_board()}"
            return text
        else:
            return f"Game Over!"
    def hoster(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), 1240))
        s.listen(1)
        client, xdd = s.accept()
        client.send("Ready to start? y/n".encode('UTF-8'))
        client_answer = client.recv(2048)
        if 'n' == client_answer.decode('UTF-8'):
            client.send('no one asked. Fishie moves!'.encode('UTF-8'))
        client.send(self.manager().encode('UTF-8'))
        while True:
            if self.turn == "Player":
                client_answer = client.recv(2048).decode('UTF-8')
                managed = self.manager(client_answer)
            else:
                managed = self.manager()
            if managed == "Game Over!":
                s.close()
                break
            client.send(managed.encode('UTF-8'))

n = TTT()
n.hoster()