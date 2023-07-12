import sys

import buildmtree

def input_string_to_list(user_input: str) -> list:
    user_input = user_input[1:-1]
    split_str = user_input.split(",")
    for i in range(0, len(split_str)):
        split_str[i] = split_str[i].strip()
    return split_str


def build_json_tree(data_in):
    json_out = buildmtree.json_tree(buildmtree.tree_build(data_in), data_in)
    return json_out

def sub_tree_verify(tree_old:list, tree_new:list) -> bool:
    # old tree has a shorter length than new tree
    tree_new = tree_new[:len(tree_old)]
    if find_list_root_hash(tree_old) == find_list_root_hash(tree_new):
        print("yes", end=" ")
        return True
    else:
        print("no")
        sys.exit()

def find_list_root_hash(list_input: list) -> str:
    tree_find = (buildmtree.tree_build(list_input))
    root_value = tree_find[-1][0]
    return root_value

def largest_power_of_2(n):
    power = 1
    while power * 2 < n:
        power *= 2
    return power


def sub_proof(m:int, list_d:list, b:bool) -> None:
    n = len(list_d)
    if m == n:
        if b:
            return None
        else:
            proof["plaintext"].append(list_d[0:m])
            proof["hash_value"].append(find_list_root_hash(list_d[0:m]))
    elif m < n:
        k = largest_power_of_2(n)
        if m <= k:
            # SUBPROOF(m, D[n], b) = SUBPROOF(m, D[0:k], b) : MTH(D[k:n])
            proof["plaintext"].append(list_d[k:n])
            proof["hash_value"].append(find_list_root_hash(list_d[k:n]))
            sub_proof(m, list_d[0:k], b)
        else:
            # SUBPROOF(m, D[n], b) = SUBPROOF(m - k, D[k:n], false) : MTH(D[0:k])
            proof["plaintext"].append(list_d[0:k])
            proof["hash_value"].append(find_list_root_hash(list_d[0:k]))
            sub_proof(m - k, list_d[k:n], False)


if __name__ == '__main__':
    tree1 = input_string_to_list(sys.argv[1])
    tree2 = input_string_to_list(sys.argv[2])
    # The hashed line are test code.
    # tree1 = ["alice", "bob", "david", "carlol"]
    # tree2 = ["alice", "bob", "david", "carlol", "eve", "fred"]
    # tree1 = [str(i) for i in range(0,4)]
    # tree2 = [str(i) for i in range(0,7)]
    # print(str(tree1) + "\n" + str(tree2))

    json1 = build_json_tree(tree1)
    json2 = build_json_tree(tree2)

    f = open("merkle.trees", 'w')
    f.writelines(json1)
    f.writelines("\n")
    f.writelines(json2)
    f.close()

    sub_tree_verify(tree1, tree2)

    proof = {"plaintext":[], "hash_value": []}
    sub_proof(len(tree1), tree2, True)
    print("[" + find_list_root_hash(tree1) +", "
          + str(proof["hash_value"]) +", "
          + find_list_root_hash(tree2) + "]")

    """ 
    The last line to show detail of the proof.
    If you hope to clearly look through about the proof, remove "#" please
    """
    # print("Proof--Need to be hashed list:" + str(proof["plaintext"]))