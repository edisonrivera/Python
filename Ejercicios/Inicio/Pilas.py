apilar = [1,2,3]
apilar.append(4)
apilar.append(5)
print(apilar)
# del apilar[-1] Totalmente funcional
apilar.pop() #Retiramos el último elemento
print(apilar)
apilar.insert(0,100)
print(apilar)
print(apilar.count(1))
apilar.reverse()
print(apilar)