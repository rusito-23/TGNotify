PYTHON=$(shell which python)
FILES=files.txt

all:
	$(PYTHON) setup.py install --record $(FILES)

clean:
	xargs rm -rf < $(FILES)
