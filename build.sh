#!/bin/bash

echo "Compiling the program"
g++ main.cpp -o out

echo "Running ..."
./out > result.csv

echo "Plotting ..."
python plot_result.py result.csv
