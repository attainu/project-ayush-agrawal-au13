import linecache
import argparse
from maze_logic import *


if __name__ == '__main__':

    maze_obj= maze_logic()

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', default='inputfile.txt',
                        help='Enter Input File?')
    parser.add_argument('-o', default='outputfile.txt',
                        help='output will be provided in this file....')

    input_file = open("inputfile.txt", "r")
    output_file = open("outputfile.txt", "w")
    N = linecache.getline("inputfile.txt", 1)  # to get 1 st line of input file
    N = int(N)

    input_file = open("inputfile.txt", "r")

    input_file = open("inputfile.txt", "r")
    input_matrix = []

    for i in range(N+1):
        line = input_file.readline()
        if i > 0:
            input_matrix.append(list(map(int, line.rstrip().split())))
    input_file.close()

    temp_list =maze_obj.solveMaze(input_matrix, N)

    if type(temp_list) is list:
        for i in temp_list:
            for j in i:
                output_file.write(str(j))
                output_file.write(" ")

            output_file.write("\n")
        output_file.close()

    else:
        output_file.write(str(temp_list))
        output_file.close()


