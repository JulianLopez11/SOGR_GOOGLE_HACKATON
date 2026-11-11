def chainReactions(n, diversion, punteros):

    hijos = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        hijos[punteros[i - 1]].append(i)
    valor = [0] * (n + 1)
    total = 0
    for modulo in range(n, -1, -1):
        if not hijos[modulo]:
            valor[modulo] = diversion[modulo - 1]
            continue
        valores_hijos = [valor[hijo] for hijo in hijos[modulo]]
        menor = min(valores_hijos)
        total += sum(valores_hijos) - menor
        if modulo == 0:
            total += menor
        else:
            valor[modulo] = max(diversion[modulo - 1], menor)
    return total


def main():
    casos = int(input())
    for caso in range(1, casos + 1):
        n = int(input())
        diversion = list(map(int, input().split()))
        punteros = list(map(int, input().split()))
        print(f"Case #{caso}: {chainReactions(n, diversion, punteros)}")

main()
