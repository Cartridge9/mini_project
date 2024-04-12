import random as r
line = "-------------------------------------------------------------------------------------------------"
emp = """





"""
bm = [["참치마요삼각김밥", "계란볶음밥", "카레", "소고기 주먹밥", "멸치 주먹밥", "소고기죽", "동지팥죽", "달걀죽", "감자조림", "닭죽"], # 밥
      ["콩나물국", "계란찜", "떡만두국", "떡국", "참치김치찌개", "황태국", "김치어묵탕", "오징어 뭇국", "순두부명란국", "새우완탕", "오이냉국", "미소된장국"], # 국
      ["바나나", "사과", "블루베리", "메론", "딸기", "복숭아"], # 과일
      ["에그토스트", "샌드위치(과일넣은)", "햄치즈토스트", "양배추 토스트"], # 토스트
      ["그래놀라", "그릭 요구르트", "시리얼", "브로콜리 감자스프", "단호박스프", "양송이감자스프", "그린주스", "퍼플주스", "블랙주스", "누룽지"]] # 간편식

ldm = [["짜장면", "잔치국수", "바지락 칼국수", "닭칼국수", "짬뽕", "비빔국수", "어묵우동", "월남쌀국수", "비빔당면", "열무비빔국수"], # 면
      ["뚝배기 김치날치알밥", "장어덮밥", "유뷰초밥", "소고기밥", "파인애플 볶음밥",  "제육덮밥", "초밥", "대패삼겹살 덮밥",
       "참치마요볶음밥", "깻잎쌈밥", "짜장밥", "스팸마요덮밥", "돈가스덮밥", "만두덮밥"], # 밥
      ["된장찌개", "순두부찌개", "순대국", "설렁탕", "부대찌개", "뼈다귀 해장국", "시래기 된장국",
       "미소된장국", "소고기미역국", "동태찌개", "감자탕", "돼지고기 김치찌개", ], # 국
      ["돈까스", "김밥+라면", "떡튀순", "치즈돈까스", "충무김밥"], # 분식
      ["치킨", "피자", "햄버거"], # 패스트푸드
      ["까르보나라", "토마토 파스타", "로제파스타",  "함박스테이크", "알리오올리오 파스타", "쫄면"], # 양식
      ["삼겹살", "찜닭", "곱창", "막창", "대창", "양고기", "소고기", "닭볶음탕", "고등어조림",
       "오리고기", "오징어볶음", "떡갈비", "대패삼겹살", "회", "낙지볶음"]] # 고기류
print(emp)
print(line)
print("메뉴를 고르시려면 1 , 메뉴를 추가하시려면 2, 메뉴를 삭제하시려면 3, 기본 메뉴를 확인하려면 4를 입력해 주세요 . ")
print(line)
f = int(input())

if f == 1:
    print(emp)
    print(line)
    print("아침, 점심, 저녁 중 무슨 메뉴를 추천해 드릴까요 ? ")
    print(line)
    w = input()
    if w == "아침":
        print(emp)
        print(line)
        print("아침 메뉴에는 밥, 국, 과일, 토스트, 간편식이 있습니다 ! \n무엇을 추천해드릴까요 ? ")
        print(line)
        wbm = input()
        if wbm == "밥": print(emp); print(line); print(r.choice(bm[0]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "국": print(emp); print(line); print(r.choice(bm[1]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "과일": print(emp); print(line); print(r.choice(bm[2]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "토스트": print(emp); print(line); print(r.choice(bm[3]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "간편식" or "간편": print(emp); print(line); print(r.choice(bm[4]), "을(를) 추천드려요 ! " ); print(line)
    elif w == "점심":
        print(emp)
        print(line)
        print("점심 메뉴에는 면, 밥, 국, 분식, 패스트푸드, 양식, 고기류가 있습니다 ! \n무엇을 추천해드릴까요 ? ")
        print(line)
        wlm = input()
        if wlm == "면": print(emp); print(line); print(r.choice(ldm[0]), "을(를) 추천드려요 ! "); print(line)
        elif wlm == "밥": print(emp); print(line); print(r.choice(ldm[1]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "국": print(emp); print(line); print(r.choice(ldm[2]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "분식": print(emp); print(line); print(r.choice(ldm[3]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "패스트푸드": print(emp); print(line); print(r.choice(ldm[4]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "양식": print(emp); print(line); print(r.choice(ldm[5]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "고기류" or "고기": print(emp); print(line); print(r.choice(ldm[6]), "을(를) 추천드려요 ! " ); print(line)
    elif w == "저녁":
        print(emp)
        print(line)
        print("저녁 메뉴에는 면, 밥, 국, 분식, 패스트푸드, 양식, 고기류가 있습니다 ! \n무엇을 추천해드릴까요 ? ")
        print(line)
        wdm = input()
        if wdm == "면": print(emp); print(line); print(r.choice(ldm[0]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "밥": print(emp); print(line); print(r.choice(ldm[1]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "국": print(emp); print(line); print(r.choice(ldm[2]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "분식": print(emp); print(line); print(r.choice(ldm[3]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "패스트푸드": print(emp); print(line); print(r.choice(ldm[4]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "양식": print(emp); print(line); print(r.choice(ldm[5]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "고기류" or "고기": print(emp); print(line); print(r.choice(ldm[6]), "을(를) 추천드려요 ! "); print(line)
    else:
        print(emp)
        print(line)
        print("올바른 값을 입력해주세요 . ")
        print(line)

elif f == 2:
    print(emp)
    print(line)
    print("아침, 점심, 저녁 중 어디에 메뉴를 추가할까요 ? ")
    print(line)
    p = input()
    if p == "아침":
        print(emp)
        print(line)
        print(f"밥 : {bm[0]}")
        print(f"국 : {bm[1]}")
        print(f"과일 : {bm[2]}")
        print(f"토스트 : {bm[3]}")
        print(f"간편식 : {bm[4]}")        
        print(line)
        print("아침 메뉴에는 밥, 국, 과일, 토스트, 간편식이 있습니다 ! \n어디에 추가할까요 ? ")
        print(line)
        wm = input()
        if wm == "밥": wm = 0
        elif wm == "국": wm = 1
        elif wm == "과일": wm = 2
        elif wm == "토스트": wm = 3
        elif wm == "간편식": wm = 4
    elif p == "점심":
        print(emp)
        print(line)
        print(f"면 : {ldm[0]}")
        print(f"밥 : {ldm[1]}")
        print(f"국 : {ldm[2]}")
        print(f"분식 : {ldm[3]}")
        print(f"패스트푸드 : {ldm[4]}")
        print(f"양식 : {ldm[5]}")
        print(f"고기류 : {ldm[6]}")
        print(line)
        print("점심 메뉴에는 면, 밥, 국, 분식, 패스트푸드, 양식, 고기류가 있습니다 ! \n어디에 추가할까요 ? ")
        print(line)
        wm = input()
        if wm == "면": wm = 0
        elif wm == "밥": wm = 1
        elif wm == "국": wm = 2
        elif wm == "분식": wm = 3
        elif wm == "패스트푸드": wm = 4
        elif wm == "양식": wm = 5
        elif wm == "고기류": wm = 6
    elif p == "저녁":
        print(emp)
        print(line)
        print(f"면 : {ldm[0]}")
        print(f"밥 : {ldm[1]}")
        print(f"국 : {ldm[2]}")
        print(f"분식 : {ldm[3]}")
        print(f"패스트푸드 : {ldm[4]}")
        print(f"양식 : {ldm[5]}")
        print(f"고기류 : {ldm[6]}")
        print(line)
        print("저녁 메뉴에는 면, 밥, 국, 분식, 패스트푸드, 양식, 고기류가 있습니다 ! \n어디에 추가할까요 ? ")
        print(line)
        wm = input()
        if wm == "면": wm = 0
        elif wm == "밥": wm = 1
        elif wm == "국": wm = 2
        elif wm == "분식": wm = 3
        elif wm == "패스트푸드": wm = 4
        elif wm == "양식": wm = 5
        elif wm == "고기류": wm = 6
    print(emp)
    print(line)
    print("추가할 메뉴를 입력해주세요 . ")
    print(line)
    me = input()
    if p == "아침":
        if me in bm[wm]: print(emp); print(line); print("이미 있는 메뉴입니다 ! "); print(line)
        else: bm[wm].append(me); print(emp); print(line); print(f"{me} 이(가) {p} 메뉴에 추가되었습니다 ! "); print(line)
    elif p == "점심":
        if me in ldm[wm]: print(emp); print(line); print("이미 있는 메뉴입니다 ! "); print(line)
        else: ldm[wm].append(me); print(emp); print(line); print(f"{me} 이(가) {p} 메뉴 에 추가되었습니다 ! "); print(line)
    elif p == "저녁":
        if me in ldm[wm]: print(line); print(emp); print("이미 있는 메뉴입니다 ! "); print(line)
        else: ldm[wm].append(me); print(emp); print(f"{me} 이(가) {p} 메뉴 에 추가되었습니다 ! ")
    else: print(line); print("올바른 값을 입력해주세요 . "); print(line)
# 메뉴 추가 후 메뉴 추천
    print(emp)
    print(line)
    print("아침, 점심, 저녁 중 무슨 메뉴를 추천해 드릴까요 ? ")
    print(line)
    w = input()
    if w == "아침":
        print(emp)
        print(line)
        print("아침 메뉴에는 밥, 국, 과일, 토스트, 간편식이 있습니다 ! \n무엇을 추천해드릴까요 ? ")
        print(line)
        wbm = input()
        if wbm == "밥": print(emp); print(line); print(r.choice(bm[0]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "국": print(emp); print(line); print(r.choice(bm[1]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "과일": print(emp); print(line); print(r.choice(bm[2]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "토스트": print(emp); print(line); print(r.choice(bm[3]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "간편식" or "간편": print(emp); print(line); print(r.choice(bm[4]), "을(를) 추천드려요 ! " ); print(line)
    elif w == "점심":
        print(emp)
        print(line)
        print("점심 메뉴에는 면, 밥, 국, 분식, 패스트푸드, 양식, 고기류가 있습니다 ! \n무엇을 추천해드릴까요 ? ")
        print(line)
        wlm = input()
        if wlm == "면": print(emp); print(line); print(r.choice(ldm[0]), "을(를) 추천드려요 ! "); print(line)
        elif wlm == "밥": print(emp); print(line); print(r.choice(ldm[1]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "국": print(emp); print(line); print(r.choice(ldm[2]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "분식": print(emp); print(line); print(r.choice(ldm[3]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "패스트푸드": print(emp); print(line); print(r.choice(ldm[4]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "양식": print(emp); print(line); print(r.choice(ldm[5]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "고기류" or "고기": print(emp); print(line); print(r.choice(ldm[6]), "을(를) 추천드려요 ! " ); print(line)
    elif w == "저녁":
        print(emp)
        print(line)
        print("저녁 메뉴에는 면, 밥, 국, 분식, 패스트푸드, 양식, 고기류가 있습니다 ! \n무엇을 추천해드릴까요 ? ")
        print(line)
        wdm = input()
        if wdm == "면": print(emp); print(line); print(r.choice(ldm[0]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "밥": print(emp); print(line); print(r.choice(ldm[1]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "국": print(emp); print(line); print(r.choice(ldm[2]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "분식": print(emp); print(line); print(r.choice(ldm[3]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "패스트푸드": print(emp); print(line); print(r.choice(ldm[4]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "양식": print(emp); print(line); print(r.choice(ldm[5]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "고기류" or "고기": print(emp); print(line); print(r.choice(ldm[6]), "을(를) 추천드려요 ! "); print(line)
    else:
        print(emp)
        print(line)
        print("올바른 값을 입력해주세요 . ")
        print(line)

elif f == 3:
    print(emp)
    print(line)
    print("아침, 점심, 저녁 중 무슨 메뉴를 삭제하시겠어요 ? ")
    print(line)
    d = input()
    if d == "아침":
        print(line)
        print(f"밥 : {bm[0]}")
        print(f"국 : {bm[1]}")
        print(f"과일 : {bm[2]}")
        print(f"토스트 : {bm[3]}")
        print(f"간편식 : {bm[4]}")
        print(line)
        print("무슨 종류의 어떤 메뉴를 삭제하시겠습니다 ? ( 종류 메뉴 로 입력 )")
        print(line)
        dt, dw = input().split()
        if dt == "밥": dt = 0
        elif dt == "국": dt = 1
        elif dt == "과일": dt = 2
        elif dt == "토스트": dt = 3
        elif dt == "간편식": dt = 4
        else: print("해당 메뉴는 없는 메뉴입니다 .. ")
        if dw in bm[dt]: del(bm[dt][bm[dt].index(dw)]); print(line); print(f"{dw} 메뉴가 삭제되었습니다 ! "); print(line)
        else: print(line); print("해당 메뉴는 없는 메뉴입니다 .. "); print(line)
    elif d == "점심" or "저녁":
        print(line)
        print(f"면 : {ldm[0]}")
        print(f"밥 : {ldm[1]}")
        print(f"국 : {ldm[2]}")
        print(f"분식 : {ldm[3]}")
        print(f"패스트푸드 : {ldm[4]}")
        print(f"양식 : {ldm[5]}")
        print(f"고기류 : {ldm[6]}")
        print(line)
        print("무슨 종류의 어떤 메뉴를 삭제하시겠습니다 ? ( 종류 메뉴 로 입력 )")
        dt, dw = map(str, input().split())
        if dt == "면": dt = 0
        elif dt == "밥": dt = 1
        elif dt == "국": dt = 2
        elif dt == "분식": dt = 3
        elif dt == "패스트푸드": dt = 4
        elif dt == "양식": dt = 5
        elif dt == "고기류": dt = 6
        else: print("해당 메뉴는 없는 메뉴입니다 .. ")
        if dw in ldm[dt]: del(ldm[dt][ldm[dt].index(dw)]); print(line); print(f"{dw} 메뉴가 삭제되었습니다 ! "); print(line)
        else: print(line); print("해당 메뉴는 없는 메뉴입니다 .. "); print(line)
# 메뉴 삭제 후 메뉴 추천    
    print(emp)
    print(line)
    print("아침, 점심, 저녁 중 무슨 메뉴를 추천해 드릴까요 ? ")
    print(line)
    w = input()
    if w == "아침":
        print(emp)
        print(line)
        print("아침 메뉴에는 밥, 국, 과일, 토스트, 간편식이 있습니다 ! \n무엇을 추천해드릴까요 ? ")
        print(line)
        wbm = input()
        if wbm == "밥": print(emp); print(line); print(r.choice(bm[0]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "국": print(emp); print(line); print(r.choice(bm[1]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "과일": print(emp); print(line); print(r.choice(bm[2]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "토스트": print(emp); print(line); print(r.choice(bm[3]), "을(를) 추천드려요 ! " ); print(line)
        elif wbm == "간편식" or "간편": print(emp); print(line); print(r.choice(bm[4]), "을(를) 추천드려요 ! " ); print(line)
    elif w == "점심":
        print(emp)
        print(line)
        print("점심 메뉴에는 면, 밥, 국, 분식, 패스트푸드, 양식, 고기류가 있습니다 ! \n무엇을 추천해드릴까요 ? ")
        print(line)
        wlm = input()
        if wlm == "면": print(emp); print(line); print(r.choice(ldm[0]), "을(를) 추천드려요 ! "); print(line)
        elif wlm == "밥": print(emp); print(line); print(r.choice(ldm[1]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "국": print(emp); print(line); print(r.choice(ldm[2]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "분식": print(emp); print(line); print(r.choice(ldm[3]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "패스트푸드": print(emp); print(line); print(r.choice(ldm[4]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "양식": print(emp); print(line); print(r.choice(ldm[5]), "을(를) 추천드려요 ! " ); print(line)
        elif wlm == "고기류" or "고기": print(emp); print(line); print(r.choice(ldm[6]), "을(를) 추천드려요 ! " ); print(line)
    elif w == "저녁":
        print(emp)
        print(line)
        print("저녁 메뉴에는 면, 밥, 국, 분식, 패스트푸드, 양식, 고기류가 있습니다 ! \n무엇을 추천해드릴까요 ? ")
        print(line)
        wdm = input()
        if wdm == "면": print(emp); print(line); print(r.choice(ldm[0]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "밥": print(emp); print(line); print(r.choice(ldm[1]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "국": print(emp); print(line); print(r.choice(ldm[2]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "분식": print(emp); print(line); print(r.choice(ldm[3]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "패스트푸드": print(emp); print(line); print(r.choice(ldm[4]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "양식": print(emp); print(line); print(r.choice(ldm[5]), "을(를) 추천드려요 ! " ); print(line)
        elif wdm == "고기류" or "고기": print(emp); print(line); print(r.choice(ldm[6]), "을(를) 추천드려요 ! "); print(line)
    else:
        print(emp)
        print(line)
        print("올바른 값을 입력해주세요 . ")
        print(line)

elif f == 4:
    print(emp)
    print("아침" + line)
    print(f"밥 : {bm[0]}")
    print(f"국 : {bm[1]}")   
    print(f"과일 : {bm[2]}")
    print(f"토스트 : {bm[3]}")
    print(f"간편식 : {bm[4]}")
    print(line)
    print("점심 & 저녁"+line)
    print(f"면 : {ldm[0]}")
    print(f"밥 : {ldm[1]}")
    print(f"국 : {ldm[2]}")
    print(f"분식 : {ldm[3]}")
    print(f"패스트푸드 : {ldm[4]}")
    print(f"양식 : {ldm[5]}")
    print(f"고기류 : {ldm[6]}")
    print(line)

else:
    print(emp)
    print(line)
    print("올바른 숫자를 입력해주세요 . ")
    print(line)