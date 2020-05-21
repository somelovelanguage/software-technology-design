# -*- coding: utf-8 -*-
# @Time : 2020/5/20 9:12
# @Author : Yang
# @File : postbackups.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time : 2020/5/19 9:13
# @Author : Yang
# @File : Funcpost.py
# @Software: PyCharm
# REFERENCE： https://blog.csdn.net/weixin_44677409/java/article/details/89185785
'''如果需要修改文件，第45行；如果需要修改往文件写入的内容，第68-71行'''

import os   #修改文件用，不用理会

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
    },
    {
        "name": "woc",
        "id": 6
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
      },{
            "start":6,
            "end":7,
            "time":123,
            "price":456
      }]
}  # data from you, include "nodes" and "edges" in a dictionary
arr = []  # 数据库读取结果
res = []  # 返回的那个列表
lenOfReq = len(ans['nodes'])  #请求中存放节点的数量

def openData(filename):
    '''打开TXT文件读取'''
    contents = open(filename,'r')
    for content in contents:
        if not content.startswith("@"):  # @后面是注释部分
            # print('reading...\n')
            content.strip('\n') # 去掉回车
            content.split(' ')  # 空格分割，因为list用逗号分割了
            arr.append(content)
    print("reading data already!\n")
    return arr  #存储读取到的（现有的）数据
    # contents.close()

def post(ans):
    '''建⽴⼀个节点表，也就是在本地txt⽂件中保存节点信息，如果已经建⽴过则覆盖它'''
    flag = 0    #  标识res列表是否为空
    arr = openData('basedata.txt')
    length = len(arr)  # 目前已有节点数量，由于从0开始，但第一行是注释，所以不用   减一
    print("length is :", length)
    # deled = 0#如果已经删除过一次，会导致序号改变，这里做标识
    for num in range(lenOfReq):   # 根据id来查表
        id = ans['nodes'][num]['id']
        Exist = idExist(id) #数据已存在，删除后重新写入
        if Exist:
            # print('Exist:',Exist)

            '''添加新的记录'''
            id = str(ans['nodes'][num]['id'])   # id
            name = str(ans['nodes'][num]['name'])   # name
            neighbor = []  # neighbor
            time = []  # time
            price = []  # price
            for i in range(len(ans['edges'])):
                if int(ans['edges'][i]['start']) == int(id):
                    neighbor.append(ans['edges'][i]['end'])
                    time.append(ans['edges'][i]['time'])
                    price.append(ans['edges'][i]['price'])

            # 如果需要新项，可以手动添加
            temp = str(Exist) + ' ' + id + ' ' + '\'' + name + '\'' + ' ' + str(neighbor) + ' ' + str(time) + ' ' + str(price) +'\n'
            # print('temp_change:',temp)
            del arr[Exist-1]  #   如果已有记录，删掉
            # deled = deled + 1
            arr.insert(Exist-1,temp)

            print('new:',arr)
        else:
            '''添加新的记录'''
            length = length + 1 #写在最后一行
            id = str(ans['nodes'][num]['id'])  # id
            name = str(ans['nodes'][num]['name'])  # name
            neighbor = []  # neighbor
            time = []  # time
            price = []  # price
            for i in range(len(ans['edges'])):
                if int(ans['edges'][i]['start']) == int(id):
                    neighbor.append(ans['edges'][i]['end'])
                    time.append(ans['edges'][i]['time'])
                    price.append(ans['edges'][i]['price'])

            # 如果需要新项，可以手动添加
            temp = '\n' + str(length) + ' ' + id + ' ' + '\'' + name + '\'' + ' ' + str(neighbor) + ' ' + str(time) + ' ' + str(
                price) + '\n'
            # print('temp_change:',temp)
            # arr[Exist] = arr[Exist] + temp
            arr.append( temp)

            # print('temp_add:',temp)
            print('new:',arr)

        flag = 1    #表示返回数组res费控
    # contents.close()

    def modify_text():
        '''清空文件test_new.txt'''
        with open('test_new.txt', "w+") as f:
            read_data = f.read()
            f.seek(0)
            f.truncate()  # 清空文件
            f.close()
    #写回文件
    modify_text()
    f = open('test_new.txt', 'w', encoding="utf-8")
    print('arr:',arr)
    f.writelines(arr)
    f.close()
    # backups文件如果存在则无法被创建，所以无论如何先删除了
    if os.path.exists('backups.txt'):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove('backups.txt')
    os.rename('basedata.txt', 'backups.txt')
    os.rename('test_new.txt', 'basedata.txt')
    #依然是basedata存储我们的数据，backups作为回收站/xyx

    #测试用
    # print(arr)
    if flag == 1:
        return {'status':'added'}
    else:
        return {'status':'success'}

def idExist(id):
    '''通过id来检索，请求的数据是否已经存在
        其实有些问题，逗号也读进来了/px，所以下标其实是2n而不是n-1'''
    #上述问题已经解决，用split即可
    for ar in arr:
        if ar:
            lines = ar.split(' ')
            # print('ar:',ar)
            if int(lines[1]) == id:
                return int(lines[0])
    return 0

if __name__ == '__main__':
    print(post(ans))

