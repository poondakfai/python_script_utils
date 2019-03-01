#!/usr/bin/python


import sys


def parse(model, lines):
  for line in lines:
    line = line.strip()[0:-1]
    tokens = line.split(" ")
    if (len(tokens) == 3) and tokens[0] == "private":
        model.append(tokens[1:])


def capitalizeFirst(s):
  return s[0].upper() + s[1:]


def encode(model):
  TAB = "  "
  # Generate getter
  for item in model:
    print ("")
    print (TAB + "public " + item[0] + " get" + capitalizeFirst(item[1]) + "() {")
    print (TAB + TAB + "return this." + item[1] + ";")
    print (TAB + "}")
  # Generate setter
  for item in model:
    print ("")
    print (TAB + "public void set" + capitalizeFirst(item[1]) + "(" + item[0] + " " + item[1] + ") {")
    print (TAB + TAB + "this." + item[1] + " = " + item[1] + ";")
    print (TAB + "}")


buffer = sys.stdin.read()
buffer = buffer.replace("\r\n", "\n")
lines = buffer.split("\n")
docroot = []
parse(docroot, lines)
print ("")
print ("#############")
print ("#############")
print ("#############")
encode(docroot)

