def get_korean(text):
  if '엔프제' in text:
    return 'ENFJ'
  elif '엔프피' in text:
    return 'ENFP'
  elif '엔티제' in text:
    return 'ENTJ'
  elif '엔팁' in text:
    return 'ENTP'
  elif '엣프제' in text:
    return 'ESFJ'
  elif '엣프피' in text:
    return 'ESFP'
  elif '엣티제' in text:
    return 'ESTJ'
  elif '엣팁' in text:
    return 'ESTP'
  # 
  elif '인프제' in text:
    return 'INFJ'
  elif '인프피' in text or '씹프피' in text:
    return 'INFP'
  elif '인티제' in text:
    return 'INTJ'
  elif '인팁' in text:
    return 'INTP'
  elif '잇프제' in text:
    return 'ISFJ'
  elif '잇프피' in text:
    return 'ISFP'
  elif '잇티제' in text:
    return 'ISTJ'
  elif '잇팁' in text:
    return 'ISTP'
  else:
    return ''


def get_mbti_counts(titles, contents):
  mbtis = []
  for a in 'EI':
    for b in 'NS':
      for c in 'FT':
        for d in 'JP':
          mbtis.append(a + b + c + d)
  mbti_counts = {key: 0 for key in mbtis}
  print('제목에서 MBTI 추출 시작')
  for title in titles:
    for mbti in mbtis:
      if mbti in title:
        mbti_counts[mbti] += 1
    result = get_korean(title)
    if result:
      mbti_counts[result] += 1
  print('제목에서 MBTI 추출 완료')
  print('내용에서 MBTI 추출 시작')
  for content in contents:
    for mbti in mbtis:
      if mbti in content:
        mbti_counts[mbti] += 1
    result = get_korean(content)
    if result:
      mbti_counts[result] += 1
  print('내용에서 MBTI 추출 완료')
  return mbti_counts
