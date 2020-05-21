# -*- coding: utf-8 -*-
# @Time : 2020/5/20 14:04
# @Author : Yang
# @File : getbackups.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time : 2020/5/19 9:13
# @Author : Yang
# @File : Funcget.py
# @Software: PyCharm

ans = {
  "nodes": [
    {
      "name": "beijing",
      "id": 1
    },
    {
      "name": "shanghai",
      "id": 2
    },
    {
      "name": "chengdu",
      "id": 3
    }
  ],
  "edges":[
      {
          "start":1,
          "end":3,
          "time":23,
          "price":203
      },{
          "start":2,
          "end":3,
          "time":23,
          "price":203
      },{
          "start":1,
          "end":2,
          "time":23,
          "price":203
      }]
}  # data from you, include "nodes" and "edges" in a dictionary
arr = []  # 数据库读取结果
res = []  # 返回的那个列表
length = len(ans['nodes'])   # ans中id的个数

def openData(filename):
    '''打开TXT文件读取'''
    contents = open(filename,'r')
    for content in contents:
        if not content.startswith("@"):  # @后面是注释部分
            # print('reading...\n')
            content.strip('\n') # 去掉回车
            content.split(' ')  # 空格分割，因为list用逗号分割了
            arr.append(content)
    # print("reading data already!")
    return arr  #存储读取到的（现有的）数据
    # contents.close()

def get(ans):
    '''若本地已经建⽴此表，则将此表返回，若没有返回[]'''
    flag = 0    #  标识res列表是否为空
    arr = openData('basedata.txt')
    # print(arr[1][0])  #输出上海的id
    for num in range(length):   # 根据id来查表
        temp = {}  # 存储当前循环返回的内容
        id = ans['nodes'][num]['id']
        # print('id:',id)
        Exist = idExist(id)
        # print(arr)
        if Exist:
            lines = arr[Exist-1].split(' ')
            temp['id'] = lines[1]
            temp['name'] = lines[2]
            temp['neighbor'] = lines[3]
            temp['time'] = lines[4]
            temp['price'] =lines[5]
            res.append(temp)
            flag = 1    #表示返回数组res费控
        else:continue
    if flag == 1:
        return res
    else:
        return []

def idExist(id):
    '''通过id来检索，请求的数据是否已经存在
        其实有些问题，逗号也读进来了/px，所以下标其实是2n而不是n-1'''
    #上述问题，可以通过split解决
    for ar in arr:
        if int(ar[2]) == id:
            # print('ar:',ar)
            return int(ar[0])
    return 0

if __name__ == '__main__':
    print(get(ans))