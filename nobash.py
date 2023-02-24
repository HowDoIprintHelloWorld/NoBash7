#!/usr/bin/env python3

from src.scriptPrep.fileToStringPy import readFileToString
from src.scriptPrep.stringToLines import stringToLines

from sys import argv
import ctypes



if __name__ == "__main__":
    lib = ctypes.cdll.LoadLibrary("src/scriptPrep/fileToString.so")
    lib.printHi()

    fileString = readFileToString(argv[1])
    lineList = stringToLines(fileString)
    print(lineList)