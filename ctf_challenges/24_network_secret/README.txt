Задание 24: Сетевой секрет

Категория: Forensics (PCAP)
Сложность: Medium

В дампе traffic.pcap есть HTTP-сессия, в которой передан файл с флагом. Нужно извлечь файл из потока.

Подсказка:
1. Откройте файл в Wireshark: wireshark traffic.pcap
2. Фильтруйте HTTP трафик: http
3. Найдите HTTP запрос с файлом (POST или GET)
4. Извлеките данные: File -> Export Objects -> HTTP
5. Или используйте tshark: tshark -r traffic.pcap -Y http -T fields -e http.file_data
6. Или strings: strings traffic.pcap | grep school21

