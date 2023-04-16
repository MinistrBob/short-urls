# short-urls

## Static files
При сборке docker контейнера не получится собрать статические файлы, т.к. setting подключается потом при старте контейнера, монтированием с диска.  
Добавил в settings
```bash
import os

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```


## For develop
### Get requirements.txt
```shell
pip freeze | Out-File -Encoding UTF8 c:\MyGit\short-urls\requirements.txt
```
### Length of VARCHAR
- SQLite does not enforce the length of a VARCHAR. You can declare a VARCHAR(10) and SQLite will be happy to store a 500-million character string there. And it will keep all 500-million characters intact. Your content is never truncated. SQLite understands the column type of "VARCHAR(N)" to be the same as "TEXT", regardless of the value of N.
- PostgreSQL can store a string up to 65,535 bytes long.
- MySQL The length can be specified as a value from 0 to 65,535.
### Docker (example for Windows)
```commandline
cd c:\MyGit\short-urls
git clone https://github.com/DevGivinSchool/GivinSchoolPortal.git .
docker build . -t ministrbob/short-urls:latest
docker push ministrbob/short-urls:latest
# docker run --rm -it -v c:\MyGit\short-urls\short_urls\short_urls.sqlite3:/app/short_urls.sqlite3 ministrbob/short-urls:latest
docker run --name shorturls --rm -d -p 8000:8000 -v c:\MyGit\short-urls\short_urls\short_urls.sqlite3:/app/short_urls.sqlite3 ministrbob/short-urls:latest
```