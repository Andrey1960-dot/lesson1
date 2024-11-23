from pprint import pprint
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
   n = 0
   strings_positions ={}
   for i in info:
       file = open(file_name, 'a', encoding='utf-8')
       tell = (file.tell())
       n += 1
       file.write(f'{i}\n')
       file.close()
       strings_positions.update({(n, tell):i})
       return strings_positions

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)