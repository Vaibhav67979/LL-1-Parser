diction = {}
firsts = {}
follows = {}
rules = ["S -> a B | a c | S d | S e",
         "B -> b B c | f",
         "C -> g"]

nonterm_userdef = ['S', 'B', 'C']
term_userdef = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
sample_input_string = "a c"
# start_symbol = list(diction.keys())[0]

