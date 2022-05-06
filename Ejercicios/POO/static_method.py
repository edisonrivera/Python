#
# DECORATORS
#

class Algo():

    @staticmethod
    def add_x (x):
        return x + 5


print(Algo.add_x(5))