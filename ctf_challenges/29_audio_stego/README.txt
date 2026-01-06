Задание 29: Стеганография в аудио

Категория: Stegano
Сложность: Medium

В аудиофайле song.wav скрыто сообщение методом LSB. Нужно извлечь его с помощью steghide или собственного скрипта.

Подсказка:
1. Используйте steghide: steghide extract -sf song.wav
2. Или используйте Python скрипт для извлечения LSB из аудио
3. Или audacity для анализа волновой формы
4. Или strings: strings song.wav | grep school21
5. Или hexdump: hexdump -C song.wav | grep school21

Пример Python скрипта:
```python
import wave
wav = wave.open('song.wav', 'rb')
frames = wav.readframes(wav.getnframes())
# Извлеките LSB из каждого байта
```

