def greater(stk, result, init):
    str="bcdefghijklmnopqrstuvwxyz"
    index=ord(init)-97
    temp=str[index:index+len(stk)]
    init=chr(ord(init) + len(stk))
    temp = temp[::-1]
    result = result[:-1] + temp + result[-1:]
    return init, result

def smaller(stk, result, init):
    str = "bcdefghijklmnopqrstuvwxyz"
    index =ord(init)-97
    temp = str[index : index+len(stk)]
    init = chr(ord(init) + len(stk))
    result = result + temp
    return init, result


def print_str(s):
    stk = []
    init = "a"
    result = "a"
    for i in s:
        if i == "<" and (len(stk) == 0 or stk[-1] == "<"):
            stk.append(i)
        elif i == ">" and (len(stk) == 0 or stk[-1] == ">"):
            stk.append(i)
        elif i == "<" and stk[-1] == ">":
            init, result = greater(stk, result, init)
            stk = [i]
        elif i == ">" and stk[-1] == "<":
            init, result = smaller(stk, result, init)
            stk = [i]

    if len(stk) > 0:
        if stk[-1] == "<":
            init, result = smaller(stk, result, init)
        elif stk[-1] == ">":
            init, result = greater(stk, result, init)
    return result
    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print(print_str("<><"))
    pass