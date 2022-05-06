from re import findall, search

lista = ["Spreen - YouTube",
        "Hola - YouTube",
        "Juanito565 - YouTube",
        "Lolito Fz - YouTube"
    ]

for item in lista:
    resutados_filtrados = (r"[(A-Za-z)$] - YouTube",item)

print (resutados_filtrados)

str = 'an example word:cat!!'
match = search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print(match.group()) ## 'found word:cat'
else:
  print('did not find')

str = "pad192  @qew"

mat = findall(r"\d+\s*\@", str)
print(mat)
#print(mat.group())