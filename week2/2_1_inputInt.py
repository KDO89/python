def input_int(a, b):
    while True:
        inputString = input()
        if inputString.isdigit():
            inputString = int(inputString)
            if inputString >= a and inputString <= b:
                return inputString
            else:
                print("Please try again")
                continue
        else:
            print("Please enter a number")
            continue
input_int(1, 10)
                
        
