# DailyQuestion
Python之禅和他朋友们知识星球的每日一题  https://t.xiaomiquan.com/IUFmuFu

## 第6题

设计一个程序，用于统计一个项目中的代码数，包括文件个数，代码行数，注释行数，空行行数。尽量设计灵活一点可以通过输入不同参数来统计不同语言的项目

例如执行：
```
# type用于指定文件类型
python counter.py --type python
```

输出：

```
files:10
code_lines:200
comments:100
blanks:20
```

## 第5题：

一个完整的URL由5部分组成，格式为：

```
<scheme>://<netloc>/<path>?<query_params>#<fragment>
```

例如
```python
url = "http://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652566513#wechat_redirect"
```
解析后得到：
```
scheme='http'
netloc='mp.weixin.qq.com'
path='/s'
query_params='__biz=MzA4MjEyNTA5Mw==&mid=2652566513'
fragment='wechat_redirect'
```

问题：设计一个算法，将URL转换成5部分，注意，query_params 要转换成字典类型

```
query_params={'__biz': 'MzA4MjEyNTA5Mw==', 'mid=2652566513'}
```

提示：字符串在编程中是最常用的操作之一，这个题目主要是要求大家熟悉字符串的常用方法。此外，大家尽可能用抽象、面向对象的风格来写。可以设计一个URL的类，还有一个算法，大概的框架就是下面这样子。

```python
class URL:
	....
    pass

def url_parse(url):
	.....
	return URL(xxx)
```

## 第4题：

用Python实现斐波那契数列，费波那契数列由0和1开始，之后的费波那契系数就是由之前的两数相加而得出，例如前 斐波那契数列 0, 1, 1, 2, 3, 5, 8, 13, 21, 34。用数学方法可定义为如图所示：

![fib](./images/fn.png)


## 第3题：
统计一个文件中每个单词出现的次数，列出出现频率最多的5个单词。

## 第2题：

设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。

## 第1题：

在使用 for 循环迭代一个列表时，有时我们需要获取列表中每个元素所在的下标位置是多少，例如：有列表 numbers = [10, 29, 30, 41]，要求输出 (0, 10)，(1, 29)，(2, 30)，(3, 41)










