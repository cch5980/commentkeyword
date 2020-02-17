from konlpy.tag import Komoran

komoran = Komoran()
# print(komoran.morphs(u'여기 카페 가지 마세요! 드럽고 음료도 맛없고 공부하기 안 좋아요. 사장님도 불친절합니다. '))
# print(komoran.nouns(u'여기 카페 가지 마세요! 드럽고 음료도 맛없고 공부하기 안 좋아요. 사장님도 불친절합니다. '))


# print(komoran.pos(u'여기 카페 가지 마세요! 드럽고 음료도 맛없고 공부하기 안 좋아요. 사장님도 불친절합니다.'))
# print()
# print(komoran.pos(u'음식이 맛있어요'))
# print()
# print(komoran.pos(u'조명이 밝아서 좋네요. 근데 음악이 조금 시끄러워서 오랫동안 공부하기에는 좋진 않네요. '))
# print()
# print(komoran.pos(u'책상이 넓어서 공부하긴 좋습니다. '))
# print()
# print(komoran.pos(u'여기 개쩔어요. '))
# print()
# print(komoran.pos(u'여기 냄새나요. '))
# print()
# print(komoran.pos(u'맛이 없어요. '))
# print()
# print(komoran.pos(u'시끄럽다. '))
# print()
# print(komoran.pos(u'눈치 준다.'))
# print()
# print(komoran.pos(u'자리가 좁다.'))
# print()
# print(komoran.pos(u'마감 한시간전에 청소 한다.'))
# print()
# print(komoran.pos(u'서비스가 안좋다.'))
# print()
# print(komoran.pos(u'시발 여기 개좆같다'))
# print()
# print(komoran.pos(u'시발 여기 개좆같다'))
# print()
# print(komoran.pos(u'깨끗하고 분위기가 편안한데 음료는 맛없어요. 근데 좌석이 너무 편안해서 좋았어욤. 다음에 또 올게요!'))
# print()


array = []
array = komoran.pos(u'시발 여기 개좆같다 ')
tmp_str = ''
str_array = []
start_check = False
VA_check = False
for i in array:
    if "NN" in i[1]:
        tmp_str = i[0]
        start_check = True
    elif "MAG" in i[1] and start_check == True:
        tmp_str += i[0]
    elif "VA" in i[1] and start_check == True:
        tmp_str += i[0]
        VA_check = True
    elif "E" in i[1] and start_check == True:
        if(VA_check == False):
            tmp_str = ''
            start_check = False
            VA_check = False
        else:
            tmp_str += i[0]
            str_array.append(tmp_str)    
            tmp_str = ''
            start_check = False
            VA_check = False

for str in str_array:
    print(str)