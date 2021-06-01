def calculate(s, starts, ends):
    res,store_mem,count = [],[],0
    #there is a count of | of mark the compartment/pipes
    # along with an memory array to restructure the given string into a list like [0, '*', '*', 1, '*', 2, '*'] f
    # or string |**|*|*
    for char in s:
        if char == '|':
            store_mem.append(count)
            count += 1
        else:
            store_mem.append("*")

    for i in range(len(starts)):
        #start and end for marking the end
        start = starts[i]-1
        end = ends[i]-1
        #loop within the compartment over the start and end index with incrementining start step and dectementing end
        while start < end and start < len(s) and store_mem[start] == "*":
            start += 1
        while start < end and end >= 0 and store_mem[end] == "*":
            end -= 1

        #no res if overflow or underflow
        if start >= len(s) or end < 0:
            res.append(0)
        else:
            try:
                res.append((end - start) - (store_mem[end] - store_mem[start]))
            except TypeError:
                res.append(0)
    return res


if __name__ == "__main__":
    test_cases = [
        ["|**|*|*", [1, 1], [5, 6]],
        ["*|*", [1], [3]],
        ["*|*|*|",[1,1],[1,6]]
    ]
    for test in test_cases:
        res = calculate(test[0], test[1], test[2])
        print(res)