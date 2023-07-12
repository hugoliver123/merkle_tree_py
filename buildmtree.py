import hashlib
import json
import sys

def input_string_to_list(user_input: str) -> list:
    user_input = user_input[1:-1]
    split_str = user_input.split(",")
    for i in range(0, len(split_str)):
        split_str[i] = split_str[i].strip()
    return split_str

def json_tree(tree, ori_input):
    dic = {"root": tree[-1][0], "level_num": len(tree), "row_data": ori_input}

    level = {}
    for i in range(0,len(tree)):
        index = "level" + str(i)
        level.update({index: tree[i]})
    dic.update({"level": level})
    return json.dumps(dic)

def print_tree(p_tree):
    p_tree.reverse()
    for i in p_tree:
        print(i)
    print(strin)

def tree_build(stri):
    tree = []
    leaf = []
    for i in stri:
        leaf.append(hashlib.sha256(i.encode("utf-8")).hexdigest())
    tree.append(leaf)

    while len(tree[-1]) != 1:
        up_leaf = []
        for i in range(0, len(tree[-1]), 2):
            try:
                content = tree[-1][i] + tree[-1][i + 1]
                up_leaf.append((hashlib.sha256(content.encode("utf-8")).hexdigest()))
            except:
                content = tree[-1][i]
                up_leaf.append(content)
        tree.append(up_leaf)
    return tree

if __name__ == '__main__':

    strin = input_string_to_list(sys.argv[1])
    tree_out = tree_build(strin)

    f = open("merkle.tree",'w')
    f.writelines(json_tree(tree_out, strin))
    f.close()
    # print_tree(tree_out)