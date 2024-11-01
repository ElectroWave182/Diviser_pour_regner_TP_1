from random import randint


def cherche(x, t): # t est une liste d'entiers triée

    # Précondition
    n = len(t)
    for ind in range(n - 1):
        assert t[ind + 1] >= t[ind], "Précondition, liste non triée"

    milieu = n // 2

    # Cas d'arrêt
    if n == 0:
        sortie = False
    elif x == t[milieu]:
        sortie = True

    # Cas récursif
    elif x < milieu:
        sortie = cherche(x, t[: milieu])
    else:
        sortie = cherche(x, t[milieu + 1 :])

    # Postcondition
    assert n == len(t), "Postcondition, la liste a été modifiée"
    for ind in range(n - 1):
        assert t[ind + 1] >= t[ind], "Postcondition, liste non triée"
    
    return sortie
    

# Tests
for nb in range(10):
    t = [randint(0, 10) for _ in range(10)]
    t.sort()
    x = randint(0, 10)
    assert cherche(x, t) == x in t, "Tests non concluants"