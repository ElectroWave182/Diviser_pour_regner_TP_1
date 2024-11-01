def point_fixe(t): # t est une liste d'entiers triée

    # Précondition
    n = len(t)
    assert n > 0, "Précondition, la liste est vide"
    for ind in range(n - 1):
        assert t[ind + 1] > t[ind], "Précondition, liste non triée"

    milieu = n // 2
    x = t[milieu]

    # Cas d'arrêt
    if n == 0:
        sortie = False
    elif x = milieu:
        sortie = True

    # Cas récursif
    elif x > milieu:
        sortie = point_fixe(t[: milieu])
    else:
        for ind in range(milieu + 1, n):
            t[ind] -= milieu + 1
        sortie = point_fixe(t[milieu + 1 :])

    # Postcondition
    assert n == len(t), "Postcondition, la liste a été modifiée"
    for ind in range(n - 1):
        assert t[ind + 1] >= t[ind], "Postcondition, liste non triée"
    
    return sortie