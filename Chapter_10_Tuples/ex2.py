"""Exercise 2.

This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
python timeofday.py

Enter a file name: mbox-short.txt

04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

try:
    filename = input("Enter a file name: ")
    file_handler = open(filename, encoding="utf-8")  # pylint: disable=R1732
except FileNotFoundError:
    print("Invalid file name")
    exit()  # pylint: disable=R1722

hour_histogram = {}
for line in file_handler:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
        time = words[5]
        time_list = time.split(":")
        hour = time_list[0]
        if hour not in hour_histogram:
            hour_histogram[hour] = 1
        else:
            hour_histogram[hour] += 1

# print(f"\nDebug: {hour_histogram}\n")

hour_list = []
for key, val in list(hour_histogram.items()):
    hour_list.append((key, val))

# print(f"\nDebug: {hour_list}\n")
hour_list.sort()
# print(f"\nDebug: {hour_list}\n")

for key, val in hour_list:
    print(key, val)
