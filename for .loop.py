# list=["a:10","b:20","c:10"]
# dict={}
# for i in range (3):
#     dict[i]=list[i]
# print(dict)



# 1,1,2,3,5,8,13,21

# 1,1,2,4,8,16,32

# # 1,3,7,13,21

# # i=0
# b=int(input("enter no:-"))
# i=0
# a=1
# c=0
# while i<b:
#     print(a)
#     if a==1:
        

# a= int(input("enter table:-"))
# # i=0
# y=0
# x=int(input("enter any number:-"))
# while y<=10:
#     print(x,"*",y,"=",x*y)
#     y=y+1
    


    # if x==rev:
# que_list=["Who Invented computer","Who invented Internet","When was python developed","what is the fullform of www."]
# opt_list=[["Vint cerf","Mark Jukerberg","Charls babbage","Robert Vintage"],["Vint cerf","vinton cerf", "Guido","John babbage"],["21 feb","20 feb","20 march","19 jan"],["world web wide","world wide web","world web webside","world wide webside"]]
# ans_list=[3,1,2,2]
# fifty_list=[["Charls babbage","Robert Vintage"],["vint cef","guido"],["21 feb","20 feb"],["world web wide","world wide web"]]
# sol_list=[1,1,2,2]  
# lifelinecount = 0
# def lifeline(index):  
#     global lifelinecount
#     j=0 
#     if(lifelinecount==0): 
#         while j<len(fifty_list[index]):
#             print(j+1,fifty_list[index][j])
#             j=j+1
#         user_ans = int(input('.....'))
#         lifelinecount+=1
#         if user_ans==sol_list[index]:
#             return True
#         else:
#             return False
#     else:
#         print('you Already used 5050')
#         return "no"
# def option(index):
#     j=0
#     while j<len(opt_list[index]):
#         print(j+1,opt_list[index][j])
#         j=j+1
#     user_ans = int(input('.....'))
#     if user_ans==ans_list[index]:
#         return True
#     if user_ans == 5050:
#         return(lifeline(index))
#     else:
#         return False
# def que():
#     index=0
#     while index<len(que_list):
#         print("Q.",index+1,que_list[index],"?")
#         result=option(index)
#         if result == "no":
#             index-=1
#         elif result==True:
#             print("Congractualtion")
#         else:
#             print("you Losse !")
#             break 
#         index+=1
# def main():
#     que()
# main()
    





que_list=["How many are girls in Sarjapur Campus?","What is Capital of India?","Name of Pink city name?","Who is  Dico in Sarjapur Campus?"]
opt_list=[[123,134,568,100],["Delhi","Bangalore","Nanital","Odisa"],["Aagra","Chamoli","Panjab","Jaypur"],["Himani","Kajal","Harman","Gudiya"]]
ans_list=[2,1,4,1]
cash=0
def option(index):
    j=0
    while j<len(opt_list[index]):
        print(j+1,opt_list[index][j])
        j=j+1
    user_ans = int(input('.....'))
    if user_ans==ans_list[index]:
        return True
    else:
        return False
def que():
    global cash
    index=0
    while index<len(que_list):
        print("Q.",index+1,que_list[index],"?")
        result=option(index)
        if result==True:
            cash+=10000
            print("Congractualtion \n ","u won - ",cash)
        else:
            print("you Losse ! \n","u won - ",cash)
            break 
        index+=1
def main():
    que()
main()





