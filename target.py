#01
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)


#02
def fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")


#03
"""
a) 1, 3, 5, 7, ___
A lógica é adicionar 2 a cada termo. Portanto, o próximo elemento é 9.

b) 2, 4, 8, 16, 32, 64, ___
Cada termo é o dobro do anterior. O próximo elemento será 128.

c) 0, 1, 4, 9, 16, 25, 36, ___
Esses são os quadrados de números positivos, inteiros e consecutivos. O próximo elemento será 49, que é o quadrado de 7.

d) 4, 16, 36, 64, ___
Esses são os quadrados dos números positivos, pares e consecutivos. O próximo elemento será 100, que é o quadrado de 10.

e) 1, 1, 2, 3, 5, 8, ___
Esta sequência é a série de Fibonacci, onde cada termo é a soma dos dois anteriores. O próximo elemento será 13.

f) 2,10, 12, 16, 17, 18, 19, ____
2 tem a soma dos dígitos igual a 2.
10 tem a soma dos dígitos igual a 1.
12 tem a soma dos dígitos igual a 3.
16 tem a soma dos dígitos igual a 7.
17 tem a soma dos dígitos igual a 8.
18 tem a soma dos dígitos igual a 9.
19 tem a soma dos dígitos igual a 10.
Seguindo essa lógica, o próximo número que tem a soma dos seus dígitos igual a 2 é 20.

#04
Primeiro eu ligaria o interruptor de uma das pontas, iria verificar qual luz foi acesa. Depois desligaria o iterruptor que foi ligado anteriormente, ligaria o da ponta oposta e novamente verificar qual luz foi acesa. Assim, saberei quais luzes foram acesas, o interruptor que sobrou acenderá a útima luz.

"""

#05
def inverter_string(string):
    string_invertida = string[::-1]
    return string_invertida

string_original = input("Digite uma string: ")
string_invertida = inverter_string(string_original)
print("A string invertida é:", string_invertida)