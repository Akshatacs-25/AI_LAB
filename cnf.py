def eliminate_implication(expr):
    expr = expr.replace("->", "|")
    return expr


def distribute_or(expr):
    return expr


def convert_to_cnf(expr):
    expr = eliminate_implication(expr)
    expr = distribute_or(expr)
    return expr


print("Enter a propositional logic expression:")
expression = input()

cnf = convert_to_cnf(expression)

print("CNF:", cnf)
