# -*- coding: utf-8 -*-
# @Time : 2020/5/18 12:08
# @Author : Yang
# @File : test.py
# @Software: PyCharm

# arr = []
# contents = open('basedata.txt','r')
# for content in contents:
#     if not content.startswith("@"):  # @后面是注释部分
#         # print('reading...\n')
#         content.strip('\n')  # 去掉回车
#         content.split(' ')  # 空格分割，因为list用逗号分割了
#         arr.append(content)
# for i in range(len(arr)):
#     print(arr[i][0])



# #test of seek in IO:
# with open('basedata.txt', "w+") as f:
#     read_data = f.read()
#     f.seek()
#     f.truncate()  # 清空文件
#     f.close()
# contents = open('basedata.txt','r')
# print(contents)


# #test of arr  $05191743
# ans = {
#   "nodes": [
#     {
#       "name": "beijing",
#       "id": 1
#     },
#     {
#       "name": "shanghai",
#       "id": 2
#     },
#     {
#       "name": "chengdu",
#       "id": 3
#     }
#   ],
#   "edges":[
#       {
#           "start":1,
#           "end":3,
#           "time":23,
#           "price":203
#       },{
#           "start":2,
#           "end":3,
#           "time":23,
#           "price":203
#       },{
#           "start":1,
#           "end":2,
#           "time":23,
#           "price":203
#       }]
# }  # data from you, include "nodes" and "edges" in a dictionary
# arr = []  # 数据库读取结果
# res = []  # 返回的那个列表
# length = len(ans['nodes'])   # ans中id的个数
# def openData():
#     '''打开TXT文件读取'''
#     contents = open('basedata.txt','r')
#     for content in contents:
#         if not content.startswith("@"):  # @后面是注释部分
#             # print('reading...\n')
#             content.strip('\n') # 去掉回车
#             content.split(',')  # 逗号分割
#             arr.append(content)
#     print("reading data already!")
#     # return arr  #存储读取到的（现有的）数据
#     contents.close()
# openData()
# lines = arr[1].split(' ')
# print('arr:',arr)
# print(lines[4])

# #test of IO
# arr = []
# with open('basedata.txt') as contents: # 文件句柄存储
#     '''打开TXT文件读取'''
#     for content in contents:
#         if not content.startswith("@"):  # @后面是注释部分
#             # print('reading...\n')
#             content.strip('\n') # 去掉回车
#             content.split(',')  # 逗号分割
#             arr.append(content)
#     print("reading data already!")
#     # return arr  #存储读取到的（现有的）数据
# print(len(arr))


# test of json
ans = {
  "nodes": [
    {
      "name": "shanghai",
      "id": 1
    },
    {
      "name": "shanghai",
      "id": 1
    }
  ],
  "edges":[
      {
          "start":1,
          "end":3,
          "time":22,
          "price":203
      },{
          "start":3,
          "end":4,
          "time":33,
          "price":666
      }]
}
print(ans.keys())

temp1 = 'edges'
temp2 = 'price'
# print(ans["nodes"][1]['id'])
print('len of edges:',len(ans[temp1]))
# ans["nodes"].append('beijing')
# print(ans['nodes'])
print(ans['edges'][0]['time'])

# '' [
# '' {
# '' "id":1,
# '' "name":"source",
# '' "neighbour":[1,2],//邻居节点的id
# "price":[12,23]//到达邻居节点的所耗资⾦
# '' },
# '' ]