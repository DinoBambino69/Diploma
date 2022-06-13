import csv
import random


def export_to_csv(filename, data):
    with open(f'files/{filename}.csv', 'w', encoding='utf-8') as csvfile:
        writer_csv = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)

        for i, k in data.__dict__.items():
            if i == '_state' or i == 'id':
                continue
            else:
                writer_csv.writerow([i,k])

def ai():
    predictCount = random.randint(0, 20)
    chanse = 100 - (predictCount / 20) * 100
    result = 'Итоговый результат = ' + str(predictCount) + ' баллов \n Шанс отчисления = ' + str(int(chanse)) + '%'
    return result
