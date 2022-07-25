def valid_name(names):
    namesList = []
    for i in (list(names.split(","))):
        if i.isalpha() and len(i) <= 10:
            namesList.append(i)
        else:
            namesList.clear()
            return namesList

    return namesList
