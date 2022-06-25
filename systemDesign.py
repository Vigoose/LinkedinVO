"""
设计real time TopK: https://www.1point3acres.com/bbs/thread-823737-1-1.html
这一轮想问下大家到底应该怎么设计
我是参照的油管俄罗斯小哥🔗www.youtube.com的讲解 
我先说的slow track partition and aggregate the data and then do 2 map reduce jobs那个方法 然后对方说太慢了 
我就说了count main sketch to get ferquency count然后 partition each key to different servers, 
get top k for each server locally and then merge k sorted list. 然后对方重点follow up了需要不同的k比如10 100 1000 
以及time period 可能会变的问题 比如想知道last 5 mins, last 1 hour, last 24 hours。这里有一个点 
就是我说我们可以store 5 min data into a file, for example, 10:00 - 10:05, 10:05 - 10:10..
对方就问那这样如果我们想知道10:02 - 10:07的top k怎么办 我想了也只能实时储存比如每秒钟都send message and then calculate..但对方明显不是很满意。。
不知道大家觉得因该怎么处理
还有一个问题就是如果我们store top k in the past 5 mins,但我们想get top k in the past 10 mins,不能简单 merge 两个5 min file. 这个应该怎么处理？
设计 calendar User可以创event邀请其他人,收到的人可以接受/拒绝, 在自己的calendar可以看到自己创的和受邀请的event.
设计malicious ip/blacklist: https://www.1point3acres.com/bbs/thread-841667-1-1.html
设计messge queue  https://www.1point3acres.com/bbs/thread-812910-1-1.html
设计search document 两个API load和search inverted index
设计公司权限系统 https://www.1point3acres.com/bbs/thread-813582-1-1.html
设计metrics aggregation and monitoring system: 🔗www.youtube.com
key-value store  https://www.1point3acres.com/bbs/thread-841026-1-1.html
设计Autocomplete System https://www.1point3acres.com/bbs/thread-834306-1-1.html
rate limiter https://www.1point3acres.com/bbs/thread-843111-1-1.html
SD: 非常规sd, 要求设计一个系统在一个地图上显示领英新注册用户的地理位置, 问了一下QPS说只有10, 感觉single host都可以解决
"""