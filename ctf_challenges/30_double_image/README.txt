Задание 30: Двойное изображение

Категория: Stegano
Сложность: Hard

Изображение double.png содержит два слоя: видимый и скрытый. Нужно разделить слои и найти флаг в скрытом слое.

Подсказка:
1. Используйте stegsolve для анализа битовых плоскостей
2. Или zsteg: zsteg double.png
3. Или проверьте альфа-канал: convert double.png -alpha extract alpha.png
4. Или используйте Python с PIL/Pillow для анализа каналов
5. Попробуйте разные режимы смешивания в stegsolve

Команды:
- stegsolve (GUI) - Analyze -> Data Extract
- zsteg -a double.png
- python3 -c "from PIL import Image; img = Image.open('double.png'); img.split()"

