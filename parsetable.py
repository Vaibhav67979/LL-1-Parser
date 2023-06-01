from main import terminals, non_terminals
from tabulate import tabulate


def get_rule(non_terminal, terminal, grammar, grammar_first):
    for rhs in grammar[non_terminal]:
        # print(rhs)
        for rule in rhs:
            if rule == terminal:
                string = non_terminal + "~" + rhs
                return string

            elif rule.isupper() and terminal in grammar_first[rule]:
                string = non_terminal + "~" + rhs
                return string


def generate_parse_table(terminals, non_terminals, grammar, grammar_first, grammar_follow):
    parse_table = [[""] * len(terminals) for i in range(len(non_terminals))]

    for non_terminal in non_terminals:
        for terminal in terminals:
            # print(terminal)
            # print(grammar_first[non_terminal])
            if terminal in grammar_first[non_terminal]:
                rule = get_rule(non_terminal, terminal, grammar, grammar_first)
                # print(rule)

            elif "`" in grammar_first[non_terminal] and terminal in grammar_follow[non_terminal]:
                rule = non_terminal + "~`"

            elif terminal in grammar_follow[non_terminal]:
                rule = "Sync"

            else:
                rule = ""

            parse_table[non_terminals.index(non_terminal)][terminals.index(terminal)] = rule

    return parse_table


def display_parse_table(parse_table, terminal, non_terminal):
    print("\t\t\t\t", end="")
    for terminal in terminals:
        print(terminal + "\t\t", end="")
    print("\n\n")

    for non_terminal in non_terminals:
        print("\t\t" + non_terminal + "\t\t", end="")
        for terminal in terminals:
            print(parse_table[non_terminals.index(non_terminal)][terminals.index(terminal)] + "\t\t", end="")
        print("\n")

    print(tabulate(parse_table, headers=terminals))
