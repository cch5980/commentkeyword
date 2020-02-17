from konlpy.tag import Komoran
komoran = Komoran()

# sentense2 = "책상이 넓어서 공부하긴 좋습니다.여기 개쩔어요.여기 냄새나요.맛이 없어요. 시끄럽다. 눈치 준다. 자리가 좁다. 마감 한시간전에 청소 한다. 서비스가 안좋다. 시발 여기 개좆같다.깨끗하고 분위기가 편안한데 음료는 맛없어요. 근데 좌석이 너무 편안해서 좋았어욤. 다음에 또 올게요!"
# sentense2 = "적당함"
sentense2 = "냄새나고 별로에요"

sentense = ''
for i in range(len(sentense2)):
    if sentense2[i] == '.' or sentense2[i] == '?' or sentense2[i] == '!' or sentense2[i] == ',' or sentense2[i] == '(' or sentense2[i] == ')' or sentense2[i] == '-':
        sentense += ' '
    else:
        sentense += sentense2[i]
# print(sentense)

analysis = []
analysis = komoran.pos(sentense)
print(analysis)


str = ''
word_dict = {}
for i in analysis:
    if ('NN') in i[1]:
        str = i[0]
    elif ('VA') in i[1]:
        str += (i[0] + "음")       
        if str in word_dict:
            word_dict[str] += 1
        else:
            word_dict[str] = 1
        str = ''
    elif ('NA') in i[1]:
        str = i[0]
        if str in word_dict:
            word_dict[str] += 1
        else:
            word_dict[str] = 1

print(word_dict)