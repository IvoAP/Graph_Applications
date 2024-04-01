from itertools import permutations

number_vertices1 = None
number_vertices2 = None
vertices_list1 = [] 
vertices_list2 = []
adjacency_matrix1 = []
adjacency_matrix2 = []
flag_number_vertices = False
flag_number_edges = False
flag_degrees_graphs = False
flag_check_bijection = False


# Function to print adjacency list
def print_adjacency_matrix(matrix):
    print("Adjacency Matrix:")
    for row in matrix:
        print(' '.join(map(str, row)))



# Function to verify number of vertices
def check_number_of_vertices_of_graphs(n1,n2):
  return n1 == n2

# Function to verify number of edges 
def check_number_of_edges_graphs(matrix1, matrix2):
    count_edges_graph1 = [row.count(1) for row in matrix1]
    count_edges_graph2 = [row.count(1) for row in matrix2]
    sum(count_edges_graph1)
    return sum(count_edges_graph1) == sum(count_edges_graph2)

# Function to verify the degree of each vertice if they correpond     
def check_degree_of_graphs(matrix1, matrix2 , number_vertices1, number_vertices2):
    degree_graph1 = [0] * number_vertices1
    degree_graph2 = [0] * number_vertices2

    for i, row in enumerate(matrix1):
        degree_graph1[i] = row.count(1)
    
    for i, row in enumerate(matrix2):
        degree_graph2[i] = row.count(1)

    degree_graph1.sort()
    degree_graph2.sort()

    return  degree_graph1 == degree_graph2

#Function to Bijection    
def check_bijection(matrix1, matrix2):
    n1, n2 = len(matrix1), len(matrix2)
    if n1 != n2:
        return False
    
    for permutation in permutations(range(n1)):
        bijection_found = True  
        for i in range(n1):
            row_permutada = [matrix1[i][j] for j in permutation]
            if row_permutada not in matrix2:
                bijection_found = False 
                break
        if bijection_found:
            return True
    return False


    

def main():
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
   
    # CHeck the flags
    flag_number_vertices = check_number_of_vertices_of_graphs(number_vertices1,number_vertices2)
    if(flag_number_vertices == False):
        print("They are not isomorphic because they have a different number of vertices.")
        return
    
    flag_number_edges = check_number_of_edges_graphs(adjacency_matrix1, adjacency_matrix2)
    if(flag_number_edges == False):
        print("They are not isomorphic because they have a different number of edges.")
        return
    
    flag_degrees_graphs = check_degree_of_graphs(adjacency_matrix1, adjacency_matrix2, number_vertices1, number_vertices2)
    if(flag_degrees_graphs == False):
        print("They are not isomorphic because they have a different number of degrees.")
        return
    
    flag_check_bijection =check_bijection(adjacency_matrix1,adjacency_matrix2)
    if(flag_check_bijection == False):
        print("They are not isomorphic because they don't have the same bijection function.")
        return
    
    if flag_check_bijection and flag_degrees_graphs and flag_number_edges and flag_number_vertices:
        print("The graphs are isomorphic.")

    # print_adjacency_matrix(adjacency_matrix1)


if __name__ == "__main__":
    main()

# Case 1 :  Invalid
# Case 2 :  Invalid
# Case 3 :  Isomorphic
# Case 4 :  Isomoprhic
# Case 5 :  Invalid