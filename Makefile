# Makefile for Django REST Filtering Tutorial

# ----------------------------------------------------------------------------
# Variables {{{
# ----------------------------------------------------------------------------
SHELL			:= /usr/bin/env bash
ROOT			:= ${CURDIR}
VENV			:= $(ROOT)/.venv
BIN				:= $(VENV)/bin
PYTHON_VER		:= python3.8
PYTHON3			:= $(BIN)/python3
PYTHON			:= $(PYTHON3)
APP_DIR			:= $(ROOT)/src
MANAGE			:= $(PYTHON) manage.py
DATABASE		:= $(ROOT)/db.sqlite3

# Export all variable to sub-make
export
# ----------------------------------------------------------------------------
# }}}
# ----------------------------------------------------------------------------

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show targets
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ----------------------------------------------------------------------------
# LOCAL DEV {{{
# ----------------------------------------------------------------------------

.PHONY: start
start: setup server # Setup the project and run the dev server

.PHONY: setup
setup: # Setup the project
	$(PYTHON_VER) -m venv $(VENV) \
		&& source $(BIN)/activate \
		&& $(BIN)/pip install -r requirements.txt \
		&& $(PYTHON) $(ROOT)/populate_db.py

.PHONY: server
server: ## Run the Django server
	$(MANAGE) runserver $(DJANGO_PORT)

.PHONY: shell
shell: ## Django extension shell
	$(MANAGE) shell_plus --ipython
# ----------------------------------------------------------------------------
# }}}
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# UTILS {{{
# ----------------------------------------------------------------------------

.PHONY: createsecret
createsecret: ## Create DJANGO_SECRET
	@echo "Creating SECRET_KEY"
	@echo "SECRET_KEY="\"`python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'`\"

.PHONY: clean
clean: migrations-delete ## Delete db and venv
	rm $(DATABASE)
	rm -rf $(VENV)

# DB
# ----------------------------------------------------------------------------
.PHONY: reset-db
reset-db:  ## Delete and recreate db&migrations
	$(MANAGE) reset_db --noinput # same as: rm $(DATABASE)
	$(PYTHON) populate_db.py
	# $(MAKE) -f $(ROOT)/Makefile reset-migrations

.PHONY: reset-migrations
reset-migrations:  ## Delete and reset db&migrations
	find $(APP_DIR) -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find $(APP_DIR) -path "*/migrations/*.pyc"  -delete
	$(MANAGE) makemigrations
	$(PYTHON) populate_db.py
# -------------------------------------------------------------------------------------
# }}}
# -------------------------------------------------------------------------------------
