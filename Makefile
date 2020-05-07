install:
	@printf "$(OK_COLOR) Installing dependencies...$(NO_COLOR)\n"
	@pip install -r requirements.txt -r test-requirements.txt

test:
	@pytest -vvs ./tests

initdb:
	@python glittr/models/db_models.py db init

migratedb:
	@python glittr/models/db_models.py db migrate
	
upgradedb:
	@python glittr/models/db_models.py db upgrade

rollbackdb:
	@python glittr/models/db_models.py db downgrade
runserver:
	@python3 -m glittr.api
