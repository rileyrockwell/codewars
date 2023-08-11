# Collaborator: P. Domitrovich

def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix) > 2:
        sum = 0
        for i in range(len(matrix)):
            # review
            cofactor = matrix[0][i] * (-1)**(1 + i + 1)
            # "throw out" the first column and first row
            minor = []
            for j in range(len(matrix)):
                if j == 0:
                    continue
                temp_list = []
                for k in range(len(matrix)):
                    if k == i:
                        continue
                    else:
                        temp_list.append(matrix[j][k])
                minor.append(temp_list)
            print("minor:", minor)
            sum += cofactor * determinant(minor)
        return sum


print(determinant([[1, 2], [3, 4]]))
print(determinant([[1, 1], [1, 1]]))
print(determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(determinant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))