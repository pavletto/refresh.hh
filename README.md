# autoupdate-hh-resume

Маленький скрипт, выполняющий автоматическую публикацию резюме на сайте [hh].

## Конфигурация

Для работы требуется выполнить скрипт со следующими аргументами:

```sh
python /path/to/hh.py <token> <resume_id>
```

- идентификатор резюме (resume_id) - берем из адресной строки, выбрав нужное резюме на сайте
- токен доступа (access_token) - можно получить здесь [hh-api]

А также установить следующие пакеты:

```sh
$ pip install requests
$ pip install logging
```

## Установка

Для автоматического выполнения создать таск в [cron]

```sh
$ (crontab -l; echo "0 */4 * * * python /path/to/hh.py <token> <resume_id>" ) | crontab
```

[cron]: http://help.ubuntu.ru/wiki/cron
[hh]: http://hh.ru
[hh-api]: https://dev.hh.ru/admin
