#!/bin/bash

chmod +x basics_test.sh

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
source ssshtest

pycodestyle style.py

pycodestyle get_column_stats.py

(for i in 'seq 1 100'
    do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM"
    done) > data.txt

python get_column_stats.py data.txt 2


V = 1
(for i in 'seq 1 100'
    do
    echo - e "$V\t$V\t$V\t$V\t$V"
    done) > data.txt

python get_column_stats.py data.txt 2

# added a test to ensure that if no values are provided:
# exit code 1
# no output
run mean_test python3 get_column_stats.py mean()
assert_exit_code 1
assert_no_stdout

# added a test to ensure that if the values 2 and 4 are provided:
# their mean is 3 and output is displayed
run mean_test python3 get_column_stats.py mean(2 4)
assert_stdout
assert_in_stdout 3

# added a test to ensure that if no values are provided:
# exit code 1
#no output
run stdev_test python3 get_column_stats.py stdev()
assert_exit_code 1
assert_no_stdout
