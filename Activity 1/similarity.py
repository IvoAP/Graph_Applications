import numpy as np

number_vertices1 = None
number_vertices2 = None
vertices_list1 = [] 
vertices_list2 = []
adjacency_matrix1 = []
adjacency_matrix2 = []

def weighted_jaccard_similarity(adj_matrix1, adj_matrix2):
    max_shape = np.array((adj_matrix1.shape, adj_matrix2.shape)).max(axis=0)
    padded_matrix1 = np.pad(adj_matrix1, ((0, max_shape[0] - adj_matrix1.shape[0]), (0, max_shape[1] - adj_matrix1.shape[1])), 'constant')
    padded_matrix2 = np.pad(adj_matrix2, ((0, max_shape[0] - adj_matrix2.shape[0]), (0, max_shape[1] - adj_matrix2.shape[1])), 'constant')

    degrees1 = padded_matrix1.sum(axis=1)
    degrees2 = padded_matrix2.sum(axis=1)

    intersection_bool = np.logical_and(padded_matrix1, padded_matrix2)
    union_bool = np.logical_or(padded_matrix1, padded_matrix2)

    intersection = intersection_bool.astype(int)
    union = union_bool.astype(int)

    intersection_weighted = intersection * np.minimum(degrees1, degrees2).reshape(-1, 1)
    
    union_weighted = (padded_matrix1 * degrees1.reshape(-1, 1)) + (padded_matrix2 * degrees2.reshape(-1, 1))
    union_weighted -= intersection_weighted
    
    intersection_sum = np.sum(intersection_weighted)
    union_sum = np.sum(union_weighted)

    return intersection_sum / union_sum if union_sum != 0 else 0

def main():
    global number_vertices1, number_vertices2, vertices_list1, vertices_list2, adjacency_matrix1, adjacency_matrix2

    # Input Graph 1
    vertices_input1 = input("Enter all vertices of graph 1, separated by spaces: ")
    vertices_list1 = vertices_input1.split()
    number_vertices1 = len(vertices_list1)

    for i in range(number_vertices1):
        row = input(f"Enter the elements of row {i+1}, separated by spaces: ").split()
        adjacency_matrix1.append([int(x) for x in row])

    # Input Graph 2
    vertices_input2 = input("Enter all vertices of graph 2, separated by spaces: ")
    vertices_list2 = vertices_input2.split()
    number_vertices2 = len(vertices_list2)

    for i in range(number_vertices2):
        row = input(f"Enter the elements of row {i+1}, separated by spaces: ").split()
        adjacency_matrix2.append([int(x) for x in row])

    # Adajcency matrix to Array Numpy
    adjacency_matrix1 = np.array(adjacency_matrix1)
    adjacency_matrix2 = np.array(adjacency_matrix2)

    # Answer
    similarity = weighted_jaccard_similarity(adjacency_matrix1, adjacency_matrix2)
    print("Graph Similarity: ", similarity)

if __name__ == "__main__":
    main()
