Тестовое задание. Слияние логов

Имеется два файла с логами в формате JSONL, пример лог
```
{"timestamp": "2021-02-26 08:59:20", "log_level": "INFO", "message": "Hello"}
{"timestamp": "2021-02-26 09:01:14", "log_level": "INFO", "message": "Crazy"}
{"timestamp": "2021-02-26 09:03:36", "log_level": "INFO", "message": "World!"}
```

Сообщения в заданных файлах упорядочены по полю timestamp в порядке возрастания.

Требуется написать скрипт, который объединит эти два файла в один.
При этом сообщения в получившемся файле тоже должны быть упорядочены в порядке возрастания по полю timestamp.

К заданию прилагается вспомогательный скрипт на python3, который создает два файла "log_a.jsonl" и "log_b.jsonl".

Командлайн для запуска: 
log_generator.py <path/to/dir>

Ваше приложение должно поддерживать следующий командлайн:
```bash
<your_script>.py <path/to/log1> <path/to/log2> -o <path/to/merged/log>
```

Поличилось 3 варианта слияния отсортированных файлов

64mb_files

| Algorithm      | Memory           | Time  |
| -------------  |:-------------:| -----:|
|64mb_files |64mb_files|64mb_files|
| merge_by_memory| 15.6 MiB | 10.115399 sec |
| merge_by_time  | 244.6 MiB | 5.104569 sec |
| pythonic_merge  | 15.6 MiB | 4.529216 sec |

1024mb_files

| Algorithm      | Memory           | Time  |
| -------------  |:-------------:| -----:|
| merge_by_memory| ? | 175.070014 sec |
| merge_by_time  | ? | 121.021235 sec |
| pythonic_merge  | ? | 71.886162 sec |
