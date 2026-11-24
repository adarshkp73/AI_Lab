
def unify(x, y, theta):
    if x == y:
        return theta

    if isinstance(x, str) and x.startswith("?"):
        if x in theta:
            return unify(theta[x], y, theta)
        theta[x] = y
        return theta

    if isinstance(x, tuple) and isinstance(y, tuple):
        for a, b in zip(x, y):
            theta = unify(a, b, theta)
            if theta is None:
                return None
        return theta

    return None


def substitute(x, theta):
    if isinstance(x, str) and x.startswith("?"):
        return theta.get(x, x)

    if isinstance(x, tuple):
        return tuple(substitute(a, theta) for a in x)

    return x


def match(premises, facts, theta={}):
    if not premises:
        return [theta]

    results = []

    for fact in facts:
        t = unify(substitute(premises[0], theta), fact, theta.copy())

        if t is not None:
            results += match(premises[1:], facts, t)

    return results


def FOL_FC_ASK(KB, query):
    while True:
        new = set()

        for premises, conclusion in KB["rules"]:

            for theta in match(premises, KB["facts"]):
                q = substitute(conclusion, theta)

                if q not in KB["facts"]:
                    new.add(q)

                if unify(query, q, {}) is not None:
                    return True

        if not new:
            return False

        KB["facts"].update(new)


# Knowledge Base
KB = {
    "facts": {
        ("Parent", "John", "Mary"),
        ("Parent", "Mary", "Sam")
    },

    "rules": [
        (
            [("Parent", "?x", "?y"),
             ("Parent", "?y", "?z")],

            ("Grandparent", "?x", "?z")
        )
    ]
}

# Query
query = ("Grandparent", "John", "Sam")

print(FOL_FC_ASK(KB, query))
