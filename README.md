# HttPet

## Preparing environment

- Use `make install` for installing `uv` and other project dependencies.
- After above instruction fill to generated `.env` file
- Read `app.controllers.env` for more information about dotEnvFile

## Run project

- Use `make run` for running project
- Use `make pre` for running `pre-commit run --all-files`

## Тактико технические характеристики HttPet 1107

Необходимо разработать асинхронное скрипт, который будет собирать данные с
нескольких внешних API, обрабатывать их и сохранять в excel.

### Внешние API:
- OpenWeatherMap — для получения данных о погоде в любых 30 городах России 2
- NewsAPI — для получения новостей по теме “PC gaming”.
- RandomUser — Получить случайных пользователей.

### Скрипт должен:
- Асинхронно запрашивать данные с каждого API.
- Сохранить данные в excel в отдельный лист по каждой API

### Разрешённые библиотеки:
- aiohttp
- asyncio
- pandas