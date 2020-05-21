import sys
sys.path.append('../utils/exam1/part4')
import Funcget

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
} 
print(Funcget.get(ans) )