import numpy as np

np.set_printoptions(legacy='1.13')

input_list = list(map(float, input().split()))

#floor_array = np.array(input_list)
floor_array = np.floor(np.array(input_list))

#ceil_array = np.array(input_list)
ceil_array = np.ceil(np.array(input_list))

#rint_array = np.array(input_list)
rint_array = np.rint(np.array(input_list))

print(floor_array)
print(ceil_array)
print(rint_array)
