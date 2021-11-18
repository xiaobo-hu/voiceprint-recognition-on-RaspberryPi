## lip_tracking module

#### system requirements 

cmake

libboost-python-dev

libglib2.0-0



#### python requirements

python (3.6.13)

opencv-python (4.5.3.56)

dlib (19.7.0)



#### Usage

1.  若通过本地视频进行测试

   cd 到源码目录下，执行：

   ​	`python cur_lip_tracking.py -i input.mp4`

2. 树莓派实时拍摄视频

   注释掉代码中 step1部分，并将step 3中参数修改为0

