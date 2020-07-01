# -*- coding: utf-8 -*-
# funplus(点点互动)题目

'''
1.现有一个长度确定的整型数组，需要找出所有重复出现的数字，并返回包含这些数字的数 
组，比如[1,20,31,4,4, 20,2]中的重复的数字为[4, 20], 不限语言，请尝试找到最优解 
'''
def findRepeatNum(arr):
    flagDic = {}
    ret = []
    for n in arr:
        if n in flagDic and flagDic[n] != n+1:
            ret.append(n)
            flagDic[n] = n+1
        else:
            flagDic[n] = n
    return ret

'''
2.现有两个不为空的单向链表，分别储存了两个逆序的整数，
现需要算出两个链表表示数字的 和，也用单向链表返回。比如：单向链表(5 -> 6 -> 3) 表示整数365, 单向链表(1 -> 8 - > 3) 表示整数 381, 两链表相加结果应该为 单向链表(6 -> 4 -> 7)
'''
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def addList(l1, l2):
    rethead = ListNode(0)
    node1 = l1
    node2 = l2
    curNode = rethead
    carry = 0
    while node1 or node2:
        v1 = node1.val if node1 else 0
        v2 = node2.val if node2 else 0
        sum = v1 + v2 + carry
        curNode.next = ListNode(sum % 10)
        curNode = curNode.next
        carry = sum // 10
        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next
    if carry > 0:
        curNode.next = ListNode(carry)   

    return rethead.next

'''
3.请用你最熟悉的语言，使用面向对象设计思想，设计一个学生的简历模块，写出每个类。
'''
import re
class BaseInfo:
    def __init__(self, name, age, cellphone, identity, about):
        self.name = name
        self.age = age
        self.identity = identity
        self.cellphone = cellphone
        self.about = about
    def __str__(self):
        return f'name: {self.name} \nage: {self.age} \ncell: {self.cellphone} \nid: {self.identity} \nabout: {self.about}\n----------------\n'
    # @property
    # def name(self):
    #     return self.name

    # @name.setter
    # def name(self, name):
    #     assert name, 'name must not be none'
    #     self.name = name
    
    # @property
    # def age(self):
    #     return self.age

    # @age.setter 
    # def age(self, age):
    #     assert age > 0, 'age must big than 0'
    #     self.age = age
    
    # @property
    # def cellphone(self):
    #     return self.cellphone
    
    # @cellphone.setter
    # def cellphone(self, cellphone):
    #     assert re.match(r'^1[3,5,6,7,8,9]{1}[0-9]{9}$', cellphone), 'invalid cellphone num'
    #     self.cellphone = cellphone
    
    # @property 
    # def identity(self):
    #     return self.identity

    # @identity.setter 
    # def identity(self, identity):
    #     assert re.match(r'^[1,2,3,4,5,6,7,8,9]{1}\d{9}(\d | \w){1}'), 'invalid identity'
    #     self.identity = identity
    
class WorkInfo:
    def __init__(self, works=[]):
        self.worklist = []
        self.worklist.extend(works)
    # 公司名字， 开始结束时间，职位，工作内容
    def addWork(self, company, starttime, endtime, position, content):
        aWork = {}
        aWork['company'] = company
        aWork['starttime'] = starttime
        aWork['endtime'] = endtime
        aWork['position'] = position
        aWork['content'] = content
        self.worklist.append(aWork)
    def __str__(self):
        ret = ''
        for work in self.worklist:
            awork = f"company: {work['company']}  starttime: {work['starttime']}  endtime: {work['endtime']}  position: {work['position']} \ncontent: {work['content']}\n"
            ret = ret + awork
        ret = ret + '----------------\n'
        return ret

class EduInfo:
    def __init__(self, edus=[]):
        self.edulist = []
        self.edulist.extend(edus)
    def addEdu(self, school, starttime, endtime, degree):
        aEdu = {}
        aEdu['school'] = school
        aEdu['starttime'] = starttime
        aEdu['endtime'] = endtime
        aEdu['degree'] = degree
        self.edulist.append(aEdu)
    def __str__(self):
        ret = ''
        for edu in self.edulist:
            aedu = f"school: {edu['school']}  starttime: {edu['starttime']}  endtime: {edu['endtime']}  degree: {edu['degree']} \n"
            ret = ret + aedu
        return ret

class PersonalResume:
    def __init__(self, baseInfo, workInfo, eduInfo):
        self.baseInfo = baseInfo
        self.workInfo = workInfo
        self.eduInfo = eduInfo
    def __str__(self):
        return self.baseInfo.__str__() + self.workInfo.__str__() + self.eduInfo.__str__()


# my resume
eduInfo = EduInfo()
eduInfo.addEdu('焦作大学','2009-9-1', '2012-6-1', '大专')
eduInfo.addEdu('西南大学', '2016-9-1','2019-1-13', '本科')
workInfo = WorkInfo()
workInfo.addWork('tencent', '2013-10-11', '2015-11-5', 'game dev', 'develop mobile phone games')
workInfo.addWork('alibaba', '2015-12-11', '2019-7-5', 'game dev', 'develop mobile phone games')

myResume = PersonalResume(BaseInfo('Sky', '30', '18103101265', '110256123456539885', '爱生活爱编程'), workInfo, eduInfo)
print(myResume)