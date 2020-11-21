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
<img alt="classes" src="https://user-images.githubusercontent.com/35232831/99877378-ce352900-2c23-11eb-9839-7ac4a324ea2e.png">

