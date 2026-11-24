def tt_entails(KB, alpha):
    symbols = list(set(KB + alpha))
    return tt_check_all(KB, alpha, symbols, {})


def tt_check_all(KB, alpha, symbols, model):

    # If all symbols have been assigned
    if not symbols:
        if pl_true(KB, model):
            return pl_true(alpha, model)
        else:
            return True

    # Select first symbol
    P = symbols[0]
    rest = symbols[1:]

    # Check P = True
    model_true = model.copy()
    model_true[P] = True

    # Check P = False
    model_false = model.copy()
    model_false[P] = False

    return (tt_check_all(KB, alpha, rest, model_true)
            and
            tt_check_all(KB, alpha, rest, model_false))


# Evaluate a propositional logic expression
def pl_true(expression, model):
    return eval(expression, {}, model)


# Example
KB = ["P or Q", "not P or R"]
alpha = "Q or R"

result = tt_entails(KB, alpha)

if result:
    print("KB entails alpha (True)")
else:
    print("KB does not entail alpha (False)")
