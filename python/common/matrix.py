
def add_matrix_2_matrix(destination, source, start_x, start_y):
    for j in range(source.shape[0]):
        for i in range(source.shape[1]):
            if 0 < j <= destination.shape[0] and 0 < i <= destination.shape[1]:
                destination[start_y + j, start_x + i] = source.item(j, i)