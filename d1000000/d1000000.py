def d1000000(dados):

    dados.sort()
    largo = 0
    for s in dados:
        if s > largo:
            largo += 1
    return largo


def main():
    casos = int(input())
    for caso in range(1, casos + 1):
        n = int(input())
        dados = list(map(int, input().split()))
        print(f"Case #{caso}: {d1000000(dados)}")

main()
