While the integer, floating-point, and string data types have an unlimited number of possible values, the Boolean data type has only two values: True and False.

# Comparison Operators
There are 6 comparison operators:

== Equal to

!= Not equal to

< Less than

> Greater than

<= Less than or equal to

>= Greater than or equal to

You might have noticed that the == operator (equal to) has two equal signs, while the = operator (assignment) has just one equal sign. It’s easy to confuse these two operators with each other. Just remember these points:

* The == operator (equal to) asks whether two values are the same as each other.
* The = operator (assignment) puts the value on the right into the variable on the left.

# Boolean Operators
The three Boolean operators (and, or, and not) are used to compare Boolean values. Like comparison operators, they evaluate these expressions down to a Boolean value. Let’s explore these operators in detail, starting with the and operator.

Unlike and and or, the not operator operates on only one Boolean value (or expression). The not operator simply evaluates to the opposite Boolean value.

# Elements of Flow Control
## Conditions
The Boolean expressions you’ve seen so far could all be considered conditions, which are the same thing as expressions; condition is just a more specific name in the context of flow control statements. Conditions always evaluate down to a Boolean value, True or False. A flow control statement decides what to do based on whether its condition is True or False, and almost every flow control statement uses a condition.

## Blocks of Code
   if name == 'Mary':
          ❶     print('Hello Mary')
                if password == 'swordfish':
          ❷         print('Access granted.')
                 else:
          ❸         print('Wrong password.')

The first block of code ❶ starts at the line print('Hello Mary') and contains all the lines after it. Inside this block is another block ❷, which has only a single line in it: print('Access Granted.'). The third block ❸ is also one line long: print('Wrong password.').

# Flow Control Statements

## if Statements
The most common type of flow control statement is the if statement. An if statement’s clause (that is, the block following the if statement) will execute if the statement’s condition is True. The clause is skipped if the condition is False.

## else Statements
An if clause can optionally be followed by an else statement. The else clause is executed only when the if statement’s condition is False. In plain English, an else statement could be read as, “If this condition is true, execute this code. Or else, execute that code.” An else statement doesn’t have a condition, and in code, an else statement always consists of the following:

## elif Statements
While only one of the if or else clauses will execute, you may have a case where you want one of many possible clauses to execute. The elif statement is an “else if” statement that always follows an if or another elif statement. It provides another condition that is checked only if all of the previous conditions were False. In code, an elif statement always consists of the following:

## while Loop Statements
You can make a block of code execute over and over again with a while statement. The code in a while clause will be executed as long as the while statement’s condition is True. In code, a while statement always consists of the following:

## break Statements
There is a shortcut to getting the program execution to break out of a while loop’s clause early. If the execution reaches a break statement, it immediately exits the while loop’s clause. In code, a break statement simply contains the break keyword.

## continue Statements
Like break statements, continue statements are used inside loops. When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition. (This is also what happens when the execution reaches the end of the loop.)

“Truthy” and “Falsey” Values

There are some values in other data types that conditions will consider equivalent to True and False. When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True. For example, look at the following program:

## for Loops and the range() Function

The while loop keeps looping while its condition is True (which is the reason for its name), but what if you want to execute a block of code only a certain number of times? You can do this with a for loop statement and the range() function.

In code, a for statement looks something like for i in range(5): and always includes the following:

* The for keyword

* A variable name

* The in keyword

* A call to the range() method with up to three integers passed to it

* A colon

* Starting on the next line, an indented block of code (called the for clause)


The range() function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.



