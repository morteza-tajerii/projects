import string


def calculatein(listed, dictionary, imm, non_imm):

    time_loss = 0

    for f, s in imm:
        fir = listed.index(f)
        sec = listed.index(s)
        order = [fir, sec]
        order.sort()
        sub_list = listed[order[0]+1: order[1]+1]

        for i in range(0, len(sub_list)):
            sub_list[i] = dictionary[sub_list[i]]

        time_loss += sum(sub_list)

    for f, s in non_imm:
        fir = listed.index(f)
        sec = listed.index(s)

        order = [fir, sec]
        order.sort()

        sub_list = listed[order[0]+1: order[1]+1]

        for i in range(0, len(sub_list)):
            sub_list[i] = dictionary[sub_list[i]]

        time_loss += 15-sum(sub_list)

    return time_loss


condition = input('enter condition: ')
condition = condition.strip().split()

if len(condition) != 4:
    exit()

c_number = condition[0]
c_prereq = condition[1]
c_immediate = condition[2]
c_non_immediate = condition[3]

times_list = input('enter times: ')
times_list = times_list.strip().split()

if len(times_list) != int(c_number):
    exit()

times_dict = dict()

alphabet = string.ascii_lowercase
counter = 0

for item in times_list:
    times_dict[alphabet[counter]] = int(item)
    counter += 1


prereq_list = []

for st in range(0, int(c_prereq)):
    p = input('enter prerequired: ')
    p = p.strip().split()
    prereq_list.append((p[0], p[1]))

prereq = prereq_list


immediate_list = []

for st in range(0, int(c_immediate)):
    i = input('enter immediate: ')
    i = i.strip().split()
    immediate_list.append((i[0], i[1]))

immediate = immediate_list


non_immediate_list = []

for st in range(0, int(c_non_immediate)):
    n = input('enter non-immediate: ')
    n = n.strip().split()
    non_immediate_list.append((n[0], n[1]))

non_immediate = non_immediate_list

# first = immediate , second = non-immediate , third = prerequired

result = list(times_dict.keys())

# 5, 2, 2, 1, 3
# a, b, c, d, e

# imm a, e
# imm b, d

# less in end


def check()

for a, b in immediate:

    items = {a: times_dict[a], b: times_dict[b]}
    priority = list(sorted(items.items(), key=lambda one: one[1]))

    small_in = result.index(priority[0])
    big_in = result.index(priority[1])

    if small_in > big_in:
        result.insert(small_in + 1, result.pop(big_in))
    elif big_in >= small_in:
        result.insert(small_in - 1, result.pop(big_in))


#    if priority[0] > priority[1] and index_0 < index_1:
#        pass
#
#    elif priority[0] > priority[1] and index_0 > index_1:
#        result_list[index_0],result_list[index_1] = result_list[index_1],
# result_list[index_0]

#    elif priority[0] <= priority[1] and index_0 > index_1:

#        result_list[index_0],result_list[index_1] = result_list[index_1],
# result_list[index_0]
#    elif priority[0] <= priority[1] and index_0 < index_1:
#        pass
# for element in non_immediate:
#    priority = [ int(element[0]) , int(element[1]) ]
#    index_0 = result_list.index(priority[0])
#    index_1 = result_list.index(priority[1])
#
#    if priority[0] > priority[1] and index_0 < index_1:
# result_list[index_0]
#    elif priority[0] > priority[1] and index_0 > index_1:
#        pass
#    elif priority[0] <= priority[1] and index_0 > index_1:
#        pass
#    elif priority[0] <= priority[1] and index_0 < index_1:
#
#        result_list[index_0],result_list[index_1] = result_list[index_1],
# result_list[index_0]
# for element in prereq:
#    priority = [ int(element[0]) , int(element[1]) ]
#    index_0 = result_list.index(priority[0])
#    index_1 = result_list.index(priority[1])

#    if index_0 < index_1:
#        pass
#    if index_0 < index_1 :
#        result_list[index_0],result_list[index_1] = result_list[index_1],
# result_list[index_0]
