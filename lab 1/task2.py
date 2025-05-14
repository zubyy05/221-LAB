def calculator(t):
    for i in range(t):
 
        n = input()
        value = n.split(' ')
        
        if value[2] == "+":
            calc = float(int(value[1]) + int(value[3]))
            print(calc)
 
        elif value[2] == "-":
            calc = float(int(value[1]) - int(value[3]))
            print(calc)
 
        elif value[2] == "*":
            calc = float(int(value[1]) * int(value[3]))
            print(calc)
            
        elif value[2] == "/":
            calc = float(int(value[1]) / int(value[3]))
            print(calc)
 
    
 
calculator(int(input()))