import spacy

# NLP 모델 로드
nlp = spacy.load("en_core_web_sm")

# XPath 패턴 추출 함수
def extract_pattern(xpath):
    doc = nlp(xpath)
    pattern = [token.text if not token.text == '/' else ' ' for token in doc]
    return ''.join(pattern)

# 패턴 추천 함수
def recommend_pattern(xpath):
    pattern = extract_pattern(xpath)
    return pattern

# 여러 XPath에 대한 패턴 추천 함수
def recommend_patterns(xpath_list):
    recommended_patterns = []
    for xpath in xpath_list:
        recommended_pattern = recommend_pattern(xpath)
        recommended_patterns.append(recommended_pattern)
    return recommended_patterns
