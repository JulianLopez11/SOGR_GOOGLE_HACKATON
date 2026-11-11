def parentingParteringReturns(actividades):

    n = len(actividades)
    orden = []
    for i in range(n):
        inicio, fin = actividades[i]
        orden.append((inicio, fin, i))
    orden.sort()
    asignacion = [""] * n
    finCameron = 0
    finJamie = 0
    for inicio, fin, i in orden:
        if finCameron <= inicio:
            asignacion[i] = "C"
            finCameron = fin
        elif finJamie <= inicio:
            asignacion[i] = "J"
            finJamie = fin
        else:
            return "IMPOSSIBLE"
    return "".join(asignacion)


def main():
    casos = int(input())
    for caso in range(1, casos + 1):
        n = int(input())
        actividades = []
        for _ in range(n):
            inicio, fin = map(int, input().split())
            actividades.append([inicio, fin])
        print(f"Case #{caso}: {parentingParteringReturns(actividades)}")

main()
