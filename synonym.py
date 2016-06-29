
# coding: utf-8

# ## 一些list的用法

# In[40]:

a = [1,4,'a',3,5]
print a.index('a')  #印出'a'在list出現的位置 -> [2]
print a[:2]  #印出[2]之前的字串
print a[2:]  #印出[2]之後(包含[2])的字串


# ## 試著把同義詞配對

# In[103]:

a=['牛奶','牛乳','鮮奶','鮮乳']
dic={}
for i in a[1:]:  #除了牛奶，依序把'牛乳','鮮奶','鮮乳'丟給 i
    dic[i] = a[0]  #把牛乳(=dic[0])、鮮奶(=dic[1])、鮮乳(=dic[2])與牛奶(=a[0])配對
print dic
print '========='

for k in dic:
    print k + '是key'
print dic.values()[0] + '是value'
print '========='

for j in xrange(0,3):
    print dic.keys()[j]+':'+dic.values()[j]


# In[104]:

#把同義詞建成字典
test_file1 = open('classification.txt','r')
dic={}
for i in test_file1.readlines():
#     a = i.split(',')
#     print a[:2]
    if '' in i.split(','): 
        a = i.split(',')[:i.split(',').index('')] #如果有空白的話，把後面空白截掉
        for j in a[1:]:
            dic[j] = a[0] #把同義詞對到食材
    else:
        a = i.split(',') 
        for j in a[1:]:  
            dic[j] = a[0]
            
test_file2 = open('dic_add.txt','w')
for k in dic:
    test_file2.write(k+':'+dic.values()[0]+'\n')  #將dic寫出存成txt檔

# for k in dic:
#     test_file2.write(k+' 3'+' n'+'\n') #變成jieba字典的格式加到jieba字典
    
test_file2.close()
test_file1.close()

