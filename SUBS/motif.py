def substring_positions(s, t):
    pos_list = []
    pos = s.find(t)
    while (pos != -1):
        # It appends 'pos + 1' because Python strings indices starts at 0 and
        # the task asks us the positions of the substring starting from 1.
        pos_list.append(pos + 1)
        # pos + 1 because we want to find the next position of the substring
        # starting from the 'last one + 1'
        pos = s.find(t, pos + 1)
    return pos_list


subs_file = open('rosalind_subs.txt', 'r')
try:
    # [:-1] so it removes the \n from the end of the line
    s = subs_file.readline()[:-1]
    t = subs_file.readline()[:-1]
    pos_list = substring_positions(s, t)
finally:
    subs_file.close()

[print(p, end=' ') for p in pos_list]
