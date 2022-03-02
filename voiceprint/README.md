Branch1 -- train_ubm.m

​	**训练**一个通用背景模型（基于CNC2）

​	保存通用背景模型到/model目录下



Branch2 -- enroll.m

​	**加载**通用背景模型

​	**更新**通用背景模型

​	保存



Branch3 -- verify.m

​	**加载**模型

​	进行判断，输出一个结果



Branch.m

Main.m

基本结构

```
	if arg = 1：
		train_ubm()  #只在初次部署时运行
	elif arg = 2:
		save()    #输入：注册所用的一段音频；输出：无
    elif arg = 3:
    	enroll()
    	verify() #输入：一段音频 输出：true or false

​		
```

