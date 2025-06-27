# word_frequency_counter.py
import re
from collections import Counter

def count_word_frequency(filepath):
    """
    텍스트 파일 내의 단어 빈도수를 계산하여 반환합니다.
    """
    word_counts = Counter()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            # 모든 문자를 소문자로 변환하고, 알파벳과 숫자만 남깁니다.
            # (re.sub는 정규표현식으로 문자열을 대체합니다. ^a-z0-9는 알파벳과 숫자가 아닌 것을 의미)
            cleaned_text = re.sub(r'[^a-z0-9\s]', '', text.lower())
            words = cleaned_text.split() # 공백 기준으로 단어 분리

            for word in words:
                if word: # 빈 문자열이 아닌 경우만 카운트
                    word_counts[word] += 1
        return word_counts
    except FileNotFoundError:
        print(f"오류: '{filepath}' 파일을 찾을 수 없습니다.")
        return None
    except Exception as e:
        print(f"파일을 읽는 중 오류 발생: {e}")
        return None

def main():
    print("--- 텍스트 파일 단어 빈도수 계산기 ---")
    file_path = input("분석할 텍스트 파일 경로를 입력하세요 (예: sample.txt): ")

    word_frequencies = count_word_frequency(file_path)

    if word_frequencies:
        print(f"\n--- '{file_path}' 파일의 단어 빈도수 (상위 10개) ---")
        for word, count in word_frequencies.most_common(10): # 가장 많이 나타난 상위 10개
            print(f"'{word}': {count}번")
    else:
        print("단어 빈도수를 계산할 수 없습니다.")

if __name__ == "__main__":
    # 테스트를 위한 샘플 파일 생성 (없으면 오류)
    sample_content = """
    Python is an interpreted, high-level, general-purpose programming language.
    Python's design philosophy emphasizes code readability with its notable use of significant indentation.
    Python is dynamically typed and garbage-collected. It supports multiple programming paradigms,
    including structured (particularly procedural), object-oriented, and functional programming.
    """
    try:
        with open("sample.txt", "w", encoding="utf-8") as f:
            f.write(sample_content.strip())
        print("샘플 파일 'sample.txt'가 생성되었습니다.")
    except Exception as e:
        print(f"샘플 파일 생성 실패: {e}")

    main()
