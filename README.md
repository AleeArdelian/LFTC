# LFTC
Minilanguage analyse 

~Lab 1:

Statement: Considering a small programming language (that we shall call mini-langauge), you have to write a scanner (lexical analyzer). The assignment can be divided in two parts:

1. Minilanguage Specification

	The minilanguage should be a restricted form of a known programming language, and should contain the following:
- 2 simple data types and a user-defined type
- statements:
	- assignment
	- input/output
	- conditional
	- loop
- some conditions will be imposed on the way the identifiers and constants can be formed.

2. Scanner implementation

	The scanner input will be a text file containind the source program, and will produce as output the following:
	- PIF - Program Internal Form
	- ST  - Symbol Table
In addition, the program should be able to determine the lexical errors, specifying the location, and, if possible, the type of the error.

The scanner assignment will be diferentiated based on:
	1. Identifiers:
		- length at most 8 characters
	2. Symbol Table:
		- unique for identifiers and constants
	3. Symbol Table Organization:
		- lexicographically binary tree


~Lab 2:

Regular grammars and finite automata

Write a program that:
1. Reads a grammar (from keyboard and from file)
2. Displays the elements of a grammar, using a menu: set of non-terminals, set of terminals,  set of productions, the productions of a given non-terminal symbol
3. Verifies if the grammar is regular
4. Reads the elements of a FA (from keyboard and from file)
5. Displays the elements of a finite automata, using a menu: the set of states, the alphabet, all the transitions, the set of final state.
6. Given a regular grammar constructs the corresponding finite automaton.
7. Given a finite automaton constructs the corresponding regular grammar.

~Lab 3:

Context-free grammars
Construct the grammar corresponding to your mini-language defined in lab 1
	




