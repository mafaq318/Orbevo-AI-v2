.PHONY: clean run install_dep install_linux_host_dep setup_linux_env

all: setup_linux_env

setup_linux_env: install_linux_host_dep install_pip_dep

install_linux_host_dep:
	./third_dep.sh

install_pip_dep:
	./pip_dep.sh || true

run:
	./run.sh

clean:
	python src/modules/run/cleanup.py
