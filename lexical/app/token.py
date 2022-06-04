import enum

class TokenType(enum.Enum):
    DATATYPE = 0
    IDENTIFIER = 1
    INTEGER = 2 
    DOUBLE = 3
    STRING = 4
    OPERATOR = 5
    STRING_SYBMOL = 6
    ERROR = 7


class Token():
    def __init__(self, token_value, token_type, line, column):
        self.token_value = token_value
        self.token_type = token_type
        self.line = line
        self.column = column

    @property
    def position(self):
        return (self.line, self.column)

    def __str__(self):
        return '({}, {}, {})'.\
            format(self.token_value, self.token_type, self.position)

