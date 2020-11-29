import queue  #线程队列

# 最多放3个数据
# 先进先出
q = queue.Queue(3) #FIFO
q.put(12)
q.put('hello')
q.put({'name':'alex'})
q.put_nowait(33) # -==>q.put(blcok=False)
print(q.qsize())  # 元素个数
print(q.empty())  #是否为空
print(q.full())  #是否为满
""" 
成对出现,发送信号
q.task_done()
q.join() 
"""
# q.put(18,False)
# while 1:
#     date = q.get(block=False)
#     print(date)
#     print('---------')

# 先进后出
# q2 = queue.LifoQueue()  # FILO
# q2.put(12)
# q2.put('hello')
# q2.put({'name':'alex'})
# while 1:
#     date = q2.get(block=False)
#     print(date)
#     print('---------')


# 按照优先级
q2 = queue.PriorityQueue()
q2.put([2,12])
q2.put([4,'hello'])
q2.put([5,{'name':'alex'}])
while 1:
    date = q2.get(block=False)
    print(date[1])
    print('---------')