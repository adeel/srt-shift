import sys
import re

def main():
  try:
    filename = sys.argv[1]
    shift = float(sys.argv[2])
  except IndexError, ValueError:
    print "usage: srt-shift filename shift"
    return
  
  out = ''
  
  with open(filename, 'r') as file:
    i = 0
    for line in file:
      line = line.strip()
      if not line:
        out += '\n'
        continue
      
      i += 1
      
      if re.compile('^(\d+)$').match(line):
        i = 1
      
      if i == 1:
        out += '%s\n' % line
      
      elif i == 2:
        start, end = line.split(' --> ')
        
        def parse_time(time):
          hour, minute, second = time.split(':')
          hour, minute = int(hour), int(minute)
          second_parts = second.split(',')
          second = int(second_parts[0])
          microsecond = int(second_parts[1])
          
          return [hour, minute, second, microsecond]
        
        start, end = map(parse_time, (start, end))
        
        def shift_time(time):
          shift
          time[1] += (time[2] + shift) / 60
          time[2] = (time[2] + shift) % 60
          return time
        
        start, end = map(shift_time, (start, end))
        
        out += '%s:%s:%s,%s --> %s:%s:%s,%s\n' % (
          str(start[0]).rjust(2, '0'),
          str(start[1]).rjust(2, '0'),
          str(start[2]).rjust(2, '0'),
          str(start[3]).rjust(3, '0'),
          
          str(end[0]).rjust(2, '0'),
          str(end[1]).rjust(2, '0'),
          str(end[2]).rjust(2, '0'),
          str(end[3]).rjust(3, '0'))
        
      elif i >= 3:
        out += '%s\n' % line
  
  print out

if __name__ == '__main__':
  main()