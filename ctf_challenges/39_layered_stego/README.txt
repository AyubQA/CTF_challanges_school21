Задание 39: Многослойная стеганография

Категория: Stegano / Forensics
Сложность: Hard

Изображение layered.jpg содержит несколько скрытых сообщений, каждое защищено своим паролем. Нужно последовательно извлекать их, используя разные инструменты.

Подсказка:
1. Попробуйте steghide: steghide extract -sf layered.jpg (попробуйте разные пароли)
2. Попробуйте outguess: outguess -r layered.jpg output.txt
3. Попробуйте zsteg: zsteg -a layered.jpg
4. Проверьте метаданные: exiftool layered.jpg
5. Используйте stegsolve для анализа битовых плоскостей
6. Каждый слой может содержать подсказку к паролю следующего слоя

Команды:
- steghide extract -sf layered.jpg
- outguess -r layered.jpg out.txt
- zsteg -a layered.jpg
- exiftool layered.jpg
- strings layered.jpg | grep school21

Примечание: Пароли могут быть простыми: password, secret, flag, 12345 и т.д.

