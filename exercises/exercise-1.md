# Exercise 1

**Requirement 1.** In the root folder you created at the start of class (not the `demos` folder, but a sibling to the `demos` folder), create a new folder named `calc_app`.

**Requirement 2.** In the `calc_app` folder, create a name file named `__main__.py`. Put all code for this exercise in `__main__.py`. Do not break the code into multiple modules. Add new Run Configuration for Calc App (follow the same pattern as we did for demos)

**Requirement 3.** Build a console program that prompts the user for a command.

Seven Commands:

- add: add a new operand to the current result
- subtract: subtract a new operand from the current result
- multiply: multiply a new operand from the current result
- divide: divide a new operand from the current result
- exponent: raise the current result to the power of a new operand
- clear - reset current result to 0
- exit - exits the program

Prompt the user for the command and the operand.

- Enter a command: add
- Please enter an operand: 10

**Requirement 4.** Display the result after each command.

- Result: <previous result + 10>

**Requirement 5.** If the user types no command or an unknown command, display the following error message: "Invalid Command, Try Again."

**Requirement 6.** Using a list of dictionaries, capture a history of the calculator commands: add, subtract, multiple, divide, exponent

For each history entry, store a unique integer id (do not use external modules, just write some code to generate an id), the name of the command, and the operand value typed in. Do not track the result on the history.
