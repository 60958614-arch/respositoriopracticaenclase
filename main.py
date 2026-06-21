#imprimir los n primeros numero naturales impares 
# n = 5 
# 1,3,5,7,9
print("============== serie de numeros impares ===================")
N = int(input("ingrese el primer valor de N: "))
#contador
i = 1
j = 1
while(i <= N):
    #instrucciones 
    print(f"#: {j}")
    j = j + 2
    i = i + 1