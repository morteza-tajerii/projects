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
