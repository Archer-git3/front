<h1>Инструкция по запуску программы</h1>
Данная инструкция поможет запустить данное веб приложение.

<h2>Установка</h2>
Для работы с приложением необходимо установить flask и бази данних в PostgreSQL. Инструкции по установке и запуске приложение:   


* Склонируйте репозиторий:
```
git clone https://github.com/Archer-git3/DB_lab
```

* установка Flask
```py
pip install Flask
```
* установка и подключение к базе данних. В PostgreSQL ведите следущие команди:
```SQL
CREATE TABLE IF NOT EXISTS public.data
(
    name name COLLATE pg_catalog."C" NOT NULL,
    email character varying COLLATE pg_catalog."default" NOT NULL,
    password character varying COLLATE pg_catalog."default" NOT NULL,
    "like" integer[],
    CONSTRAINT data_pkey PRIMARY KEY (email)
)
```
```SQL
CREATE TABLE IF NOT EXISTS public.data
(
    name name COLLATE pg_catalog."C" NOT NULL,
    email character varying COLLATE pg_catalog."default" NOT NULL,
    password character varying COLLATE pg_catalog."default" NOT NULL,
    "like" integer[],
    CONSTRAINT data_pkey PRIMARY KEY (email)
)

```
* В файле main.py измените перемение и их значение на свои: 
```py
database="database"
user="postgres"
password="password"
host="localhost"
port="5432"
``` 
<h2>Запустите файл main.py</h2>
<h3>PS:Також хочеться зазначити що данний сайт є рекламою для грузиньських страв на якому можна обирати улюбленні страви та писати коментарі до страв</h3>
