"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as file, open('referat_2.txt','w', encoding='utf-8') as outfile:
        text = "".join(i for i in file if not i.isspace())
        print(text)
        print()
        print(len(text))
        print()
        text_new = text.replace('.', '!')
        print(text_new)
        outfile.write(text_new)
if __name__ == "__main__":
    main()
