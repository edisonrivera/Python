import pandas as pd

x = [1,3,5,7]
y = [2,4,6,8]

graph = pd.DataFrame(y,x)
graph.plot(kind="line")