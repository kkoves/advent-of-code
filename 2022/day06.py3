#!/usr/bin/python3
# part 1 completed 2023-01-29 15:35 ET
# part 2 completed 2023-01-29 __:__ ET

import sys

def find_packet_marker(datastream):
  # max position where we can check for a four-char string is len(datastream) - 4,
  # since we're checking datastream[i] and the next three chars, but this becomes
  # len(datastream) - 3 since range excludes the top value
  max_pos = len(datastream) - 3

  for i in range(max_pos):
    char_set = set(datastream[i:i+4])
    # break when set length == 4, which means the four chars are all different
    if len(char_set) == 4:
      break

  # return how many chars were processed by end of start-of-packet marker
  return i + 4


def main():
  # only one (long) line of input in the full input file,
  # but still loop so we can test multiple inputs in one file
  for line in sys.stdin:
    line = line.rstrip('\n')
    chars_processed = find_packet_marker(line)
    # don't print ridiculously long input lines like the 4095-char full input file
    if len(line) < 40:
      print(f'Full datastream: "{line}" (length: {len(line)} chars)')
    else:
      print(f'Datastream length: {len(line)}')

    # print some stats before answer, just for fun
    marker_start, marker_end = chars_processed - 4, chars_processed
    print(f'Datastream up to end of start-of-packet marker: "{line[:marker_end]}" (length: {chars_processed} chars)')
    print(f'Start-of-packet marker: "{line[marker_start:marker_end]}"')
    percent_processed = round( (marker_end / len(line)) * 100, 2)
    print(f'{percent_processed}% of string processed up to and including start-of-packet marker')

    print(f'\nPart 1 answer: start-of-packet marker complete after char {chars_processed} of datastream\n-----\n')


if __name__ == '__main__':
  main()
