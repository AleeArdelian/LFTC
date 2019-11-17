from FiniteAutomata import FiniteAutomat
from RegularGrammar import RegularGrammar


class UI:

    def __init__(self):
        self._regular_grammar = RegularGrammar()
        self._finite_automaton = FiniteAutomat()

    @staticmethod
    def print_main_menu():
        print("1. Regular Grammar")
        print("2. Finite automaton")
        print("0. Exit")

    @staticmethod
    def print_rg_menu():
        print("1. Read from file")
        print("2. Read from keyboard")
        print("3. See non-terminals")
        print("4. See terminals")
        print("5. See productions of given non-terminal")
        print("6. See all productions")
        print("7. Check if regular")
        print("8. Convert to finite automaton")
        print("0. Back")

    @staticmethod
    def print_fa_menu():
        print("1. Read from file")
        print("2. Read from keyboard")
        print("3. See the set of states")
        print("4. See alphabet")
        print("5. See transitions")
        print("6. See set of final states")
        print("7. Convert to regular grammar")
        print("0. Back")

    def menu(self):
        running = True
        while running:
            self.print_main_menu()
            user_choice = (int(input("Your choice: ")))
            if user_choice == 1:
                self.regular_grammar_menu()
            elif user_choice == 2:
                self.finite_automata_menu()
            elif user_choice == 0:
                running = False
            else:
                print("Invalid input")

    def regular_grammar_menu(self):
        running = True
        while running:
            self.print_rg_menu()
            user_choice = (int(input("Your choice: ")))
            if user_choice == 1:
                self._regular_grammar.readFromFile()
            elif user_choice == 2:
                self._regular_grammar.readFromKeyboard()
            elif user_choice == 3:
                print(self._regular_grammar.nonTerminals)
            elif user_choice == 4:
                print(self._regular_grammar.terminals)
            elif user_choice == 5:
                non_terminal = input("Non-terminal: ")
                print(self._regular_grammar.productionsForNonTerminal(non_terminal))
            elif user_choice == 6:
                print(self._regular_grammar.productions)
            elif user_choice == 7:
                print(self._regular_grammar.checkIfRegular())
            elif user_choice == 8:
                self._regular_grammar.convertToAutomata(self._finite_automaton)
                print("Transitions: " + str(self._finite_automaton.transitions))
                print("Alphabet:  " + str(self._finite_automaton.alphabet))
                print("States: " + str(self._finite_automaton.states))
                print("Final states: " + str(self._finite_automaton.final_states))
                print("Initial state: " + str(self._finite_automaton.initial_state))
            elif user_choice == 0:
                running = False
            else:
                print("Invalid input")

    def finite_automata_menu(self):
        running = True
        while running:
            self.print_fa_menu()
            user_choice = (int(input("Your choice: ")))
            if user_choice == 1:
                self._finite_automaton.readFromFile()
            elif user_choice == 2:
                self._finite_automaton.readFromKeyboard()
            elif user_choice == 3:
                print(self._finite_automaton.states)
            elif user_choice == 4:
                print(self._finite_automaton.alphabet)
            elif user_choice == 5:
                print(self._finite_automaton.transitions)
            elif user_choice == 6:
                print(self._finite_automaton.final_states)
            elif user_choice == 7:
                self._finite_automaton.convertToRegularGrammar(self._regular_grammar)
                print("Productions: " + str(self._regular_grammar.productions))
                print("Terminals:  " + str(self._regular_grammar.terminals))
                print("Non terminals: " + str(self._regular_grammar.nonTerminals))
                print("Starting symbol: " + str(self._regular_grammar.startingSymbol))
            elif user_choice == 0:
                running = False
            else:
                print("Invalid input")
