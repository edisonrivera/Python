from os import chdir, getcwd


#TÓPICO 1) getcwd, chdir
# getcwd = Da como salida el directorio de trabajo actual.
# chdir = Cambia el directorio de trabajo.

# 1.1 Ejemplo de getcwd
cwd = getcwd()
print("Current directory working...",cwd)

# 1.2 Ejemplo de chdir

cwd_before_chdir = getcwd()
print("Current directory...", cwd_before_chdir)

other_dir = "C:\\Users\\pc\\Videos" #Dir al que se cambiará
chdir(other_dir)

cwd_after_chdir = getcwd()
print("Use \"chdir()\" directory...", cwd_after_chdir)