#!/usr/bin/python


import sys


def parse(model, lines, curline, cur_index_level):
  idx = curline
  while idx < len(lines):
    line = lines[idx]
    idx += 1
    space_count = len(line)
    line = line.lstrip()
    space_count = space_count - len(line)
    index_level = space_count / 4
    if index_level == cur_index_level:
      model.append(line)
    elif index_level == cur_index_level + 1:
      submodel = [line]
      model.append(submodel)
      idx = parse(submodel, lines, idx, index_level)
    elif index_level == cur_index_level - 1:
      return idx
    else:
      print ("Parse index error at line:" + str(idx + 1))
      sys.exit(0)


def get_class(lv):
  if (lv == 0):
    return "lindent00"
  if (lv == 1):
    return "lindent0a"
  if (lv == 2):
    return "lindent0b"
  if (lv == 3):
    return "lindent0c"
  return "lindent00"


def get_indent(lv):
  return (" " * (lv * 4))


def print_opentag(lv):
  if lv > 0:
    print get_indent(lv) + """<div class="%s">""" % get_class(lv)


def print_closetag(lv):
  if lv > 0:
    print get_indent(lv) + """</div>"""


def encode(model, curidx_lv):
  idx = 0
  maxidx = len(model)
  while idx < maxidx:
    line = model[idx]
    idx += 1
    if type(line) is list:
      encode(line, curidx_lv + 1)
    else:
      if idx > 1:
        print_closetag(curidx_lv)
      print_opentag(curidx_lv)
      print get_indent(curidx_lv + 1) + """<div>"""
      print get_indent(curidx_lv + 2) + str(line)
      print get_indent(curidx_lv + 1) + """</div>"""
  print_closetag(curidx_lv)

if len(sys.argv) > 1:
  input = sys.argv[1]
  finput = open(input, "r")
  foutput = open(input + ".html", "w")
  buffer = finput.read()
  buffer = buffer.replace("\r\n", "\n")
  lines = buffer.split("\n")
  docroot = []
  parse(docroot, lines, 0, 0)
  encode(docroot, 0)

