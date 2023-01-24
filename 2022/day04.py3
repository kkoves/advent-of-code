#!/usr/bin/python3
# part 1 completed 2023-01-16 01:07 ET
# part 2 completed 2023-01-16 01:26 ET

import sys

def main():
  overlap_count_part1 = 0
  overlap_count_part2 = 0

  for line in sys.stdin:
    # makes a list like [['2', '6'], ['4', '8']]
    ranges = [s.split('-') for s in line.split(',')]
    # flatten 2D list to 1D, convert str items to int
    ranges = [int(i) for sublist in ranges for i in sublist]

    [start1, end1, start2, end2] = ranges
    range1 = set(range(start1, end1 + 1))
    range2 = set(range(start2, end2 + 1))

    # if range1.issubset(range2) or range2.issubset(range1):
    #   overlap_count_part1 += 1

    if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):
      overlap_count_part1 += 1
    if range1.intersection(range2):
      overlap_count_part2 += 1
    # if (start1 >= start2 or end1 <= end2) or (start2 >= start1 or end2 <= end1):
    #   overlap_count_part2 += 1

  print('Part 1:', overlap_count_part1)
  print('Part 1:', overlap_count_part2)


if __name__ == '__main__':
  main()
