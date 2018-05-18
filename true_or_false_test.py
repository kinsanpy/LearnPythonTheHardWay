#一个真值表记忆测试题程序
#真值表有2列，第一列：题目，第二列：答案，还有题目序号
#随机显示所有题目中的一道题，用户输入答案后，判断正确性
#每次测试出题10道，完成后统计得分


import random

score = 0
#题库：
table = {"1":{"not False":"True"},
        "2":{"not True":"False"},
        "3":{"True or False":"True"},
        "4":{"True or True":"True"},
        "5":{"False or True":"True"},
        "6":{"False or False":"False"},
        "7":{"True and False":"False"},
        "8":{"True and True":"True"},
        "9":{"False and True":"False"},
        "10":{"False and False":"False"},
        "11":{"not(True or False)":"False"},
        "12":{"not(True or True)":"False"},
        "13":{"not(False or True)":"False"},
        "14":{"not(False or False)":"True"},
        "15":{"not(True and False)":"True"},
        "16":{"not(True and True)":"False"},
        "17":{"not(False and True)":"True"},
        "18":{"not(False and False)":"True"},
        "19":{"1 != 0":"True"},
        "20":{"1 != 1":"False"},
        "21":{"0 != 1":"True"},
        "22":{"0 != 0":"False"},
        "23":{"1 == 0":"False"},
        "24":{"1 == 1":"True"},
        "25":{"0 == 1":"False"},
        "26":{"0 == 0":"True"}}
while True:
    #随机一个int，以获取相应题目，并转成str
    rNum = str(random.randint(1,26))
    #使用随机数取得题号，然后获取题目（也就是嵌套里的key），取出的类型是dict，需转换成str
    get_Raw_Quest = str(table[rNum].keys())
    #截取题目内容
    get_real_Quest = get_Raw_Quest[12:-3]
    #打印题目内容
    print ("第"+rNum+"题:"+get_real_Quest)
    #获取序号对应题目的答案，类型是str
    c_answer = table[rNum][get_real_Quest]
    #用户输入
    u_answer = input("请输入答案：")

    if u_answer == c_answer:
    	print ("回答正确，加1分!")
    	score += 1
    	print ("当前得分：%d"%score)
    else:
        print ("回答错误，扣1分，正确答案是： %s"% c_answer)
        score -= 1
        print ("当前得分：%d"%score)
