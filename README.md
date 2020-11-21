# COSPEX - Code Summarization via Program Execution

## What is COSPEX?
1. COSPEX, is an *Atom* IDE extension, that generates summaries for Python code snippets dynamically.
2. The current version takes source code snippet and test cases as input from developers.
3. Automated test case inputs can be added in the future to COSPEX.

## Features of COSPEX:
1. COSPEX dynamically extracts dynamic information such as inputs, outputs, comments (if present in the snippet) alongwith changes in variable values during runtime. 
2. Presents the dynamic information in the form of examples to the developers while also adding natural language phrases using pre-defined templates.
3. Provides sliding window interface for loops where each window represents an iteration of the loop.

## Uses of COSPEX:
Developers rely on code documentation to understand the functionality of the code snippet. However, manually creating and maintaining the documentation is effort-intensive and prone to errors. 
COSPEX aids developers to automatically generate summaries of the code snippets dynamically.
With the help of COSPEX, developers can summarize the code snippet at hand from the editor environment itself.
## Working of COSPEX:
COSPEX is developed as a package for Atom using the following approach:

<img alt="approach" src="https://user-images.githubusercontent.com/35232831/99877164-24a16800-2c22-11eb-9012-5b70841c7216.jpeg">

1. The developer opens the code snippet in Atom and calls the functions which need to be tested using appropriate test cases before invoking the tool.     
2. The preprocessor combines a hook with input code and the test cases into a separate program which is then executed. The hook intercepts any events passed between any software components and uses callback functions to run different functions based upon its state.
3. The execution of the program is traced using the hook. The trace function takes 3 arguments- stack frame, event and arguments for the event. Stack frame maintains a record of all the data on the stack corresponding to a subprogram call and includes information about the return address, argument variables, and local variables. The value of event is detected by the hook and it can take 3 values- Line, Call and Return.
4. Each event represents a different state of the program and provides a set of information unique to that state. We propose to call it the dynamic information instance of the state. The events are defined as follows:
    I. Call: When a function is called, a call event is generated. The tool extracts the name of the function and the arguments provided to it using the arguments of the event and the caller of the function from the stack frame for the function call dynamic information instance.
    II. Line: Before a line of code is executed, a line event is generated. The tool monitors any change in local variables using the stack frame. Upon detection, the change is extracted and stored in code dynamic information instance corresponding to the line of code. The tool also extracts the line number and the corresponding code using the arguments of the line event.
    III. Return: When a function is returned, a return event is generated. The tool extracts the value returned by it and stores it in the return value dynamic information instance. 
5. This information is extracted for every line of code in the program and compiled into a dynamic information instance of the complete program.
6. The extracted dynamic information instance of the complete program is compiled into a dynamic summary. We have framed natural language sentences for instances such as function call, variable introduction and return event  to make the summary more readable. The dynamic summary is presented in the form of collapsible blocks, each of which represents a function. Each collapsible block, when expanded reveals further lower-level information inside the function call. Figure below explains the structure of the generated output for a part of the summary presented for a Quick Sort program. 


## Summary generated for QuickSort program:
<img width=500 alt="classes" src="https://user-images.githubusercontent.com/35232831/99877378-ce352900-2c23-11eb-9839-7ac4a324ea2e.png">

