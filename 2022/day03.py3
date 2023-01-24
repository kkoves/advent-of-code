#!/usr/bin/python3
# part 1 completed 2023-01-15 21:35 ET
# part 2 completed 2023-01-15 22:16 ET

import sys

priority_conversion = {
    'a':  1, 'b':  2, 'c':  3, 'd':  4, 'e':  5, 'f':  6, 'g':  7, 'h':  8, 'i':  9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
    'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46,
    'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
  }

# for part 1
def get_rucksack_priority(rucksack):
  halfway = len(rucksack) // 2
  compartment1, compartment2 = set(rucksack[:halfway]), set(rucksack[halfway:])
  in_both_compartments = compartment1.intersection(compartment2)
  return sum([priority_conversion[item_type] for item_type in in_both_compartments])


# for part 2
def get_badge_priority(rucksacks):
  # list of strings -> list of sets -> expand -> intersection
  badge_item_type = set.intersection(*[set(rucksack) for rucksack in rucksacks])
  # print(f'{badge_item_type = }')
  # one-item set -> one-item list -> extract item -> get result from priority dict
  return priority_conversion[list(badge_item_type)[0]]


def main():
  priorities_total = 0 # part 1
  # part 2
  rucksack_counter = 1
  elf_group_rucksacks = []
  badge_priorities_total = 0

  for rucksack in sys.stdin:
    rucksack = rucksack.rstrip() # found \n getting into item sets for part 2, removing them
    priorities_total += get_rucksack_priority(rucksack)
    # part 2 stuff below
    elf_group_rucksacks.append(rucksack)
    if rucksack_counter % 3 == 0:
      badge_priorities_total += get_badge_priority(elf_group_rucksacks)
      elf_group_rucksacks = []
    rucksack_counter += 1

  print('Part 1, sum of priorities of rucksacks:', priorities_total)
  print('Part 2, sum of priorities of badges:', badge_priorities_total)


if __name__ == '__main__':
  main()
