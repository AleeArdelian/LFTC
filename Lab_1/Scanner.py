import re

from Pif import ProgramInternalForm
from Specifications import *
from SymbolTable import SymbolTable


#
# def IsIdentifier(token):
#     return re.match('^[a-z]([a-zA-Z0-9]){,7}$', token) is not None
#
#
# def IsConstant(token):
#     return re.match('^(0|-?[1-9][0-9]*)$|^\'.*\'$|^\".*\"$', token) is not None


#
# def is_numeric_constant(token):
#     return re.match('^[1-9][0-9]*$', token) is not None


# def IsOperatorChar(char):
#     for op in operators:
#         if char in op:
#             return True
#     return False


# def GetOperatorFromToken(line, index):
#     token = ''
#     while index < len(line) and IsOperatorChar(line[index]) and IsOperatorChar(token + line[index]):
#         token += line[index]
#         index += 1
#     return token, index


# def GetStringFromToken(line, index):
#     token = ''
#     quote_count = 0
#     while index < len(line) and quote_count < 2:
#         if line[index] == '"':
#             quote_count += 1
#         token += line[index]
#         index += 1
#     return token, index

#
# def Tokenize(line, listOfSeparators):
#     token = ""
#     index = 0
#     tokens = []
#
#     while index < len(line):
#         if line[index] == '"':
#             if token:
#                 tokens.append(token)
#             token, index = GetStringFromToken(line, index)
#             tokens.append(token)
#             token = ''
#
#         elif IsOperatorChar(line[index]):
#             if token:
#                 tokens.append(token)
#             token, index = GetOperatorFromToken(line, index)
#             tokens.append(token)
#             token = ''
#
#         elif line[index] in listOfSeparators:
#             if token:
#                 tokens.append(token)
#             token, index = line[index], index + 1
#             tokens.append(token)
#             token = ''
#         else:
#             token += line[index]
#             index += 1
#     if token:
#         tokens.append(token)
#     return tokens


class Scanner:
    def __init__(self, file):
        self._Identifiers = SymbolTable()
        self._Constants = SymbolTable()
        self._PIF = ProgramInternalForm()
        self._filename = file

    def run(self):
        self.Tokenize(self._filename)
        f = open("codif_table.txt", "w")

        for k, v in codification_table.items():
            f.write(str(k) + " " + str(v) + '\n')
        f.close()
        print('Identifiers: \n')
        self._Identifiers.PrintSymbolTable()
        print('Constants: \n')
        self._Constants.PrintSymbolTable()
        print(self._PIF)

    def fillIdentifiers(self, filename):
        line_number = 0
        with open(filename, "r") as file:
            for line in file:
                line_number += 1
                for token in self.GetTokensFromLine(line.strip(), separators):
                    if self.IsIdentifier(token) and token not in reserved + operators + separators:
                        self._Identifiers.add(token)
        file.close()

    def Tokenize(self, filename):
        self.fillIdentifiers(filename)
        line_number = 0
        with open(filename, "r") as file:
            for line in file:
                line_number += 1
                for token in self.GetTokensFromLine(line.strip(), separators):

                    if token in reserved + operators + separators:
                        if token is not ' ':
                            self._PIF.add(codification_table[token], -1)

                    elif self.IsIdentifier(token):
                        # self._Identifiers.add(token)
                        self._PIF.add(codification_table['identifier'], self._Identifiers.get(token))

                    elif self.IsConstant(token) or self.IsNegativeNumber(token):
                        self._Constants.add(token)
                        self._PIF.add(codification_table['constant'], self._Constants.get(token))

                    else:
                        raise Exception("Unknown token " + token + " at line " + str(line_number))

        file.close()

    def GetTokensFromLine(self, line, listOfSeparators):
        token = ""
        index = 0
        tokens = []
        openBrack = 0
        closeBrack = 0
        x = len(line)
        while index < len(line):
            if line[index] == '"':
                if token:
                    tokens.append(token)
                token, index = self.GetStringFromToken(line, index)
                tokens.append(token)
                token = ''

            elif self.IsOperatorChar(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.GetOperatorFromToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] in listOfSeparators:
                if token:
                    tokens.append(token)
                if token == '{':
                    openBrack += 1
                if token == '}':
                    closeBrack += 1
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''
            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)

        return tokens

    def IsConstant(self, token):
        return re.match('^(0|[1-9][0-9]*)$|^\'[a-zA-Z0-9]\'$|^\"[A-Za-z0-9]+\"$', token) is not None

    def IsNegativeNumber(self, token):
        return re.match('^-[1-9][0-9]*$', token) is not None

    def IsIdentifier(self, token):
        return re.match('^[a-z]([a-zA-Z0-9]){,7}$', token) is not None

    def IsOperatorChar(self, char):
        for op in operators:
            if char in op:
                return True
        return False

    def GetOperatorFromToken(self, line, index):
        token = ''
        tokenForNeg = ''
        tokenForNeg += line[index] + line[index + 1]

        if self.IsNegativeNumber(tokenForNeg):
            token += tokenForNeg
            index += 2
            return token, index
        elif line[index] == '=' and line[index] == '-':
            token += line[index]
            index += 1
            return token, index
        # elif self.IsNegativeNumber(tokenForNeg):
        #     token += tokenForNeg
        #     index += 2
        #     return token, index
        while index < len(line) and self.IsOperatorChar(line[index]) and self.IsOperatorChar(token + line[index]):
            token += line[index]
            index += 1
        return token, index

    def GetStringFromToken(self, line, index):
        token = ''
        quote_count = 0
        while index < len(line) and quote_count < 2:
            if line[index] == '"':
                quote_count += 1
            token += line[index]
            index += 1
        return token, index


sc = Scanner('Example.txt')
sc.run()
# print(sc.isNegativeNumber('23'))

# val = sc.WriteProgram('Example.txt')
# print(val)
# print(sc.IsConstant(val))
# sc.WriteProgram('Example.txt')
