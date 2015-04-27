import sys
import re


def main():
    try:
        filename = sys.argv[1]
        shift = float(sys.argv[2])
    except (IndexError, ValueError):
        print("usage: srt-shift filename shift")
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

                    return (
                        hour * 60 * 60 * 1000 +
                        minute * 60 * 1000 +
                        second * 1000 +
                        microsecond
                    )

                start, end = map(parse_time, (start, end))

                def shift_time(time):
                    return time + shift * 1000

                start, end = map(shift_time, (start, end))

                def get_time(time):
                    return (
                        time // (60 * 60 * 1000),
                        (time % (60 * 60 * 1000)) // (60 * 1000),
                        (time % (60 * 1000)) // 1000,
                        time % 1000,
                    )

                def str_time(time):
                    return '%02d:%02d:%02d,%03d' % get_time(time)

                out += '%s --> %s\n' % (
                    str_time(start),
                    str_time(end),
                )

            elif i >= 3:
                out += '%s\n' % line

    print(out)

if __name__ == '__main__':
    main()

# vim: expandtab tabstop=4 shiftwidth=4
