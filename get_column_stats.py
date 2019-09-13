import sys
import math
import argparse


parser = argparse.ArgumentParser

parser.add_argument('--file_name',
                    type=str,
                    help='Name of the file',
                    required=True)

parser.add_argument('--column_number',
                    type=int,
                    help='The name of the column',
                    required=True)

args = parser.parse_args()

f = open(file_name, 'r')


V = []

for l in f:
    A = [int(x) for x in l.split()]
    V.append(A[col_num])


def get_array_mean(V):
    '''
    Compute the mean of the values in the column. Expects at least one value.

    Parameters
    -----------
    V: List of intergers in the column

    Returns
    --------
    mean: The mean of all the values in the column
    '''


mean = sum(V)/len(V)
return mean
if len(V) == 0
# return an exit code of 1 for an empty column
sys.exit(1)


def get_array_mean(V):
    '''
    Compute the standard deviation of the values in the column.
    Expects ate least one value

    Parameters
    ----------
    V: List of integers in the column

    Returns:
    --------
    stdev: The standard deviation of all the values in the column
    '''


stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
return stdev
if len(V) == 0
# return an exit code of 1 for an empty column
sys.exit(1)

print('mean:', mean)
print('stdev:', stdev)
