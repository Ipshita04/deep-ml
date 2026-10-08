def find_duplicates(records):
    # records: list of hashable items (ints or strings)
    # return a list of values that appear more than once,
    # each listed once, ordered by the position of its second occurrence
    seen=set()
    duplicates=[]
    for i in records:
        if(i in seen):
            if(i not in duplicates):
                duplicates.append(i)
        else:
            seen.add(i) 
    return duplicates       
    pass