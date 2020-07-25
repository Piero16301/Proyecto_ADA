def vectorConverter(vec):
    count = 0
    values = []
    for i in vec:
        if i == 1:
            count += 1
        else:
            if count != 0:
                values.append(count)
                count = 0
    if count != 0:
        values.append(count)
    return values
