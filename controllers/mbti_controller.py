def get_mbti_type_from_korean(text):
    mbti_korean_types_e = {'엔프제': 'ENFJ', '엔프피': 'ENFP', '엔티제': 'ENTJ', '엔팁': 'ENTP', '엣프제': 'ESFJ', '엣프피': 'ESFP', '엣티제': 'ESTJ', '엣팁': 'ESTP'}
    mbti_korean_types_i = {'인프제': 'INFJ', '인프피': 'INFP', '인티제': 'INTJ', '인팁': 'INTP', '잇프제': 'ISFJ', '잇프피': 'ISFP', '잇티제': 'ISTJ', '잇팁': 'ISTP', '씹프피': 'INFP'}

    for ko, en in mbti_korean_types_e.items():
        if ko in text:
            return en, text.count(ko)

    for ko, en in mbti_korean_types_i.items():
        if ko in text:
            return en, text.count(ko)

    return '', 0


def get_mbti_counts(titles, contents):
    mbti_types = []  # MBTI 타입 16개 생성

    for a in 'EI':
        for b in 'NS':
            for c in 'FT':
                for d in 'JP':
                    mbti_types.append(a + b + c + d)

    mbti_counts = {key: 0 for key in mbti_types}  # {MBTI_타입: 개수}

    for title in titles:
        for mbti_type in mbti_types:
            if mbti_type in title:
                mbti_counts[mbti_type] += title.count(mbti_type)
        mbti_type_from_korean, counts = get_mbti_type_from_korean(title)
        if mbti_type_from_korean:
            mbti_counts[mbti_type_from_korean] += counts

    for content in contents:
        for mbti_type in mbti_types:
            if mbti_type in content:
                mbti_counts[mbti_type] += content.count(mbti_type)
        mbti_type_from_korean, counts = get_mbti_type_from_korean(content)
        if mbti_type_from_korean:
            mbti_counts[mbti_type_from_korean] += counts

    return mbti_counts
