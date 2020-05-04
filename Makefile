install:
	@printf "$(OK_COLOR) Installing dependencies...$(NO_COLOR)\n"
	@pip install -r requirements.txt -r test-requirements.txt

test:
	@pytest -vvs ./tests

runserver:
	@python3 -m glittr.api
