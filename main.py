import sys
import time

def hvlcs(A, B, value_dict):
    m, n = len(A), len(B)
    if m == 0 or n == 0:
        return 0
    
    # Build table
    arr = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                arr[i][j] = arr[i-1][j-1] + value_dict[A[i-1]]
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    # Backtracking
    i, j = m, n
    subsequence = []
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            subsequence.append(A[i-1])
            i -= 1
            j -= 1
        elif arr[i-1][j] >= arr[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    subsequence.reverse()
    return arr[m][n], "".join(subsequence)
    

def main():
    input_file = sys.argv[1]

    # Read input file
    with open(input_file, 'r') as file:
        # First line contains k = number of characters in the alphabet
        k = int(file.readline())
        
        # Each of the next k lines contains a character and its value
        value_dict = {}
        for i in range(k):
            char, value = file.readline().split()
            value = int(value)
            value_dict[char] = value
        
        # Read the two strings
        first_str = file.readline().strip()
        second_str = file.readline().strip()

    # Start measuring runtime
    start = time.perf_counter()
    # Run the dynamic programming algorithm and output results
    max_value, subsequence = hvlcs(first_str, second_str, value_dict)
    # End Runtime
    end = time.perf_counter()

    print(max_value)
    print(subsequence)
    print(f"Runtime: {(end - start) * 1000:.3f} ms")
    

if __name__ == '__main__':
    main()