# short-urls


## For develop
### Get requirements.txt
```shell
pip freeze | Out-File -Encoding UTF8 c:\MyGit\short-urls\requirements.txt
```
### Length of VARCHAR
- SQLite does not enforce the length of a VARCHAR. You can declare a VARCHAR(10) and SQLite will be happy to store a 500-million character string there. And it will keep all 500-million characters intact. Your content is never truncated. SQLite understands the column type of "VARCHAR(N)" to be the same as "TEXT", regardless of the value of N.
- PostgreSQL can store a string up to 65,535 bytes long.
- MySQL The length can be specified as a value from 0 to 65,535.