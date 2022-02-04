#!/usr/bin/env python
# coding: utf-8

# In[1]:


###List


# In[2]:


li=[1,2,3,4,5,6,7,8]
print(li)


# In[3]:


li.append(9)


# In[4]:


li


# In[5]:


li.sort()


# In[6]:


li


# In[7]:


li.reverse()


# In[8]:


li


# In[9]:


li.insert(0,0)


# In[10]:


li


# In[11]:


li2=list(range(10,21))


# In[12]:


type(li2)


# In[13]:


li2


# In[14]:


li.extend(li2)


# In[15]:


li


# In[16]:


li.count(9)


# In[17]:


li2.count(9)


# In[18]:


li.remove(5)


# In[19]:


li


# In[20]:


li.pop()


# In[21]:


li


# In[22]:


li.pop(0)


# In[23]:


li


# In[24]:


li.sort() 


# In[25]:


li


# In[26]:


li.pop(0)


# In[27]:


li.pop(0)


# In[28]:


li.pop(0)


# In[29]:


li


# In[30]:


li=[0]*100


# In[31]:


li


# In[32]:


li2


# In[33]:


li1


# In[34]:


li1=li2


# In[41]:


li1


# In[42]:


li2


# In[43]:


li2[9]


# In[44]:


li2[9]=9


# In[45]:


li2


# In[46]:


li1.pop()


# In[47]:


li1


# In[48]:


li2


# In[49]:


###Solution of this problem


# In[50]:


li=[1,2,3,4]
li2=[]
li2.extend(li)


# In[51]:


li2


# In[52]:


li3=list(li)


# In[53]:


li3


# In[54]:


li4=li


# In[55]:


li4


# In[56]:


li[0]=0


# In[57]:


li


# In[58]:


li2


# In[59]:


li3


# In[60]:


li4


# In[61]:


stack=[] 


# In[62]:


stack.append(2)


# In[63]:


stack


# In[64]:


stack.append(3)


# In[65]:


stack.append(5)


# In[66]:


stack.append(7)


# In[67]:


stack


# In[68]:


stack.pop()


# In[69]:


stack


# In[70]:


q=[]


# In[71]:


q.append(1)


# In[72]:


q.append(2)


# In[73]:


q.append(3)


# In[74]:


q


# In[75]:


q.pop(0)


# In[76]:


q


# In[77]:


li=list(range(1,21))


# In[78]:


li


# In[79]:


even=[]


# In[80]:


for item in li:
    if item%2==0:
        even.append(item)


# In[81]:


even


# In[82]:


odd=[item for item in li if item%2==1]


# In[83]:


odd


# In[84]:


###tuple


# In[85]:


tpl=()


# In[86]:


tpl


# In[87]:


tpl=(1,2,3,[1,2,3])


# In[88]:


tpl


# In[89]:


tpl[1]


# In[90]:


tpl[3]


# In[91]:


tpl[3][2]


# In[92]:


###tuple is not mutable


# In[93]:


t=(1,2,3)


# In[94]:


a,b,c=t


# In[95]:


a


# In[96]:


b


# In[97]:


c


# In[98]:


x=5
y=8
t=x,y


# In[99]:


t


# In[100]:


tpl=(1,2,3,'string',3.5)


# In[101]:


tpl


# In[102]:


type(tpl)


# In[103]:


tpl[3]


# In[104]:


tpl[4]


# In[105]:


tpl[-1]


# In[106]:


tpl[-3]


# In[107]:


###Type casting to list


# In[108]:


li=list(tpl)


# In[109]:


li


# In[110]:


type(li)


# In[111]:


tpl_new=1,2,3


# In[112]:


tpl_new


# In[113]:


type(tpl_new)


# In[114]:


a,b,c=tpl_new



# In[115]:


tpl_new


# In[116]:


a


# In[117]:


b


# In[118]:


c


# In[119]:


#this is  unpack


# In[120]:


t=1


# In[121]:


type(t)


# In[122]:


t=(1,)


# In[123]:


type(t)


# In[124]:


tpl


# In[125]:


for i in tpl:
    print(i)


# In[126]:


tpl_new


# In[127]:


tpl_new[0]


# In[128]:


tpl_new[0]=7


# In[129]:


##becaue not mutable


# In[130]:


li=[1,2,3,[4,5,6]]


# In[131]:


li


# In[132]:


for i in li:
    print(i)


# In[133]:


tpl=(1,2,3,(4,5,6))


# In[134]:


for i in tpl:
    print(i)


# In[135]:


#So both can be nested


# In[136]:


###Set


# In[137]:


a=set()


# In[138]:


a


# In[139]:


type(a)


# In[140]:


a=set(1,2,3)


# In[141]:


a=set(1)


# In[142]:


#as iterable is asked, lets try tuple and list


# In[143]:


tpl=(1,2,3,4,5)


# In[144]:


a=set(tpl)


# In[145]:


a


# In[146]:


li=[2,3,5,7]


# In[147]:


b=set(li)


# In[148]:


type(b)


# In[149]:


b


# In[150]:


#so one parameter and that should be iterable


# In[151]:


a|b


# In[152]:


a&b


# In[153]:


a ^ b


# In[154]:


print(a^b)


# In[155]:


7 in a


# In[156]:


7 in b


# In[157]:


##a string is iterable as well, so it can be used as well


# In[158]:


c=set('abcd')


# In[159]:


c


# In[160]:


#one use of set is to remove duplicate


# In[161]:


li=[1,1,2,2,2,4,3,5,2,2,3,7,8,9]


# In[162]:


li


# In[163]:


k=set(li)


# In[164]:


k


# In[165]:


li


# In[166]:


li=list(set(li))


# In[167]:


li


# In[168]:


#dictionary


# In[169]:


dt={'a':'A','b':'B'}


# In[170]:


dt


# In[171]:


dt['a']


# In[172]:


dt['b']


# In[173]:


result={1:90,2:95,3:98}


# In[174]:


result[3]


# In[175]:


#key should be something not-mutable as string, tuple


# In[176]:


result['rafi']=95


# In[177]:


result


# In[178]:


result['rafi']=97


# In[179]:


result


# In[180]:


div={'dhaka':10,"chit":15, 'sylhet':8, 'khulna':20,'Rajshahi':12, "rangpur":10,'barishal':8}


# In[181]:


div


# In[182]:


type(div)


# In[183]:


div['dhaka']


# In[184]:


div['dhaka']=15


# In[185]:


div


# In[186]:


del div['khulna']


# In[187]:


div


# In[188]:


div['khulna']=25


# In[189]:


div


# In[190]:


div['mymensingh']=12


# In[193]:


div


# In[197]:


for item in div:
    print(item)


# In[198]:


for item in div:
    print(item,div[item])


# In[204]:


div.keys()


# In[206]:


get_ipython().run_line_magic('pinfo2', 'div')


# In[207]:


div.keys()


# In[208]:


div.values()


# In[209]:


# to get both use iteritem


# In[212]:


for key, value in div.items():
    print(key,value)


# In[213]:


div.items()


# In[214]:


#items() make it iterable for loops


# In[216]:


for x in div.items():
    print(x)


# In[ ]:


# here we can see items() is making it into a list of tuple(which is also iterable). which is iterator actually

