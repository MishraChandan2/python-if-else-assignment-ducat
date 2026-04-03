HISTORY_FILE = "history.txt"

def show_history():
    file=open(HISTORY_FILE,'r')
    lines=file.readline()
    if len(lines)==0:
        print("No history found")
    else:
        for line in (lines):
            print(line.strip())
    file.close()

def clear_history():
    file=open(HISTORY_FILE,'w')
    file.close()
    print("History cleared")

def save_to_history(equation,result):
    file=open(HISTORY_FILE,'a')
    file.write(equation + "=" + str(result))   
    file.close()

def calculator(user_input):
    parts=user_input.split()
    if len(parts) !=3:
        print("invalid input, Use format: number operator number (e.g. 5 + 4)")
        return
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])
 
    if op=="+":
        result=num1+num2                    
    elif op=="-":
        result=num1-num2  
    elif op=="*":
        result=num1*num2  
    elif op=="/":
        if num2==0:
            print('cannot divide by zero')
            return
        result=num1/num2  
    else:
        print("invalid operator")
        return
    if int(result)==result:
        result=int(result)
    print("Result:",result)
    save_to_history(user_input,result)

def main():
    print(' SIMPLE CALCULATOR(type history,clear or exit)')
    while(True):
        user_input=input("Enter calculation (+ - * /) or commond (history, clear or exit)")
        if user_input=='exit':
            print('Goodbye')
            break
        elif user_input=='history':
            show_history()
        elif user_input == 'clear':            
            clear_history()
        else:
            calculator(user_input)

main()            
