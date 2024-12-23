<h2>Автотесты на API проекта «Битва покемонов»</h2>

> **Статус проекта:**
> Проект закрытый для POST запросов, но GET можно выполнять без токена: https://pokemonbattle.ru/
> 
> 🟢 Поддерживается (активный) 

## Описание проекта и задачи
Автоматизировать часть проверок регресса с помощью Pytest и Requests

## Тест-кейсы, которые автоматизировали
* Создание покемона `POST /pokemons`
* Смена имени покемона `PUT /pokemons`
* Поймать покемона в покебол `POST /trainers/add_pokeball`
* Проверить ответ метода `GET /trainers`

Ожидаемый ответ: 
* response `status code` = 200
* в ответе в `json` приходит корректное поле `trainer_name`
* в ответе приходит корректное поле id в json

## Детали реализации

1. Автотесты написаны с применением PyTest
2. Используется библиотека Requests
3. Параметризированные тесты с использованием декоратора

![image](https://raw.githubusercontent.com/Eugene-Beskrovny-QA/Python_Pytest_Requests/refs/heads/main/PYTEST1.png)

## Локальный запуск тестов (из терминала)
1. Скачать проект
2. Перейти через терминал в директорию проекта
3. Выполнить команду:

Создаём виртуальное окружение внутри папки проекта.
Далее команды для Windows (для macOS инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
py -m venv venv\
```

``` markdown
venv\Scripts\activate

```

4. Устанавливаем библиотеки

``` markdown
python -m pip install requests
```

``` markdown
python -m pip install pytest
```

Запускаем
``` markdown
pytest tests/test_pokemon.py
```

5. Ожидаемый результат: получим отчет о прохождении тестов.


## Автор

Евгений Бескровный ([@GBloodless](https://t.me/GBloodless))
