import numpy as np
input = []

def count_neighbors(mat, og_k, og_i, og_j):
    count = 0
    k_vals = {og_k-1,og_k,og_k+1}.intersection(set(range(mat.shape[0])))
    i_vals = {og_i-1,og_i,og_i+1}.intersection(set(range(mat.shape[1])))
    j_vals = {og_j-1,og_j,og_j+1}.intersection(set(range(mat.shape[2])))
    for k in k_vals:
        for i in i_vals:
            for j in j_vals:
                if not (k == og_k and i == og_i and j == og_j):
                    count += mat[k, i, j]
    return count


with open("17.in", "r") as file:
    for i, l in enumerate(file):
        l = l.strip()
        input.append(l)

#normally convention would be x*y*z
#but we might switch that to z*x*y for better readability
mat = np.zeros(shape=(1, len(input), len(input[0])))
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '#':
            mat[0,i,j] = 1

# print(mat)
# new_mat = np.zeros(shape=(mat.shape[0]+2, mat.shape[1]+2, mat.shape[2]+2))
# new_mat[1:mat.shape[0]+1, 1:mat.shape[1]+1, 1:mat.shape[2]+1] = mat
# print(count_neighbors(new_mat, 1,1,1))

for t in range(6):
    padded_mat = np.zeros(shape=(mat.shape[0]+2, mat.shape[1]+2, mat.shape[2]+2))
    padded_mat[1:mat.shape[0] + 1, 1:mat.shape[1] + 1, 1:mat.shape[2] + 1] = mat
    new_mat = np.zeros(shape=(mat.shape[0]+2, mat.shape[1]+2, mat.shape[2]+2))

    for k in range(padded_mat.shape[0]):
        for i in range(padded_mat.shape[1]):
            for j in range(padded_mat.shape[2]):
                n = count_neighbors(padded_mat, k, i, j)
                if padded_mat[k,i,j]:
                    if n == 2 or n == 3:
                        new_mat[k,i,j] = 1
                else:
                    if n == 3:
                        new_mat[k,i,j] = 1
    mat = new_mat

print(np.sum(mat))