def countString(str1,str2,m ,n):
    if((m==0 and n==0)or n==0):
        return 1
    if(m==0):
        return 0
    if(str1[m-1] ==str2[n-1]):
        return (countString(str1,str2,m-1,n-1)+countString(str1,str2,m-1,n))
    else:
        return countString(str1, str2,m-1,n)

str1="goingtogotogoa"
str2="go"
print(countString(str1,str2,len(str1),len(str2)))
