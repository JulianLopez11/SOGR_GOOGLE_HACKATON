def bathRoomStalls(n, k):

    grupos = {n: 1}
    while True:
        mayor = max(grupos)
        cantidad = grupos.pop(mayor)
        izquierda = (mayor - 1) // 2
        derecha = mayor - 1 - izquierda
        if k <= cantidad:
            return derecha, izquierda
        k -= cantidad
        grupos[derecha] = grupos.get(derecha, 0) + cantidad
        grupos[izquierda] = grupos.get(izquierda, 0) + cantidad


def main():
    casos = int(input())
    for caso in range(1, casos + 1):
        n, k = map(int, input().split())
        maximo, minimo = bathRoomStalls(n, k)
        print(f"Case #{caso}: {maximo} {minimo}")

main()
