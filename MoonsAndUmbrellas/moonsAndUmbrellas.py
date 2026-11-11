def costo(anterior, actual, x, y):
    if anterior == "C" and actual == "J":
        return x
    if anterior == "J" and actual == "C":
        return y
    return 0


def moonsAndUmbrellas(x, y, mural):

    n = len(mural)
    INF = float("inf")
    dp = [{"C": INF, "J": INF} for _ in range(n)]
    for letra in "CJ":
        if mural[0] in (letra, "?"):
            dp[0][letra] = 0
    for i in range(1, n):
        for letra in "CJ":
            if mural[i] in (letra, "?"):
                dp[i][letra] = min(
                    dp[i - 1]["C"] + costo("C", letra, x, y),
                    dp[i - 1]["J"] + costo("J", letra, x, y),
                )
    return min(dp[n - 1].values())


def main():
    casos = int(input())
    for caso in range(1, casos + 1):
        datos = input().split()
        x = int(datos[0])
        y = int(datos[1])
        mural = datos[2]
        print(f"Case #{caso}: {moonsAndUmbrellas(x, y, mural)}")

main()
