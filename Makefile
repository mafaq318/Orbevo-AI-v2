.PHONY: clean run install_dep install_linux_host_dep setup_linux_env

all: run

setup_linux_env: install_linux_host_dep 

setup_win_env: install_win_host_dep

install_win_host_dep:
	./third_dep_win.sh

install_linux_host_dep:
	./third_dep_linux.sh

run:
	./run.sh

clean:
	python src/modules/run/cleanup.py
