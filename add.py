import json
import os

FILENAME = "words.json"


def load_words():
    """기존 단어장 불러오기"""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_words(wordbook):
    """단어장 저장하기"""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(wordbook, f, ensure_ascii=False, indent=2)


def main():
    wordbook = load_words()

    eng = input("영어 단어 입력: ").strip()
    kor = input("뜻 입력: ").strip()

    if eng in wordbook:
        print(f"⚠️ 이미 있는 단어야! 뜻을 '{wordbook[eng]}' → '{kor}' 로 업데이트할게.")
    else:
        print(f"✅ 새로운 단어 '{eng}' 추가 완료!")

    wordbook[eng] = kor
    save_words(wordbook)


if __name__ == "__main__":
    main()
