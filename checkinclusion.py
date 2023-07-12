import json
import hashlib
import sys

def root_verify(test_element, proof_dic, json_data):
    vef = hashlib.sha256(test_element.encode('utf-8')).hexdigest()
    for j in range(0, len(proof_dic['proof'])):
        if proof_dic['direction'][j] == 'R':
            vef = hashlib.sha256((vef + proof_dic['proof'][j]).encode('utf-8')).hexdigest()
        else:
            vef = hashlib.sha256((proof_dic['proof'][j] + vef).encode('utf-8')).hexdigest()
    print(vef == json_data['root'])

if __name__ == '__main__':
    f = open('merkle.tree', 'r')
    data = json.loads(f.readline())

    ini_target = sys.argv[1]
    find_target = hashlib.sha256(ini_target.encode('utf-8')).hexdigest()

    proof = {'proof': [], 'direction': []}
    for i in range(0, data['level_num']-1):
        level = "level" + str(i)
        if find_target in data['level'][level]:
            target_index = data['level'][level].index(find_target)
        else:
            print("no")
            sys.exit()


        if target_index % 2 == 0:
            try:
                pair = data['level'][level][target_index + 1]
                find_target = hashlib.sha256((find_target + pair).encode('utf-8')).hexdigest()
                proof['proof'].append(pair)
                proof['direction'].append("R")
            except:
                find_target = find_target
        else:
            pair = data['level'][level][target_index - 1]
            find_target = hashlib.sha256((pair + find_target).encode('utf-8')).hexdigest()
            proof['proof'].append(pair)
            proof['direction'].append("L")
    print("yes", end=" ")
    print(proof['proof'])

    # use the method to verify the audit path
    # root_verify(ini_target, proof, data)