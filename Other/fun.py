def add(a):
    global result
    result = a+result
    return result


def sub(a):
    global result
    result = result - a
    return result


def mul(a):
    global result
    result = a*result
    return result


def div(a):
    global result
    result = a/result
    return result

result = int(input())
opt = ""
while opt != ';':
    # print("+ -- addition")
    # print("- -- subtraction")
    # print("* -- Multiplication")
    # print("/ -- division")
    # print("; -- Exit")
    # print("== -- DISplay result")
    opt = input()
    if opt == '+':
        result = add(int(input()))
    elif opt == '-':
        result = sub(int(input()))
    elif opt == '*':
        result = mul(int(input()))
    elif opt == '/':
        result = div(int(input()))
    elif opt == '=':
        print(result)
    elif opt == ';':
        exit(0)
    else:
        print('syntax error')