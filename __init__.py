#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu May  6 19:41:49 2021

title:to compute division between two integers
"""

__author__='z'

def nextDigits(den):
    return lambda num:divmod(10*num,den) 

def isRepeat(ans,num,digitDict,numDict):
    a=False
    for i in digitDict:
        if ans==digitDict[i] and num==numDict[i]:
            a=True
            break
    if a:
        return (a,i)
    else:
        return (a,)

def dec(num,den,digits_limit=None):
    if not isinstance(num,int) or not isinstance(den,int):
        pass #return wrong
    else:
        nextD=nextDigits(den)
        answer=''
        ans=digits=0
        digitDict={}
        numDict={}
        a=(num!=0 and digits<digits_limit) if digits_limit else (num!=0)
        while a:
            ans,num=nextD(num)
            r=isRepeat(ans,num,digitDict,numDict)
            if r[0]:
                answer=answer[:r[1]]+'('+answer[r[1]:]+')'
                break
            else:
                digitDict[digits]=ans
                numDict[digits]=num
                answer+=str(ans)
            digits+=1
            a=(num!=0 and digits<digits_limit) if digits_limit else (num!=0)
        return answer

def div_int(num,den,digits_limit=None):
    if not isinstance(num,int) or not isinstance(den,int):
        pass #return wrong
    
    else:
        ans=str(num//den)
        if digits_limit==0:
            return ans
        else:
            return ans+'.'+dec(num%den,den,digits_limit=digits_limit)


def div(num,den,digits_limit=None):
    def decDigits(s):
        a=0
        for i in range(len(s)):
            if s[i]=='.':
                a=i
                break
        return len(s)-a
    
    def rmDot(s):
        sList=[i for i in s if i != '.']
        s_=''
        for i in sList:
            s_+=i
        return s_
    
    def transInt(num,den):
        s_num,s_den=str(num),str(den)
        s_intNum,s_intDen=rmDot(s_num),rmDot(s_den)
        dD_NumDen=decDigits(s_num)-decDigits(s_den)
        if dD_NumDen>=0:
            s_intDen+='0'*dD_NumDen
        elif dD_NumDen<0:
            s_intNum+='0'*(-dD_NumDen)
        return (int(s_intNum),int(s_intDen))
    
    return div_int(*transInt(num,den),digits_limit=None)

if __name__=='__main__':
    print(div(1,7))