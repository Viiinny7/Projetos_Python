def is_fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return f"{num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"{num} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero_informado = int(input("Informe um número: "))
print(is_fibonacci(numero_informado))