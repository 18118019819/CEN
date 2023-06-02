import numpy as np
from numpy import array

snap_list = [array([[1,2,3],
                   [4,5,6],
                   [7,8,9]]),
            array([[11,22,33],
                   [44,55,66],
                   [77,88,99]])]

for triples in snap_list:
    inverse_triples = triples[:, [2, 1, 0]]
    print(inverse_triples)
    # print(inverse_triples[:, 1])



# snapshot_list = [array([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]])]

# for snapshot in snapshot_list:
#     uniq_v, edges = np.unique((snapshot[:,0], snapshot[:,2]), return_inverse=True)
#     edges = np.reshape(edges, (2, -1))
#     print(edges)