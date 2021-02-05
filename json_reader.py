import json
#
# A : 5
# B : 1
# C : 4
# D : 2
# E : 1
# F : 3

json_msg = [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]


def element_present(subel):
    if len(subel) > 0:
        for i in range(len(subel)):
            if subel[i] in res.keys():
                res[subel[i]] += 1
            elif subel[i] not in res.keys():
                res[subel[i]] = 1


if __name__ == "__main__":
    res = {}
    for i in range(len(json_msg)):
        element_present(json_msg[i]['name'])
        element_present(json_msg[i]['parents'])

    l_res = list(res.keys())
    l_res.sort()


    for i in l_res:
        print(str(i) + ' : ' + str(res[i]))
