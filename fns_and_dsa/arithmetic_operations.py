# It's time do define perform_operation and its parameters num1, num2 and operation.

def  perform_operation(num1,  num2, operation):

    if operation.lower() == "add":              # addition operation is perform right here, follow by other operations
        return num1 + num2
    
    elif operation.lower() == "subtract":
        return num1 - num2
    
    elif operation.lower() == "multiply":       
        return num1 * num2
    
    elif operation.lower() == "divide":
        if num2 == 0:                           # division handling zero
            return "Cannot be divided by Zero"
    return num1 / num2

