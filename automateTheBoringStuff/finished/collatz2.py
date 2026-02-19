import sys

print(
    "A sequência collatz é o problema impossível mais simples da matemática. Qualquer número natural que você escolher chegará ao número 1, se você dividi-lo por 2 se ele for par, ou multiplicá-lo por 3 e somar um se ele for ímpar, e for fazendo isso com os resultados dessas operações, mas ninguém sabe o porquê disso acontecer. Pode ver."
)
exit = quit = 0


def collatz(n):
    while True:
        if n == 1:
            break
        elif n % 2 == 1:
            n = 3 * n + 1
        elif n % 2 == 0:
            n = n / 2
        print(n)


while True:
    try:
        n = int(input("Enter number:"))
        if n <= 0:
            print(
                "Mano, escreve um número natural ae, na boa, por favor, se você colocar algo que não é um número essa mensagem vai aparecer de novo, e ela é mó longa tlg?"
            )
            sys.exit
        else:
            collatz(n)
    except ValueError:
        print(
            "Mano, escreve um número natural ae, na boa, por favor, se você colocar algo que não é um número essa mensagem vai aparecer de novo, e ela é mó longa tlg?"
        )
        sys.exit
