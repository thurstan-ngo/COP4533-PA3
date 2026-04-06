import sys

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
        first_str = file.readline()
        second_str = file.readline()
    

if __name__ == '__main__':
    main()