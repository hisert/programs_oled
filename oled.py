#!/bin/bash

cd
pkill test
rm -r test_cpp
git clone https://github.com/hisert/test_cpp.git
cd test_cpp/test
g++ -o test main.cpp -lwiringPi
/root/test_cpp/test/test
