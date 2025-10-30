import math

def tangente(angulo_graus):
    """Retorna a tangente de um ângulo em graus."""
    angulo_radianos = math.radians(angulo_graus)
    return math.tan(angulo_radianos)

# Exemplo de uso:
print(tangente(45))   # → 1.0
print(tangente(60))   # → 1.732...
print(tangente(90))   # → valor muito grande (tangente indefinida)
