def calculatein(main_list, dictionary, imm, non_imm):

    time_loss = 0

    for f, l in imm:
        fir = main_list.index(f)
        sec = main_list.index(l)
        order = [fir, sec]
        order.sort()
        sub_list = main_list[order[0]+1: order[1]+1]

        for i in range(0, len(sub_list)):
            sub_list[i] = dictionary[sub_list[i]]

        time_loss += sum(sub_list)

    for f, l in non_imm:
        fir = main_list.index(f)
        sec = main_list.index(l)

        order = [fir, sec]
        order.sort()

        sub_list = main_list[order[0]+1: order[1]+1]

        for i in range(0, len(sub_list)):
            sub_list[i] = dictionary[sub_list[i]]

        time_loss += 15-sum(sub_list)

    return time_loss


condition = input('enter condition(works, prerequired, imm, non_imm): ')
condition = condition.strip().split()

print(condition)

n_work = int(condition[0])
n_prereq = int(condition[1])
n_imm = int(condition[2])
n_non_imm = int(condition[3])

work_time = input('enter works required times: ')
work_time = work_time.strip().split()

print(work_time)

string = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
string += ['13', '14', '15']
count = 0
work_dict = dict()

for time in work_time:
    work_dict[string[count]] = int(time)
    count += 1

print(work_dict)

prereq = []

for x in range(0, int(n_prereq)):

    pr = input('enter prerequirments: ')
    pr = pr.strip().split()
    prereq.append((pr[0], pr[1]))

print(prereq)

imm = []

for x in range(0, int(n_imm)):
    imd = input('enter immediate works: ')
    imd = imd.strip().split()
    imm.append((imd[0], imd[1]))

print(imm)

non_imm = []

for x in range(0, int(n_non_imm)):
    nimd = input('enter non-immediate: ')
    nimd = nimd.strip().split()
    non_imm.append((nimd[0], nimd[1]))

print(non_imm)


def sort_prereq(main_list, prereq):
    pass


def sort_imm(main_list, imm):
    pass


def sort_non_imm(main_list, non_imm):
    pass


# یک راه پیدا کردم که شاید جواب بده.
# این که لیست های مطابق پیش نیاز ها رو جدا کنم و یکی که
# کمترین ضرر رو به بار میاره رو جدا کنم
