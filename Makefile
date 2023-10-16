# Makefile 

.PHONY:	clean run


run:
	./run.sh

clean:
	python src/modules/run/cleanup.py
