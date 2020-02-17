# 카카오맵 장소 정보 파싱
def kakaoPlaceInfo(placeId):
    url = "https://place.map.kakao.com/main/v/"+str(placeId)
    response = requests.get(url)
    kakao_place_data = response.json()
    placeName = kakao_place_data["basicInfo"]["placenamefull"]  # 장소 이름
    placeAddress = kakao_place_data["basicInfo"]["address"]["region"]["fullname"] + kakao_place_data["basicInfo"]["address"]["newaddr"]["newaddrfull"]  # 장소 주소
    # 장소 번호
    if "phonenum" in kakao_place_data["basicInfo"].keys():
        placePhonenum = kakao_place_data["basicInfo"]["phonenum"]   
    else:
        placePhonenum = "062-123-4567"
    
    # 장소 이미지
    if "mainphotourl" in kakao_place_data["basicInfo"].keys():
        placeImg = kakao_place_data["basicInfo"]["mainphotourl"]   
    else:
        placeImg = "이미지x"    # 대체 이미지 필요
    
    # 장소 소개글
    if "introduction" in kakao_place_data["basicInfo"].keys():
        placeIntroduction = kakao_place_data["basicInfo"]["introduction"]   
    else:
        placeIntroduction = placeName
    
    # 장소 영업시간
    if "openHour" in kakao_place_data["basicInfo"].keys():
        placeOpenHour = kakao_place_data["basicInfo"]["openHour"]["periodList"][0]["timeList"][0]["timeSE"]
    else:
        placeOpenHour = "00:00 ~ 24:00"

    # 장소 카테고리
    placeCategoryCode = int(kakao_place_data["basicInfo"]["cateid"])
    # 18427: 도서관(교육,학문) / 23758: 스터디카페(음식점) / 174: 커피음식점(음식점), 86: 카페(음식점)
    if placeCategoryCode <= 10000:
        placeCategory = "카페"
    elif placeCategoryCode <= 20000:
        placeCategory = "도서관"
    else:
        placeCategory = "스터디카페"

    placeData = {
        'placeName' : placeName,
        'placeImg' : placeImg,
        'placePhonenum' : placePhonenum,
        'placeIntroduction' : placeIntroduction,
        'placeAddress' : placeAddress,
        'placeOpenHour' : placeOpenHour,
        'placeCategory' : placeCategory,
    }
    return placeData