#!/usr/bin/python3
# completed 2023-01-__ __:__ ET

import sys


class Directory:
  def __init__(self, name, children={}, parent=None):
    self.name = name
    self.children = children
    self.parent = parent
    self.size = 0

class File:
  def __init__(self, name, size, parent_dir=None):
    self.name = name
    self.size = size


def main():
  root_dir = Directory('/')
  curr_dir = root_dir

  for line in sys.stdin:
    line = line.rstrip('\n')
    ljust_line = line.ljust(20) # longest input line is 19 chars

    match line.split():
      case ['$', 'cd', dest_dir] if dest_dir != '/':
        print(f' {ljust_line} | changing current dir to "{dest_dir}"')
        if dest_dir == '..':
          print(f'  - changing current dir ("{curr_dir.name}") to parent dir ("{curr_dir.parent.name}")')
          curr_dir = curr_dir.parent
        else:
          curr_dir = curr_dir.children[dest_dir]

      case ['$', 'ls']: # maybe don't need this case, nothing to be done in our code when `ls` is run
        print(f' {ljust_line} | listing current dir "{curr_dir.name}"')

      case ['dir', dir_name]:
        print(f' {ljust_line} | found dir "{dir_name}"')
        new_dir = Directory(dir_name, parent=curr_dir)
        curr_dir.children[dir_name] = new_dir

      case [file_size, file_name] if file_size[0].isnumeric():
        file_size = int(file_size)
        print(f' {ljust_line} | found file "{file_name}", size {file_size}')
        curr_dir.children[file_name] = File(file_name, file_size, curr_dir)
        dir_pointer = curr_dir
        while True:
          dir_pointer.size += file_size
          print(f'  - new size of dir "{dir_pointer.name}": {dir_pointer.size}')
          if dir_pointer.parent != None:
            dir_pointer = dir_pointer.parent
          else:
            break

      case _:
        print(f' {ljust_line} | ignored / no matching pattern')


if __name__ == '__main__':
  main()
