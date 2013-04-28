class TicTacToeBoard:
    VALUES = ('X', 'O')
    ROW = '{} | {} | {} | {} |\n'
    X_WINS = 'X wins!'
    O_WINS = 'O wins!'
    GAME_IN_PROGRESS = 'Game in progress.'
    DRAW = 'Draw!'

    def __init__(self):
        self.fields = {'A1': ' ', 'A2': ' ', 'A3': ' ',
                       'B1': ' ', 'B2': ' ', 'B3': ' ',
                       'C1': ' ', 'C2': ' ', 'C3': ' '}

        self.last_move = None

    def __setitem__(self, field, value):
        if field not in self.fields:
            raise InvalidKey

        if value not in self.VALUES:
            raise InvalidValue

        if self.fields[field] != ' ':
            raise InvalidMove

        if self.last_move == value:
            raise NotYourTurn

        self.fields[field] = value
        self.last_move = value

    def __getitem__(self, key):
        return self.fields[key]

    def __str__(self):
        place = self.fields

        board = '\n  -------------\n' +\
                self.ROW.format('3', place['A3'], place['B3'], place['C3']) +\
                '  -------------\n' +\
                self.ROW.format('2', place['A2'], place['B2'], place['C2']) +\
                '  -------------\n' +\
                self.ROW.format('1', place['A1'], place['B1'], place['C1']) +\
                '  -------------\n' +\
                '    A   B   C  \n'

        return board

    def check_for_win(self, mark):
        win_rows = [[self.fields['A1'], self.fields['B1'], self.fields['C1']],
                    [self.fields['A2'], self.fields['B2'], self.fields['C2']],
                    [self.fields['A3'], self.fields['B3'], self.fields['C3']],
                    [self.fields['A1'], self.fields['A2'], self.fields['A3']],
                    [self.fields['B1'], self.fields['B2'], self.fields['B3']],
                    [self.fields['C1'], self.fields['C2'], self.fields['C3']],
                    [self.fields['C1'], self.fields['B2'], self.fields['A3']],
                    [self.fields['A1'], self.fields['B2'], self.fields['C3']]]

        for row in win_rows:
            if row[0] == row[1] == row[2] == mark:
                return True
        return False

    def game_status(self):
        if self.check_for_win('X'):
            return self.X_WINS
        elif self.check_for_win('O'):
            return self.O_WINS
        elif self.check_for_win(' ') is not True:
            return self.DRAW
        else:
            return self.GAME_IN_PROGRESS


class TicTacToeError(Exception):
    pass


class InvalidKey(TicTacToeError):
    pass


class InvalidValue(TicTacToeError):
    pass


class InvalidMove(TicTacToeError):
    pass


class NotYourTurn(TicTacToeError):
    pass
