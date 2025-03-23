import re

def convert_to_pawn_format(text):
    # Убираем CreateObject и скобочки
    text = re.sub(r'CreateObject\((.*?)\);', r'\1', text)
    # Убираем все запятые, если они есть
    text = text.replace(',', '')
    # Вернем отформатированный текст
    return text

# Чтение файла и обработка строк
def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            # Преобразуем строку и записываем в файл
            formatted_line = convert_to_pawn_format(line)
            outfile.write(formatted_line + '\n')

# Пример использования
input_file = 'objects.txt'
output_file = 'result.txt'
process_file(input_file, output_file)

print(f'Обработка завершена. Результат записан в {output_file}')
