from platform import platform,machine,processor, system,version

print(platform(1,1))
print(platform(1,0))
print(platform())
print(machine())
print(processor())
print(version())
print(platform(1,1) + " " + machine() + " " + system())

from platform import python_implementation, python_version_tuple
print(python_implementation())
for atr in python_version_tuple():
    print(atr, end=".")