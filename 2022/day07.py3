#!/usr/bin/python3
# part 1 completed 2023-02-01 03:23 ET
# part 2 completed 2023-02-02 23:26 ET

import sys


class Directory:
  def __init__(self, name, children={}, parent=None):
    self.name = name
    self.children = children
    self.parent = parent
    self.size = 0

  # default sort by size
  def __lt__(self, other):
    return self.size < other.size


class File:
  def __init__(self, name, size, parent_dir=None):
    self.name = name
    self.size = size


class FileSystemAnalyzer:
  def __init__(self, debug=False):
    self.root_dir = Directory('/')
    self.curr_dir = self.root_dir
    self._DEBUG = debug
    # to prevent clashes between files and directories with the same name
    self.DIR_PREFIX = 'DIR_'
    # to store results for part 1, directories with size <= 100k
    self.dirs_100k = []
    self.all_dirs = []

  def change_dir(self, dest_dir):
    if dest_dir == '..':
      self.debug_print(f'  - changing current dir ("{self.curr_dir.name}")'
                       f' to parent dir ("{self.curr_dir.parent.name}")')
      self.curr_dir = self.curr_dir.parent
    else:
      dest_dir = self.DIR_PREFIX + dest_dir
      self.curr_dir = self.curr_dir.children[dest_dir]

  def create_dir(self, dir_name):
    new_dir = Directory(dir_name, parent=self.curr_dir)
    dir_name = self.DIR_PREFIX + dir_name
    self.curr_dir.children[dir_name] = new_dir
    self.all_dirs.append(new_dir)

  def create_file(self, file_name, file_size):
    new_file = File(file_name, file_size, self.curr_dir)
    self.curr_dir.children[file_name] = new_file
    self.update_dir_sizes(new_file)

  def update_dir_sizes(self, file):
    dir_pointer = self.curr_dir
    HUNDRED_K = 100000

    while True:
      dir_pointer.size += file.size

      # for part 1 - update list of directories up to 100,000 in size as needed
      if (dir_pointer is not self.root_dir and dir_pointer.size <= HUNDRED_K
          and dir_pointer not in self.dirs_100k):
        self.dirs_100k.append(dir_pointer)
      elif dir_pointer in self.dirs_100k and dir_pointer.size > HUNDRED_K:
        self.dirs_100k.remove(dir_pointer)

      self.debug_print(f'  - new size of dir "{dir_pointer.name}": {dir_pointer.size}')
      if dir_pointer.parent != None:
        dir_pointer = dir_pointer.parent
      else:
        break

  def debug_print(self, message, input_line=None):
    if(self._DEBUG):
      # pretty-print command inputs/outputs so they all line up nicely in debug output;
      # left-justify by 20 chars, since longest input line is 19 chars
      if input_line:
        message = f'{input_line.ljust(20)} | {message}'
      print(message)

  def print_title(self, message):
    fancy_line = '=' * (len(message) + 1)
    print(fancy_line, message, fancy_line, sep='\n')

  def print_part1(self):
    message = 'Part 1 results - directories up to 100K in size'
    self.print_title(message)

    # sort and print largest to smallest
    self.dirs_100k.sort(reverse=True)
    sum_100k = 0
    for curr_dir in self.dirs_100k:
      sum_100k += curr_dir.size
      print(f'| "{curr_dir.name}" - size {curr_dir.size}, parent "{curr_dir.parent.name}"')

    print(f'Sum: {sum_100k}')

  def print_part2(self):
    total_disk_space = 70000000
    free_space = total_disk_space - self.root_dir.size
    space_needed = 30000000
    space_to_clear = space_needed - free_space
    dir_to_delete = None

    message = 'Part 2 results - directory to delete to make 30M free space'
    self.print_title(message)

    # look through all dirs from smallest up to the size we need to clear
    self.all_dirs.sort()
    for curr_dir in self.all_dirs:
      if curr_dir.size >= space_to_clear:
        dir_to_delete = curr_dir
        break

    print( '| Total disk space:', total_disk_space)
    print( '| Free space:', free_space)
    print( '| Space needed:', space_needed)
    print( '| Space to clear:', space_to_clear)
    print(f'Directory to delete: "{dir_to_delete.name}" - size {dir_to_delete.size}, '
          f'parent "{dir_to_delete.parent.name}"')


  def scan(self):
    for line in sys.stdin:
      line = line.rstrip('\n')

      match line.split():
        case ['$', 'cd', dest_dir] if dest_dir != '/':
          self.debug_print(f'changing current dir to "{dest_dir}"', line)
          self.change_dir(dest_dir)

        case ['$', 'ls']:
          self.debug_print(f'listing current dir "{self.curr_dir.name}"', line)

        case ['dir', dir_name]:
          self.debug_print(f'found dir "{dir_name}"', line)
          self.create_dir(dir_name)

        case [file_size, file_name] if file_size[0].isnumeric():
          self.debug_print(f'found file "{file_name}", size {file_size}', line)
          self.create_file(file_name, int(file_size))

        case _:
          self.debug_print(f'ignored / no matching pattern', line)

    self.print_part1()
    self.print_part2()


if __name__ == '__main__':
  fs = FileSystemAnalyzer(debug=True)
  fs.scan()
