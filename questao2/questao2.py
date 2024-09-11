import math

# Função para verificar se um número é um quadrado perfeito
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

# Função para verificar se o número pertence à sequência de Fibonacci
def pertence_fibonacci(n):
    # Verifica as duas condições matemáticas
    cond1 = 5 * n * n + 4
    cond2 = 5 * n * n - 4
    if is_perfect_square(cond1) or is_perfect_square(cond2):
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

# Exemplo de número informado
numero_informado = 21
print(pertence_fibonacci(numero_informado))