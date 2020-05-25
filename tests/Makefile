.PHONY: help
help:
	@echo Please read the 'Makefile'

.PHONY: clean
clean:
	rm -rf taiga-back

.PHONY: clone
clone:
	git clone  --depth=1 https://github.com/taigaio/taiga-back.git taiga-back
	cd taiga-back && virtualenv -p python3.6 .venv
	cd taiga-back && .venv/bin/pip install --upgrade pip wheel setuptools
	cd taiga-back && .venv/bin/pip install -r requirements.txt
	cd taiga-back && .venv/bin/pip install -r requirements-devel.txt
	cd taiga-back && .venv/bin/pip install -e ../../

.PHONY: test
test:
	cd taiga-back && .venv/bin/py.test ../test_view.py
