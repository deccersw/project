a,b=list(map(int,input("Введите два целых числа \n").split()))
op=str(input("Введите операцию над числами\n"))
if op =="+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op =="//":
    print("я не знаю о такой операции")
print("Вот вся магия чисел")

