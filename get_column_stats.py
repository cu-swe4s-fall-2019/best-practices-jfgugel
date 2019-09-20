import sys
import math
import argparse



def mean(V):
    '''
    Compute the mean of the values in the column. Expects at least one value.

    Parameters
    -----------
    V: List of intergers in the column

    Returns
    --------
    mean: The mean of all the values in the column
    '''
    
    if len(V) == 0:
        return None
        # return an exit code of 1 for an empty column
        sys.exit(1)
             
    else: 
        mean = sum(V)/len(V)
        return mean
    

def stdev(V):
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
    
    if len(V) == 0:
        return None
        # return an exit code of 1 for an empty column
        sys.exit(1)
        
    else:
        stdev = math.sqrt(sum([(mean(V)-x)**2 for x in V]) / len(V))
        return stdev



if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file',
                        required=True)

    parser.add_argument('--column_number',
                        type=int,
                        help='The name of the column',
                        required=True)

    args = parser.parse_args()

    try: 
        file = open(args.file_name, 'r')
    except FileNotFoundError:
        print('Could not find' + args.file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open' + args.file_name)
        sys.exit(1)

    V = []

    for col in file:
        try: 
            A = [int(x) for x in col.split()]
        except ValueError:
            print('Check column values')
            sys.exit(1)
        try: V.append(int(A[args.column_number]))
        except IndexError:
            print('Problem with column number')
            sys.exit (1)



    print('mean:', mean(V))
    print('stdev:', stdev(V))