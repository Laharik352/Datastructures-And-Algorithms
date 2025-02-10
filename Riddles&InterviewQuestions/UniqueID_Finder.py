'''Given a list of account ID numbers (integers) which contains duplicates , find the one unique integer.
(the list is guaranteed to only have one unique (non-duplicated) integer'''

def solution(id_list):

    # Initiate unique Id
    unique_id = 0

    # XOR fo revery id in id list
    for i in id_list:

        # XOR operation
        unique_id ^= i
        # print(unique_id)
    return unique_id

print(solution([1,2,3,2,1])) 


