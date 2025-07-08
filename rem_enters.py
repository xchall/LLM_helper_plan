import re
def process_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # заменяем все переносы строк на пробелы
        content = content.replace('\n', ' ')
        # убираем двойные пробелы
        content = re.sub(r' +', ' ', content)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)
        print("Переносы строки удалены")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

input_filename = 'input.txt'
output_filename = 'output.txt'
process_file(input_filename, output_filename)