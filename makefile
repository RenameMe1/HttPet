install:
	@if [ ! -f .env ]; then\
		echo "API_OPENWEATHER_KEY=" >> .env;\
		echo "API_NEWSAPI_KEY=" >> .env;\
	fi

	pip install uv 
	uv sync

run:
	uv run app/main.py