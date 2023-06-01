def parse(expr, parse_table, terminals, non_terminals):
    stack = ["$"]
    stack.insert(0, non_terminals[0])

    print("\t\t\tMatched\t\t\tStack\t\t\tInput\t\t\tAction\n")
    print("\t\t\t-\t\t\t", end="")
    for i in stack:
        print(i, end="")
    print("\t\t\t", end="")
    print(expr + "\t\t\t", end="")
    print("-")

    matched = "-"
    while (True):
        action = "-"

        if (stack[0] == expr[0] and stack[0] == "$"):
            break

        elif (stack[0] == expr[0]):
            if (matched == "-"):
                matched = expr[0]
            else:
                matched = matched + expr[0]
            action = "Matched " + expr[0]
            expr = expr[1:]
            stack.pop(0)

        else:
            action = parse_table[non_terminals.index(stack[0])][terminals.index(expr[0])]
            stack.pop(0)
            i = 0
            for item in action[2:]:
                if (item != "`"):
                    stack.insert(i, item)
                i += 1

        print("\t\t\t" + matched + "\t\t\t", end="")
        for i in stack:
            print(i, end="")
        print("\t\t\t", end="")
        print(expr + "\t\t\t", end="")
        print(action)