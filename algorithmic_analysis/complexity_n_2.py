import sys

assert len(sys.argv) > 1, "ARGV missing"
n = int(sys.argv[1])

count = 0
for i in range(n):
    for j in range(n):
        count += 1
        sys.stdout.write(f'\r Count: {count} ')

sys.stdout.write('\n')
