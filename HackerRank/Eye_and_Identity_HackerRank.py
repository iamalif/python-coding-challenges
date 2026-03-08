import numpy

numpy.set_printoptions(legacy='1.13')

shape = list(map(int, input().split()))

print(numpy.eye(shape[0], shape[1]))

