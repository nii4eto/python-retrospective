class TicTacToeBoard:
    def __init__(self):
        self.fields = {'A1': ' ', 'A2': ' ', 'A3': ' ',
                       'B1': ' ', 'B2': ' ', 'B3': ' ',
                       'C1': ' ', 'C2': ' ', 'C3': ' '}

        self.values = ('X', 'O')
        self.count = 0
        self.last_move = None

    def __setitem__(self, field, value):
        if field not in self.fields:
            raise InvalidKey
        if value not in self.values:
            raise InvalidValue
        if self.fields[field] != ' ':
            raise InvalidMove
        if self.last_move == value:
            raise NotYourTurn

        self.fields[field] = value
        self.last_move = value
        self.count += 1

    def __getitem__(self, key):
        return self.fields[key]

    def __str__(self):
        row = '{} | {} | {} | {} |\n'
        place = self.fields

        board = '\n  -------------\n' +\
                row.format('3', place['A3'], place['B3'], place['C3']) +\
                '  -------------\n' +\
                row.format('2', place['A2'], place['B2'], place['C2']) +\
                '  -------------\n' +\
                row.format('1', place['A1'], place['B1'], place['C1']) +\
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
            return 'X wins!'
        elif self.check_for_win('O'):
            return 'O wins!'
        elif self.count == 9:
            return 'Draw!'
        else:
            return 'Game in progress.'


class InvalidKey(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidMove(Exception):
    pass


class NotYourTurn(Exception):
    pass
