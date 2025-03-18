# HttPet

## Preparing environment

- Use `make install` for installing `uv` and other project dependencies.
- After above instruction fill to generated `.env` file
- Read `app.services.env` for more information about dotEnvFile

## Run project

- Use `make run` for running project
- Use `make pre` for running `pre-commit run --all-files`

## Тактико технические характеристики HttPet 1107

Необходимо разработать асинхронный скрипт, который будет собирать данные из
нескольких внешних API, обрабатывать их и сохранять в excel.

### Внешние API:
- OpenWeatherMap — для получения данных о погоде в любых 30 городах России
- NewsAPI — для получения новостей по теме “PC gaming”.
- RandomUser — Получить случайных пользователей.

### Скрипт должен:
- Асинхронно запрашивать данные из каждого API.
- Сохранить данные в отдельные листы excel по каждой API

### Разрешённые библиотеки:
- aiohttp
- asyncio
- pandas