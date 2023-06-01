from collections import OrderedDict
from first import first, insert, isterminal
from follow import follow, rec_follow
from parsetable import generate_parse_table, display_parse_table
from parser import parse


def show_dict(dictionary):
    for key in dictionary.keys():
        print(key + "  :  ", end="")
        for item in dictionary[key]:
            if (item == "`"):
                print("Epsilon, ", end="")
            else:
                print(item + ", ", end="")
        print("\b\b")


grammar = OrderedDict()
grammar_first = OrderedDict()
grammar_follow = OrderedDict()

f = open('grammer.txt')
for i in f:
    i = i.replace("\n", "")
    lhs = ""
    rhs = ""
    flag = 1
    for j in i:
        if (j == "~"):
            flag = (flag + 1) % 2
            continue
        if (flag == 1):
            lhs += j
        else:
            rhs += j
    grammar = insert(grammar, lhs, rhs)
    grammar_first[lhs] = "null"
    grammar_follow[lhs] = "null"

print("Grammar\n")
show_dict(grammar)

for lhs in grammar:
    if (grammar_first[lhs] == "null"):
        grammar_first = first(lhs, grammar, grammar_first)

print("\n\n\n")
print("First\n")
show_dict(grammar_first)

start = list(grammar.keys())[0]
for lhs in grammar:
    if (grammar_follow[lhs] == "null"):
        grammar_follow = follow(lhs, grammar, grammar_follow, start)

print("\n\n\n")
print("Follow\n")
show_dict(grammar_follow)

non_terminals = list(grammar.keys())
terminals = []

for i in grammar:
    for rule in grammar[i]:
        for char in rule:

            if (isterminal(char) and char not in terminals):
                terminals.append(char)

terminals.append("$")

# print(non_terminals)
# print(terminals)


print("\n\n\n\n\t\t\t\t\t\t\tParse Table\n\n")
parse_table = generate_parse_table(terminals, non_terminals, grammar, grammar_first, grammar_follow)
display_parse_table(parse_table, terminals, non_terminals)

# expr = input("Enter the expression ending with $ : ")
# expr = "i+i*i$"
#
# print("\n\n\n\n\n\n")
# print("\t\t\t\t\t\t\tParsing Expression\n\n")
# parse(expr, parse_table, terminals, non_terminals)