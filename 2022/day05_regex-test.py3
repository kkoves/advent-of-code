#!/usr/bin/python3

import sys, re

def simplify(match_obj):
  crate_col = match_obj.group(1)

  if crate_col == '   ':
    return '_'
  elif crate_col[0] == '[':
    return crate_col[1]
  else:
    return crate_col


def main():
  # test_str = '    [D]    '
  reg = r'(\[\w\]|\s{3})\s?'

  # res = re.sub(reg, simplify, test_str)
  # print(f'\"{res}\"')
  for line in sys.stdin:
    res = re.sub(reg, simplify, line)
    print(f'\"{res}\"')


if __name__ == '__main__':
  main()
