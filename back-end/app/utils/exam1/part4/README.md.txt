1、函数与文件
	主函数有   get：若本地已经建⽴对应的节点表，则将此表返回，若没有返回[]
		post：建⽴⼀个节点表，也就是在本地的txt⽂件中保存节点信息，如果已经建⽴过则覆盖它
			元数据会转存到backups.txt，新输入会覆盖basedata.txt文件，每次循环都是如此。
		函数的对应输入格式为全局变量ans的格式（json）
	test是我实验语法的地方，不用理会
	basedata.txt是内容存储的地方
	以上所有函数亲测可用

2、TXT与格式
	内容寻处在database.txt文件中，格式为：
	@开头的注释部分和直接数据开头的存储部分，没有用%分割

	数据存储可以在末尾添加比如vip之类的新项，不影响
	可以交换每一行的顺序用于排序等工作，不要删除行号就可以
		time和price要与邻居neighbor得到数量对应，所以他们的属性都是str
		即：行号（int）——id（int）——neighbor（list）——time（list）——price（list）
		P.S.实际上用空格分隔，本文件中以防误解用“——”代替
	    
	可以添加为比如：行号，id，name，neighbor, time, price,vip   ,heiheihei,……
	但不要在“行号，id，name，neighbor, time, price”之间插入新的内容
		P.S.因为空格不易察觉，此处用逗号代替。实际上是空格分隔

3、TXT读取：
	get和post函数中有明确openfile函数，可以读取对应TXT文件
		注意withopen函数会自动关闭文件，我因为这调了半天
	如果需要pandas或者其他文件读写操作可以Q我，也许会有现成函数

4、调用方法：
	get(ans)  或者  post(ans)
	ans是json格式传输，由'nodes'和'edges'两个列表组成，可以重复，可以数量不一致 /xyx
	get函数会返回json格式的对应请求数据
	post函数会返回{'status':'added'}或者{'status':'success'}表明是否对节点表做了修改

4、TXT文件
	修改basedata.txt文件中的内容，本次操作前的内容可以再backups.txt找到，以防误操，但只能存储最近一次的结果！！，如果有需要建议在本机上备份。
	文件读写直接嵌入函数中，只要将存储信息的TXT文件放在同一目录下，命名为basedata.txt和backups.txt即可