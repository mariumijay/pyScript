# ---------------------------------------
# 3. Python Libraries
# ---------------------------------------

# i. Import & Install Numpy
# Install numpy using: pip install numpy (run this in terminal if not already installed)
import numpy as np

# ---------------------------------------
# 4. Creating Arrays with NumPy
# ---------------------------------------

# i. Print the array [1, 2, 3, 4, 5] and its datatype using numpy
arr1 = np.array([1, 2, 3, 4, 5])
print("Question: Print the array [1, 2, 3, 4, 5] and its datatype using numpy")
print("Answer:", arr1)
print("Datatype:", arr1.dtype)

# ii. Use a tuple to create a NumPy array
arr2 = np.array((10, 20, 30))
print("\nQuestion: Use a tuple to create a NumPy array")
print("Answer:", arr2)

# iii. Print 0-D array
arr0D = np.array(42)
print("\nQuestion: Print 0-D array")
print("Answer:", arr0D)

# iv. Print 1-D array
arr1D = np.array([1, 2, 3, 4])
print("\nQuestion: Print 1-D array")
print("Answer:", arr1D)

# v. Print 2-D array
arr2D = np.array([[1, 2], [3, 4]])
print("\nQuestion: Print 2-D array")
print("Answer:\n", arr2D)

# vi. Print 3-D array
arr3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nQuestion: Print 3-D array")
print("Answer:\n", arr3D)

# vii. Print N-D array (example: 4-D)
arrND = np.array([[[[1], [2]], [[3], [4]]]])
print("\nQuestion: Print N-D array")
print("Answer:\n", arrND)
print("Number of Dimensions:", arrND.ndim)

# ---------------------------------------
# 5. Array Attributes
# ---------------------------------------

import numpy as np

# i. Print an array of evenly spaced numbers up to 24
arr1 = np.linspace(0, 24, 25)  # Generates 25 evenly spaced numbers from 0 to 24
print("Question: Print an array of evenly spaced numbers up to 24")
print("Answer:", arr1)

# ii. Print the size of 2-D array using shape
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print("\nQuestion: Print the size of 2-D array using shape")
print("Answer (Shape):", arr2D.shape)

# iii. Print the size of 2-D array using ndarray.size
print("\nQuestion: Print the size of 2-D array using ndarray.size")
print("Answer (Size):", arr2D.size)

# iv. Print the datatype of 2-D array using ndarray.dtype
print("\nQuestion: Print the datatype of 2-D array using ndarray.dtype")
print("Answer (Datatype):", arr2D.dtype)

# v. Print the itemsize of 2-D array
print("\nQuestion: Print the itemsize of 2-D array")
print("Answer (Itemsize):", arr2D.itemsize)


# ---------------------------------------
# 6. Array Indexing
# ---------------------------------------

# i. Print 2nd element on 1st dim using array indexing
print("\nQuestion: Print 2nd element on 1st dim using array indexing")
print("Answer:", arr2D[1])

# ii. Print 5th element on 2nd dim using array indexing
print("\nQuestion: Print 5th element on 2nd dim using array indexing")
print("Answer:", arr2D[1, 1])

# iii. Access the third element of the second array of the first array
print("\nQuestion: Access the third element of the second array of the first array")
print("Answer:", arr2D[0, 2])

# iv. Write a Python program using NumPy to create a 1D array with values from 1 to 9. Then, extract specific elements from the array using both positive and negative indexing, and display the selected elements.
arr1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("\nQuestion: Extract specific elements using positive and negative indexing")
print("Answer (Positive Indexing):", arr1D[2], arr1D[5])
print("Answer (Negative Indexing):", arr1D[-7], arr1D[-4])

# v. Develop a Python program using NumPy to create a 2-dimensional array with two rows. Retrieve and display the last element of the second row using negative indexing.
arr2D_new = np.array([[10, 20, 30], [40, 50, 60]])
print("\nQuestion: Retrieve the last element of the second row using negative indexing")
print("Answer (Last element of second row):", arr2D_new[1, -1])

# ---------------------------------------
# 7. Numpy Slicing Arrays
# ---------------------------------------

import numpy as np

# i. Arrange elements from 0 to 19 using numpy slicing
arr1 = np.arange(20)  # Array from 0 to 19
print("Question: Arrange elements from 0 to 19 using numpy slicing")
print("Answer:", arr1)

# ii. Print elements from 10 to 19 using : operator in numpy slicing
print("\nQuestion: Print elements from 10 to 19 using : operator in numpy slicing")
print("Answer:", arr1[10:20])

# iii. Slice elements from index 1 to index 5
print("\nQuestion: Slice elements from index 1 to index 5")
print("Answer:", arr1[1:6])

# iv. Slice from the index 3 from the end to index 1 from the end
print("\nQuestion: Slice from index 3 from the end to index 1 from the end")
print("Answer:", arr1[-3:-1])

# v. Slice elements from the beginning to index 4
print("\nQuestion: Slice elements from the beginning to index 4")
print("Answer:", arr1[:5])

# vi. Slice elements from index 4 to the end of the array
print("\nQuestion: Slice elements from index 4 to the end of the array")
print("Answer:", arr1[4:])

# vii. Return every other element from index 1 to index 5 using Step in slicing
print("\nQuestion: Return every other element from index 1 to index 5 using Step in slicing")
print("Answer:", arr1[1:6:2])

# viii. Return every other element from the entire array using Step in slicing
print("\nQuestion: Return every other element from the entire array using Step in slicing")
print("Answer:", arr1[::2])

# ix. Slice 2-D array from the second element, slice elements from index 1 to index 4 (not included)
arr2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("\nQuestion: Slice 2-D array from the second element, slice elements from index 1 to index 4 (not included)")
print("Answer:\n", arr2D[1, 1:4])

# x. Slice 2-D array from both elements, return index 2
print("\nQuestion: Slice 2-D array from both elements, return index 2")
print("Answer:\n", arr2D[:, 2])

# xi. Slice 2-D array from both elements, slice index 1 to index 4 (not included), this will return a 2-D array
print("\nQuestion: Slice 2-D array from both elements, slice index 1 to index 4 (not included), this will return a 2-D array")
print("Answer:\n", arr2D[:, 1:4])

# xii. Print multi-dimensional ndarray
print("\nQuestion: Print multi-dimensional ndarray")
arr3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Answer:\n", arr3D)

# xiii. Slice single element in array
print("\nQuestion: Slice single element in array")
print("Answer:", arr1[3])


import numpy as np
from scipy import stats

# ---------------------------------------
# 8. Array creation Routines
# ---------------------------------------

# i. Print an array of given shape and type, filled with zeros
arr_zeros = np.zeros((3, 4), dtype=int)
print("Question: Print an array of given shape and type, filled with zeros")
print("Answer:\n", arr_zeros)

# ii. Print an array of given shape and type, filled with ones
arr_ones = np.ones((2, 3), dtype=float)
print("\nQuestion: Print an array of given shape and type, filled with ones")
print("Answer:\n", arr_ones)

# iii. Creates 2D array with ones on the diagonal and zeros elsewhere
arr_diag = np.eye(4, dtype=int)
print("\nQuestion: Creates 2D array with ones on the diagonal and zeros elsewhere")
print("Answer:\n", arr_diag)

# iv. Print the provided output using numpy.identity()
arr_identity = np.identity(4, dtype=int)
print("\nQuestion: Print the provided output using numpy.identity()")
print("Answer:\n", arr_identity)

# v. Creates an array with a specified range
arr_range = np.arange(0, 10, 2)
print("\nQuestion: Creates an array with a specified range")
print("Answer:", arr_range)

# vi. Interpret the input as a matrix
arr_matrix = np.matrix([[1, 2], [3, 4]])
print("\nQuestion: Interpret the input as a matrix")
print("Answer:\n", arr_matrix)

# vii. Converts a sequence type into a numpy array
arr_seq = np.array([1, 2, 3, 4])
print("\nQuestion: Converts a sequence type into a numpy array")
print("Answer:", arr_seq)


# ---------------------------------------
# 9. Numpy Arithmetic Operations
# ---------------------------------------

# i. Performing addition using arithmetic operator
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("\nQuestion: Performing addition using arithmetic operator")
print("Answer:", arr1 + arr2)

# ii. Performing addition using numpy function
print("\nQuestion: Performing addition using numpy function")
print("Answer:", np.add(arr1, arr2))

# iii. Performing subtraction using arithmetic operator
print("\nQuestion: Performing subtraction using arithmetic operator")
print("Answer:", arr1 - arr2)

# iv. Performing subtraction using numpy function
print("\nQuestion: Performing subtraction using numpy function")
print("Answer:", np.subtract(arr1, arr2))

# v. Performing multiplication using arithmetic operator
print("\nQuestion: Performing multiplication using arithmetic operator")
print("Answer:", arr1 * arr2)

# vi. Performing multiplication using numpy function
print("\nQuestion: Performing multiplication using numpy function")
print("Answer:", np.multiply(arr1, arr2))

# vii. Performing division using arithmetic operator
print("\nQuestion: Performing division using arithmetic operator")
print("Answer:", arr1 / arr2)

# viii. Performing division using numpy function
print("\nQuestion: Performing division using numpy function")
print("Answer:", np.divide(arr1, arr2))

# ix. Performing mod on two matrices
print("\nQuestion: Performing mod on two matrices")
print("Answer:", np.mod(arr1, arr2))

# x. Performing remainder on two matrices
print("\nQuestion: Performing remainder on two matrices")
print("Answer:", np.remainder(arr1, arr2))

# xi. Performing mean of all numbers in matrix 'a'
a = np.array([[1, 2, 3], [4, 5, 6]])
print("\nQuestion: Performing mean of all numbers in matrix 'a'")
print("Answer:", np.mean(a))

# xii. Calculate average of all numbers in an array
print("\nQuestion: Calculate average of all numbers in an array")
print("Answer:", np.average(a))

# xiii. Calculate sum of all numbers in an array
print("\nQuestion: Calculate sum of all numbers in an array")
print("Answer:", np.sum(a))

# xiv. Calculate variance of all numbers in an array
print("\nQuestion: Calculate variance of all numbers in an array")
print("Answer:", np.var(a))

# xv. Calculate power where one array as base and returns it raised to the power of the corresponding element in the second array
b = np.array([1, 2, 3])
print("\nQuestion: Calculate power where one array as base and returns it raised to the power of the corresponding element in the second array")
print("Answer:", np.power(a, b))

# xvi. Calculate maximum in an array
print("\nQuestion: Calculate maximum in an array")
print("Answer:", np.max(a))

# xvii. Calculate median in an array
print("\nQuestion: Calculate median in an array")
print("Answer:", np.median(a))

# xviii. Calculate minimum in an array
print("\nQuestion: Calculate minimum in an array")
print("Answer:", np.min(a))

# xix. Calculate the percentile in an array
print("\nQuestion: Calculate the percentile in an array")
print("Answer:", np.percentile(a, 50))  # 50th percentile (median)

# xx. Calculate the standard deviation
print("\nQuestion: Calculate the standard deviation")
print("Answer:", np.std(a))

# xxi. Calculate the harmonic mean of an array
print("\nQuestion: Calculate the harmonic mean of an array")
print("Answer:", stats.hmean(a))


# ---------------------------------------
# 10. Task 1: Understanding the Problem (8-puzzle problem)
# ---------------------------------------

# The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with 8 tiles and one blank space.
# The goal is to arrange the tiles in a specific goal state (usually ordered numerically).

# The initial state and goal state are defined as follows:

initial_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state is usually this

# The valid moves can be up, down, left, right, depending on where the blank (0) is located.
# For example, if the blank is in the middle, it can move up, down, left, or right.

print("\nQuestion: 8-puzzle problem initialization")
print("Initial State:\n", np.array(initial_state))
print("Goal State:\n", np.array(goal_state))

from collections import deque

# BFS for 8-puzzle problem
def bfs(initial_state, goal_state):
    # Helper functions
    def is_goal(state):
        return state == goal_state
    
    def get_neighbors(state):
        # Get neighbors by moving the blank space (0)
        neighbors = []
        row, col = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in state]
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                neighbors.append(new_state)
        return neighbors

    # BFS Implementation
    queue = deque([(initial_state, [])])  # Queue holds the state and the sequence of moves taken to reach that state
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))  # Make state hashable for the visited set

    while queue:
        state, path = queue.popleft()
        
        if is_goal(state):
            return path  # Return the sequence of moves
        
        for neighbor in get_neighbors(state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                queue.append((neighbor, path + [neighbor]))  # Append the neighbor and the path taken so far
    
    return "Goal state is not reachable"

# Test BFS
initial_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Same as initial for simplicity
bfs_solution = bfs(initial_state, goal_state)
print("BFS Solution Path:", bfs_solution)

def dfs(initial_state, goal_state):
    # Helper functions
    def is_goal(state):
        return state == goal_state
    
    def get_neighbors(state):
        # Get neighbors by moving the blank space (0)
        neighbors = []
        row, col = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in state]
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                neighbors.append(new_state)
        return neighbors

    # DFS Implementation
    stack = [(initial_state, [])]  # Stack holds the state and the sequence of moves taken to reach that state
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))  # Make state hashable for the visited set

    while stack:
        state, path = stack.pop()
        
        if is_goal(state):
            return path  # Return the sequence of moves
        
        for neighbor in get_neighbors(state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                stack.append((neighbor, path + [neighbor]))  # Append the neighbor and the path taken so far
    
    return "Goal state is not reachable"

# Test DFS
dfs_solution = dfs(initial_state, goal_state)
print("DFS Solution Path:", dfs_solution)

