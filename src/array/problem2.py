# control array

def soultion(lst):
    unique_lst = list(set(lst)) # delete same value
    unique_lst.sort(reverse=True) # down sorting
    return unique_lst

