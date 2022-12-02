#!/bin/bash

# put this shell in every cov-result directory

for file in ./*
do
  cd ./$file
  lcov --capture --directory . -o coverage.info
  genhtml coverage.info -o page
  cd ..
done
