#!/usr/bin/env python3

"""
JustPrintIt is a tool for automatically adding and removing print statements for
debugging purposes. It was quickly hacked together and intented for small programs.
"""

import sys

def ends_in_semicolon(line):
    """
    Returns True if last non-white space character
    is a semicolon
    """
    ends_in_semi = False
    for c in line:
        if c == ';':
           ends_in_semi = True
        elif c not in ["\t", " ", '\n']:
            ends_in_semi = False
    return ends_in_semi

def add_lines(file_name):
    """
    Get Lines that need a print statement added before them
    and adds the lines to the file specified in file_name
    """
    f = open(file_name, "r")
    contents = f.readlines()
    f.close()

    lines_to_add = [i for i, v in enumerate(contents) if ends_in_semicolon(v)]
    insert_idxs = [i + v for i, v in enumerate(lines_to_add)]
    for i, v in enumerate(insert_idxs):
        contents.insert(v, f"std::cout << \"Debug line {i} ........ justPrintIt\" << std::endl;\n")
    contents = "".join(contents)

    f = open(file_name, "w")
    f.write(contents)
    f.close()

def remove_lines(file_name):
    """
    remove lines added from a justPrintIt debug session
    """
    f = open(file_name, "r")
    contents = f.readlines()
    f.close()

    filtered_contents = list(filter(lambda line : "justPrintIt" not in line, contents))
    contents = "".join(filtered_contents)

    f = open(file_name, "w")
    f.write(contents)
    f.close()


""" 
Script invocation logic
"""

usage = "Usage : \n\tjustPrintIt -a fileName.cpp | \n\tJustPrintIt -r fileName.cpp"

arg_len = len(sys.argv)
if arg_len < 3:
    print(usage)
elif "-a" == sys.argv[1]:
    add_lines(sys.argv[2])
elif "-r" == sys.argv[1]:
    remove_lines(sys.argv[2])
else:
    print(usage)
