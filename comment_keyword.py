from konlpy.tag import Komoran
komoran = Komoran()

# sentense2 = "사장님도 불친절합니다. 밝지 않다. 조명이 밝아서 좋네요. 근데 음악이 조금 시끄러워서 오랫동안 공부하기에는 좋진 않네요."
sentense2 = "책상이 넓어서 공부하긴 좋습니다.여기 개쩔어요.여기 냄새나요.맛이 없어요. 시끄럽다. 눈치 준다. 자리가 좁다. 마감 한시간전에 청소 한다. 서비스가 안좋다. 시발 여기 개좆같다.깨끗하고 분위기가 편안한데 음료는 맛없어요. 근데 좌석이 너무 편안해서 좋았어욤. 다음에 또 올게요!"

sentense = ''
for i in range(len(sentense2)):
    if sentense2[i] == '.' or sentense2[i] == '?' or sentense2[i] == '!' or sentense2[i] == ','or sentense2[i] == '(' or sentense2[i] == ')' or sentense2[i] == '-':
        sentense += ' '
    else:
        sentense += sentense2[i]
#print(sentense)

analysis = []
analysis = komoran.pos(sentense)
print(analysis)

word_dict = {}
analysis_len = len(analysis)
if analysis[0][1] == 'VA':
    temp = analysis[0][0] + '다'
    word_dict[temp] = 0
for idx in range(1, analysis_len):
    if analysis[idx][1] == 'VA':
        if analysis[idx-1][1] == 'MAG':
            temp = analysis[idx-1][0] + analysis[idx][0] + '다'
            if temp in word_dict:
                word_dict[temp] += 1
            else:
                word_dict[temp] = 0
        else:
            temp = analysis[idx][0] + '다'
            if len(temp) > 2:
                if temp in word_dict:
                    word_dict[temp] += 1
                else:
                    word_dict[temp] = 0
    elif analysis[idx][1] == 'NNG':
        if analysis[idx-1][1] == 'XPN':
            temp = analysis[idx-1][0] + analysis[idx][0]
            if temp in word_dict:
                word_dict[temp] += 1
            else:
                word_dict[temp] = 0
        else:
            temp = analysis[idx][0]
            if temp in word_dict:
                word_dict[temp] += 1
            else:
                word_dict[temp] = 0
    elif analysis[idx][1] == 'VX':
        temp = analysis[idx][0]
        if len(temp) > 1:
            if temp in word_dict:
                word_dict[temp] += 1
            else:
                word_dict[temp] = 0


tempresult = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
print(tempresult)
result = [tempresult[0][0], tempresult[1][0], tempresult[2][0]]
print(result)
