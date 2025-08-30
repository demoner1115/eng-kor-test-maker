import json
import random

FILENAME = "words.json"

with open(FILENAME, "r", encoding="utf-8") as f:
    wordbook = json.load(f)

while True:
    # (영어, 한국어) 한 쌍 뽑기
    eng, kor = random.choice(list(wordbook.items()))

    # 0: 영어→한국어, 1: 한국어→영어
    choice = random.randint(0, 1)

    if choice == 0:  # 영어 → 한국어
        answer = input(f"❓ '{eng}' 의 뜻은? (그만하려면 q) ")
        if answer.lower() == "q":
            break
        if answer == kor:
            print("🎉 정답!")
        else:
            print(f"😅 오답! 정답은 '{kor}'")

    else:  # 한국어 → 영어
        answer = input(f"❓ '{kor}' 를 영어로 하면? (그만하려면 q) ")
        if answer.lower() == "q":
            break
        if answer == eng:
            print("🎉 정답!")
        else:
            print(f"😅 오답! 정답은 '{eng}'")
