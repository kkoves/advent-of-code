#!/usr/bin/python3
# completed 2023-01-12 23:48 ET

import sys, copy

def main():
  elf_template = {'calories': [], 'total': 0}
  elves = []
  calorie_totals = []
  elf_num = -1

  for line in sys.stdin:
    # start a new "elf record" if we're on the first line of input or a blank line (end of current elf)
    if elf_num == -1 or line in ['\n', '\r\n']:
      # add current elf's calorie total to list once we're at the end of its input lines
      if elf_num >= 0:
        calorie_totals.append(elves[elf_num]['total'])
      elf_num += 1
      elves.append(copy.deepcopy(elf_template))
    else:
      calorie_count = int(line)
      elves[elf_num]['calories'].append(calorie_count)
      elves[elf_num]['total'] += calorie_count

  print(elves)
  print("Part 1:", max(calorie_totals))

  top_three_elf_calories = sorted(calorie_totals, reverse = True)[:3]
  print("Part 2: top three -", top_three_elf_calories, "; sum -", sum(top_three_elf_calories))


if __name__ == '__main__':
  main()