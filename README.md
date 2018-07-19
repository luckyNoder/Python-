## Python 3.x 入门
 >数据类型   
 
*** 
#### Number 类型
```Python
# int    整形
# float   浮点型
# Python  只有 float
# 其他语言中又分单精度 (float) 和爽精度 ( double )

type (2/2)   # 输出 float 1.0
type (2//2)  # 输出 int 1
# 双//  只保留整数部分
```
#### Boolean
```Python
# 任何空值都是---->false
print(r"hello \n world") # 输出  hello\world 所见即所得
```

#### String

```Python
1. "hello world"[0:5]  # 输出 hello
2. "hello world"[-5:]  # 输出 world
```

##### list

```Python
1. ["死神","大剑","妖怪名单"] [0] #输出 死神
2. ["死神","大剑","妖怪名单"] [1:] #输出 大剑 妖怪名单
3. ["死神","大剑","妖怪名单"] [-2:] #输出 大剑 妖怪名单
4. ["死神","大剑","妖怪名单"]*2 #输出 ["死神","大剑","妖怪名单","死神","大剑","妖怪名单"]

# 3 是不是在 ["死神","大剑","妖怪名单"]
3 in ["死神","大剑","妖怪名单"]
# 输出 False

# 3 是否不在 ["死神","大剑","妖怪名单"]
3 not in ["死神","大剑","妖怪名单"]
# 输出 False
```

