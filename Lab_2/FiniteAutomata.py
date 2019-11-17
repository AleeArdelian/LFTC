from RegularGrammar import RegularGrammar


class FiniteAutomat:

    def __init__(self):
        self._states = []
        self._alphabet = []
        self._transitions = {}
        self._initialState = None
        self._finalStates = None

    @property
    def states(self):
        return self._states

    @property
    def alphabet(self):
        return self._alphabet

    @property
    def transitions(self):
        return self._transitions

    @property
    def initial_state(self):
        return self._initialState

    @property
    def final_states(self):
        return self._finalStates

    def readFromKeyboard(self):
        print("Please insert states: \n Insert 0 to stop \n")
        state = input("State: ")
        while state != 0:
            self._states.append(state)
            state = input("State: ")

        print("Please insert alphabet: \n Insert 0 to stop \n")
        symbol = input("Symbol: ")
        while symbol != 0:
            self._alphabet.append(symbol)
            symbol = input("Terminal: ")

        transitions = []
        print("Please insert transitions of type (A,a)->B : \n Insert 0 to stop \n")
        trasnition = input("Transitions: ")
        while trasnition != 0:
            transitions.append(trasnition)
            trasnition = input("Transition: ")

        self._initialState = input("Please insert sinitial state: ")
        self._states.append(self._initialState)

        print("Please insert final states : \n Insert 0 to stop \n")
        finST = input("Final states: ")
        while finST != 0:
            self._finalStates.append(finST)
            finST = input("Final state: ")

        self._transitions = self.productionToDictionary(transitions)

    @staticmethod
    def productionToDictionary(transitions):
        trans = {}
        for transition in transitions:
            transition_split = transition.split('->')
            final_trans = transition_split[1]
            initial_trans = transition_split[0].strip('(').strip(')').strip()
            lhs = initial_trans.split(',')
            trans[(lhs[0], lhs[1])] = final_trans
        return trans

    def readFromFile(self, filename='fa.txt'):
        with open(filename, 'r') as f:
            lines = f.readlines()
            stripped_lines = []
            for line in lines:
                stripped_lines.append(line.strip('\n'))
            lines = stripped_lines
            self._states = lines[0].split(' ')
            self._alphabet = lines[1].split(' ')
            self._initialState = lines[2]
            self._finalStates = lines[3].split(' ')
            transitions = lines[4:]
            self._transitions = self.productionToDictionary(transitions)
            self._states.append(self._initialState)

    @states.setter
    def states(self, value):
        self._states = value

    @alphabet.setter
    def alphabet(self, value):
        self._alphabet = value

    @initial_state.setter
    def initial_state(self, value):
        self._initialState = value

    @final_states.setter
    def final_states(self, value):
        self._finalStates = value

    @transitions.setter
    def transitions(self, value):
        self._transitions = value

    def convertToRegularGrammar(self, regularGram):
        regularGram.nonTerminals = self._states
        regularGram.terminals = self._alphabet
        regularGram.startingSymbol = self.initial_state

        productions = {}
        starting_symbol = self.initial_state
        if starting_symbol in self.final_states:
            productions[starting_symbol] = ['epsilon']

        for key in self._transitions.keys():
            if key[0] not in productions.keys():
                productions[key[0]] = []

        for key, value in self._transitions.items():
            for rhs in value:
                if str(rhs[0]) == 'K':
                    productions[key[0]].append(str(key[1]))
                else:
                    productions[key[0]].append(str(key[1]) + str(rhs[0]))
        regularGram.productions = productions
        return regularGram
