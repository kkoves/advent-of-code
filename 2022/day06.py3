#!/usr/bin/python3
# part 1 completed 2023-01-29 15:35 ET
# part 2 completed 2023-01-30 00:04 ET

import sys

# Returns how many chars were processed up to and including end of start-of-packet marker
# (4 unique chars) and end of start-of-message marker (14 unique chars)
def find_markers(datastream):
  # max position where we can check for a 14-char string (message start marker) is `len(datastream) - 13`,
  # since we're checking `datastream[i]` and the next 13 chars (14 chars total), but this becomes
  # `len(datastream) - 13` since range excludes the top value, and [start-of-packet] < [start-of-message]
  max_pos = len(datastream) - 13
  packet_marker_end = 0
  message_marker_end = 0

  # constants; SoP = start-of-packet, SoM = start-of-message, LEN = length
  SOP_LEN = 4
  SOM_LEN = 14

  char_set = set()
  for i in range(max_pos):
    # don't update `char_set` if start-of-packet marker was already found
    if packet_marker_end == 0:
      char_set = set(datastream[i : i+SOP_LEN])
    # start-of-packet when set length == 4, which means the four chars are all different
    # `i + 4` instead of `i + 3` since we return number of chars processed and not index
    if packet_marker_end == 0 and len(char_set) == SOP_LEN:
      packet_marker_end = i + SOP_LEN
    
    # start looking for start-of-message marker once start-of-packet has been found
    if packet_marker_end > 0:
      char_set = set(datastream[i : i+SOM_LEN])
      if len(char_set) == 14:
        message_marker_end = i + SOM_LEN
        break

  return packet_marker_end, message_marker_end


# strings/stats related to puzzle answers, just for fun; had to duplicate
# parts 1 & 2 answers from `main()` to have these stats grouped better
def print_stats(datastream, packet_marker_end, message_marker_end):
  # don't print ridiculously long input lines like the 4095-char full input file
  if len(datastream) < 40:
    print(f'Full datastream: "{datastream}" (length: {len(datastream)} chars)')
  else:
    print(f'Datastream length: {len(datastream)}')

  # part 1 - start-of-packet marker
  packet_marker_start = packet_marker_end - 4
  print(f'Start-of-packet marker complete after char {packet_marker_end} of datastream')
  print(f'Start-of-packet marker: "{datastream[packet_marker_start:packet_marker_end]}"')
  print(f'Datastream up to end of start-of-packet marker: "{datastream[:packet_marker_end]}" (length: {packet_marker_end} chars)')
  percent_processed = round( (packet_marker_end / len(datastream)) * 100, 2)
  print(f'{percent_processed}% of string processed up to and including start-of-packet marker')
  print('\n----------\n')

  # part 2 - start-of-message marker
  message_marker_start = message_marker_end - 14
  print(f'Start-of-message marker complete after char {message_marker_end} of datastream')
  print(f'Start-of-message marker: "{datastream[message_marker_start:message_marker_end]}"')
  print(f'Datastream up to end of start-of-message marker: "{datastream[:message_marker_end]}" (length: {message_marker_end} chars)')
  percent_processed = round( (message_marker_end / len(datastream)) * 100, 2)
  print(f'{percent_processed}% of string processed up to and including start-of-message marker')
  print('\n==========\n')


def main():
  # only one (long) line of input in the full input file,
  # but still loop so we can test multiple inputs in one file
  for line in sys.stdin:
    line = line.rstrip('\n')
    packet_marker_end, message_marker_end = find_markers(line)
    print_stats(line, packet_marker_end, message_marker_end)

    print(f'Part 1 answer: start-of-packet marker complete after char {packet_marker_end} of datastream')
    print(f'Part 2 answer: start-of-message marker complete after char {message_marker_end} of datastream')
    # just a separator to notate end of output section when testing multiple datastream strings
    print('\n********************\n')


if __name__ == '__main__':
  main()
