#!/home/ec2-user/anaconda3/bin/python3.6
# -*- coding: utf-8 -*-


x = [1,2,3,4,5,6,7,8]
y = [22,55,44,66,33]
z = [44,1,8,55,4,2,33]
dic1={'a':['1','2'],'b':['4','1']}
dic2={'d':['4','7'],'a':['5','1','6']}
print("元dic1= ",dic1)

def merge(dic1,dic2):
    new_dic = dic1.copy()
    for usr in dic2:
        if usr not in new_dic.keys():
            new_dic[usr]=[]
        for srv in dic2[usr]:
            if srv not in new_dic[usr]:
                new_dic[usr][:].append(srv)
    return new_dic

def merge1(mydic1,mydic2):
    new_dic = mydic1.copy()
    for usr in mydic2:
        new_dic[usr]=["yassine"]
        print("dic1= ",mydic1)
    return new_dic

print("merge= ",merge(dic1,dic2))
print("dic1= ",dic1)
