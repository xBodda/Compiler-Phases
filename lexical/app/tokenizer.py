from __future__ import absolute_import

from app.datatypes import datatype_set
from app.operators import operator_set
from app.token import TokenType, Token
import re
class Tokenize():
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.line = 1
        self.column = 0
        self.in_string = False
        self.queue = []
        self.token_list = []
    def checkInt(self,str):
        try:
            int(str)
            return True
        except ValueError:
            return False
    def checkId(self, str):
        check = re.search(r'^[^\d][\w!@#$%^&*\;\(\)\/\\]*\Z', str)
        if check:
            return True
        else:
            return False
    def checkDouble(self,str):
        check = re.search(r'^\d+.\d\Z', str)
        if check:
            return True
        else:
            return False
    def tokenize(self):
        current_token = ""
        column_token = 0
        while self.index < len(self.text)+1:
            if(self.index != len(self.text)):
                char = self.text[self.index]
            if char == '\n':
                self.line += 1
                self.column = 1
                char = ' '
            if(char == '"'):
                self.in_string = True
                self.queue.append(Token(char, TokenType.STRING_SYBMOL, self.line, self.column))
            if (char == ' ' or self.index == len(self.text) or char == '"') and current_token.strip() != "" :
                char = ''
                self.column += 1
                if current_token in datatype_set:
                    self.token_list.append(Token(current_token, TokenType.DATATYPE, self.line, self.column))
                elif current_token in operator_set:
                    self.token_list.append(Token(current_token, TokenType.OPERATOR, self.line, self.column))
                elif  self.in_string:
                    self.token_list.append(Token(current_token, TokenType.STRING, self.line, self.column))
                    self.in_string = False
                elif self.checkId(current_token):
                    self.token_list.append(Token(current_token, TokenType.IDENTIFIER, self.line, self.column))
                elif self.checkInt(current_token):
                    self.token_list.append(
                        Token(current_token, TokenType.INTEGER, self.line, self.column))
                elif self.checkDouble(current_token):
                    self.token_list.append(
                        Token(current_token, TokenType.DOUBLE, self.line, self.column))
                else:
                    self.token_list.append(
                        Token(current_token, TokenType.ERROR, self.line, self.column))
                self.column += column_token
                column_token = 0
                current_token = ""
                self.index += 1
                continue
            if(self.queue != []):
                self.token_list.append(self.queue.pop(0))
                self.index += 1
                continue
            current_token += str(char)
            column_token += 1
            self.index += 1
        return self.token_list
