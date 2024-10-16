while True:
    #input 1: what mathematical operation is being performed.
    op = input("which mathmatical operation?")
    #input 2: the first number in the equation (could be float)
    fn = int(input("first number?"))
    #input 3: the second number in the equation(could be float)
    sn = int(input("second number?"))
    #addition 
    if op == "+":
      answer = fn + sn
    #subtraction 
    if op == "-":
       answer = fn - sn
    #division (floating point) 
    if op == "/":
     answer = float(float(fn) / float(sn))
    #multiplication 
    if op == "*":
      answer = fn * sn
    #exponents
    if op == "^":
      answer = fn ** sn
    #your output should include the formula as well as the solution for example something like this:
    print(fn, op, sn, "=", answer)
    #5 + 4 = 9

    #Your program should also implement a while loop so it keeps running, allowing the user to not have to re run your program each time

    #they use it.
