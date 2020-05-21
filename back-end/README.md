## resources
  productTable 物品记录表
  nodeTable 节点记录表
## models
	对应resources的类，提供并管理类下操作用到的逻辑
## database
	作为数据库使用，保存文件到此文件夹

## 各资源method ##
资源名|method|url|describtion
---|:--:|:--:|---:
 products| get |api/products/products|get all products
 products| get |api/products/sortedproducts|get sorted products
 products| get |api/products/dividedproducts|get divided products
 products| get |api/products/arrivaltime|get products arrival time
 products| post |api/products|add one product
 product|  delete |api/products|delete one product
 product|  put |api/products|change one product
nodes |get |api/nodes|get all nodes
 nodes |post |api/nodes|set a nodes table


