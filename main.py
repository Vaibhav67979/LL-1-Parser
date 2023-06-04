from leftRecursion import removeLeftRecursion
from leftFactoring import LeftFactoring
from first import computeAllFirsts
from follow import computeAllFollows
from parseTable import createParseTable
from parser import parsingUsingStackBuffer
from input import rules, diction, firsts, follows, nonterm_userdef, term_userdef, sample_input_string


computeAllFirsts(diction)
start_symbol = list(diction.keys())[0]
computeAllFollows()

(parsing_table, result, tabTerm) = createParseTable()

if sample_input_string != None:
    validity = parsingUsingStackBuffer(parsing_table, result,
                                       tabTerm, sample_input_string,
                                       term_userdef, start_symbol)
    print(validity)
else:
    print("\nNo input String detected")
