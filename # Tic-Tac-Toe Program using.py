import random
class TicTacToe:
    def __init__(self):
        self.board = []
        def create_board(self):
            for i in range(3):
                row = []
                for j in range(3):
                    row.append('-')
                    self.board.append(row)
                    def get_random_first_player(self):
                        return random.randint(0, 1)
                    def is_player_win(self,player):
                        iwn = None
                        n = len(self.board)
                        
                        for i in range(n):
                            if self.board[i] [j] !=player:
                                win = False
                                break
                            if win:
                                return win
                            win = True
                            for i in range(n):
                                if self.board[i] [j] !=player:
                                    win = False
                                    break
                                if win:
                                    return win
                                for i in range(n):
                                    if self.board[i] [n-1-i] != player:
                                        win = False
                                        break
                                    if win:
                                        return win
                                    return False
                                for row in self.board:
                                    for item in row:
                                        if item ==' ':
                                            return False
                                        return True
                                    def is_board_filled(self):
                                        for row in self.board:
                                            for item in row:
                                                if item ==' ':
                                                    return False
                                                return True
                                            def swap_player_turn(self,player):
                                                return 'X' if player == '0' else '0'
                                            def show_board(self):
                                                for row in self.board:
                                                    for item in row:
                                                        print(item,end=" ")
                                                        print()
                                                        def start(self):
                                                            self.create_board()
                                                            player ='X' if self.get_random_first_player() ==1 else '0'
                                                            while True:
                                                                print(f"Player (player) turn")
                                                                self.show_board()
                                                                row.col = list(map(input("Enter row and column number to fix spot:").split()))
                                                                print()
                                                                self.fix_spot(row -1,col -1,player)
                                                                if self.is_board_filled():
                                                                    print("Match Draw!")
                                                                    break
                                                                player =self.swap_player_turn(player)
                                                                print()
                                                                self.show_board()
                                                                
                                                                #stating the game 
                                                                tic_tac_toe =TicTacToe()
                                                                tic_tac_toe.start()