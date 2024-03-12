def fibonacci(max):
    a, b = 0, 1
    print("0")
    while b <= int(max):
        print(b)
        a, b = b, a + b
    return a

max_num = input("Digite um número: ")
if fibonacci(max_num)==int(max_num):
    print("Pertence")
else:
    print("Não Pertence")