# Bugs  and Debugging

## Overt vs Covert bugs

- `Overt`: (or secret) It has obvious manifestion (e.g., program craches)
- `Covert`: It has not obvious manifestion and the program may run without any apparent problem but produces `wrong` (or `bad`) results

## Persistent vs Intermittent bugs

- `Persistent`: a bug occuring ervery time the programm is run with the same arguments
- `Intermittent`: a bug occuring only some of the time even if the programm is run with the same arguments and under (almost) same conditions

## Defensive programming

- Trying to write a programm in such a way that programming mistakes lead to bugs that are produce `overt` and/or `persitent`

## NB

- *"Programms that fail in `covert` ways are often highly dangerous. Since they are not apparently problematical, poeple use them and trust them to do right things"*
- *Bugs that are both `covert` and `intermittent` are almost always the hardest to find and fix*

## Some Bugs categories

There are several types of software bugs that can occur during the development and testing process. Some common types of software bugs include:

1. **Functional Bugs**: These bugs are associated with the functionality of a specific software component¹.
2. **Logical Bugs**: A logical bug disrupts the intended workflow of software and causes it to behave incorrectly.
3. **Workflow Bugs**: These bugs are associated with the user journey (navigation) of a software application¹.
4. **Unit Level Bugs**.
5. **System-Level Integration Bugs**.
6. **Out of Bound Bugs**.
7. **Security Bugs**.


## Debugging

- *Look for the usual aspects*. For examples:
  - *Passing arguments to a function in the wrong order*
  - *Misspelled a name (e.g case sentive issue)*
  - *Failed to reinitiliaze a varible*
  - *Testing that two floating points are equal (`==`) instead of nearly equal (e.g., abs(diff(a,b)) < epsilon )*
  - *Testing for value equality (e.g., L1 == L2, L1, L2 are lists) when we mean object equality (id(L1) == id(L2))*
  - *Forgetting that some built-in function has side effect*
  - *Creating an unintentuonal alias (e.g., L2 = L1 when we need to create a copy of a list instead of L2 = L1[:], L1, L2 are lists)* 
  - *Typo*
  - ...
- *Stop asking yourself why the programm is not doing waht you want it to. Instead, ask yourself why it is doing it is*
- *Keep is mind that bug is probably not where you think it is.If it where, you would probaby have found it long ago. One practical way to go about deciding where to look is asking where the bug cannot be.*
- *Try to explain the problem to somebody else. Try to explain why the bug cannot be in certain place.*
- *Don't believe everything you read. In particular, don't believe the documentation. The code may not be doing what the documenation suggest*
- *Stop debugging and start writing documenation. This help to approach the problem from different perpectives*
- *Walk a way, and try again tomorrow*

## Sources

- 7 Common Types of Software Bugs or Defects | BrowserStack. <https://www.browserstack.com/guide/types-of-software-bugs>.
- <https://en.wikipedia.org/wiki/Software_bug>.
- Common Types of Software Bugs Every Tester Should Know - Wolfmatrix. <https://wolfmatrix.com/application-development/types-of-software-bugs/>.

- 16 Types of Bugs in Software Testing - ThinkSys Inc. https://www.thinksys.com/qa-testing/types-software-testing-bugs/
