# define variables 
VENV = my_venv
PYTHON = python3

# declare phony targets
.PHONY: venv install clean update


# define targets
venv:
	@if [ ! -d "$(VENV)" ]; then $(PYTHON) -m venv $(VENV); fi

create-requirements:
	@if [ ! -f "requirements.txt" ]; then echo  "pandas==2.0.0" > requirements.txt; fi

install: venv create-requirements
	$(VENV)/bin/pip install -r requirements.txt

update: venv
	$(VENV)/bin/pip install --upgrade -r requirements.txt 

clean:
	rm -rf $(VENV) __pychase__


#$(VENV)/bin/pip install --upgrade pip