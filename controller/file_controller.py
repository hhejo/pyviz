import csv


def load_csv(file_name):
  mbti_counts = {}
  with open(file_name, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    mbti_counts = {rows[0]: int(rows[1]) for rows in reader}
  return mbti_counts


def save_csv(file_name, mbti_counts):
  with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['MBTI', 'Count'])
    for mbti, count in mbti_counts.items():
      writer.writerow([mbti, count])
    print(f'{file_name} 저장 완료')


def save_txt(file_name, data_list):
  with open(file_name, mode='w', encoding='utf-8') as file:
    for i, data in enumerate(data_list):
      file.write(f'  {i + 1}\n{data}\n')
    print(f'{file_name} 저장 완료')
