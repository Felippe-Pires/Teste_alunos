from math import sin


def cossecante(valor):
    if sin(valor) == 0:
        raise ValueError(
            "O ângulo resulta em uma cossecante indefinida (divisão por zero)."
        )
    return 1 / sin(valor)


if __name__ == "__main__":
    angulo = float(input("Digite o ângulo em radianos: "))
    try:
        resultado = cossecante(angulo)
        print(f"A cossecante de {angulo} radianos é: {resultado}")
    except ValueError as e:
        print(e)
