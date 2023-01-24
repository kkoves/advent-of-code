#!/usr/bin/python3
# part 1 completed 2023-01-21 19:03 ET

import sys, re


class AdventOfCodeDay5:
  def __init__(self):
    self.stack_numbers = []
    self.stack_strings = []
    self.stacks = {}


  def simplify_column(self, match_obj):
    crate_col = match_obj.group(1)

    # three spaces - empty column
    if crate_col == '   ':
      return '_'
    # '[A]' -> 'A'
    elif crate_col[0] == '[':
      return crate_col[1]
    else:
      return crate_col


  def list_transpose(self):
    # last element of stack_numbers is the total number of crate stacks
    num_stacks = self.stack_numbers[-1]
    self.stack_strings.reverse()
    # print(self.stack_strings)

    curr_stack = 0
    for i in range(num_stacks):
      curr_stack = self.stack_numbers[i]
      self.stacks[curr_stack] = [s[i] for s in self.stack_strings if s[i] != '_']
      # print(f'{i = }, {curr_stack = }, {self.stacks[curr_stack] = }')


  def move_crates(self, how_many, source, dest):
    for _ in range(how_many):
      source_stack_val = self.stacks[source].pop()
      self.stacks[dest].append(source_stack_val)


  def top_of_stacks(self):
    top_string = ''
    for i in self.stack_numbers:
      top_string += self.stacks[i][-1]

    return top_string


  def main(self):
    stack_regex = r'(\[\w\]|\s{3})\s?'
    # move_template = {'count': 0, 'move_from': 0, 'move_to': 0}

    # array indexes for processed move input lines
    HOW_MANY = 0
    FROM_STACK = 1
    TO_STACK = 2

    for line in sys.stdin:
      line = line.rstrip('\n')
      # print(f'\nLINE = "{line}"')

      # crates - '   [A] [B]   ' etc. lines of input
      if '[' in line:
        self.stack_strings += [re.sub(stack_regex, self.simplify_column, line)]
        # print(f'{self.stack_strings = }')

      # stack numbers - ' 1 2 3 4 5 [...]' line of input; always has a space as line[0], so check line[1]
      elif len(line) > 1 and line[1].isnumeric():
        self.stack_numbers = [int(s) for s in line.split()]
        # print(f'{self.stack_numbers = }, proceeding to list_transpose()\n')
        # since stack numbers are after stack lines, we can finalize our data structure representation
        self.list_transpose()
        # print(self.stacks)

      # get every other element, which works out to just the numbers from "move 1 from 2 to 3"
      elif line.startswith('move'):
        curr_move = [int(num_str) for num_str in line.split()[1::2]] # returns [1, 2, 3] or the like
        self.move_crates(curr_move[HOW_MANY], curr_move[FROM_STACK], curr_move[TO_STACK])

    print(f'-----\nPart 1 answer: {self.top_of_stacks()}')


if __name__ == '__main__':
  day5 = AdventOfCodeDay5()
  day5.main()
