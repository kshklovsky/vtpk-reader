# File is used for running things locally in development

.PHONY: \
	confirm confirm2 \
	unittest pytest test format ruff ruff_check coverage mypy check lint \
	build clean_build upload_test_pypi install_test_pypi upload_pypi install_pypi \
	open_github open_coveralls open_test_pypi open_pypi \
	conda_create_all conda_delete_all conda_update_all


# Utilities
confirm:
	@echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]

confirm2:
	@echo -n "Are you sure? [Y/n] " && read ans && [ $${ans:-Y} != Y ] && echo "Aborted" && exit 1

# Commands for development

unittest:
	python -m unittest -v tests/vtpk_reader_tests.py

pytest:
	pytest

test:
	pytest

format:
	ruff format

ruff ruff_check:
	ruff check --fix

coverage:
	coverage run -m unittest -v tests/vtpk_reader_tests.py
	coverage report
	coverage html
	open htmlcov/index.html

mypy:
	mypy vtpk_reader
	mypy tests

check lint: pytest format ruff_check mypy


# Artifact-related

clean_build:
	-rm -fR ./dist/*

# This builds artifacts for upload
build: clean_build
	python -m build
	ls -la dist/

upload_test_pypi:
	python -m twine upload --repository testpypi dist/*

install_test_pypi:
	python -m pip install --index-url https://test.pypi.org/simple/ --no-deps vtpk-reader

upload_pypi: confirm
	python -m twine upload dist/*

install_pypi:
	python -m twine upload dist/*


# Open relevant webpages

open_github:
	open "https://github.com/kshklovsky/vtpk-reader"

open_coveralls:
	open "https://coveralls.io/github/kshklovsky/vtpk-reader"

open_test_pypi:
	open "https://test.pypi.org/project/vtpk-reader/"

open_pypi:
	open "https://pypi.org/project/vtpk-reader/"


# Conda environment management
conda_create_all:
	conda env create --yes --file scripts/conda_environments/conda_vtpk_devel_p309.yml
	conda env create --yes --file scripts/conda_environments/conda_vtpk_devel_p311.yml
	conda env create --yes --file scripts/conda_environments/conda_vtpk_test_p309_pip.yml
	conda env create --yes --file scripts/conda_environments/conda_vtpk_test_p309_pip_bare.yml
	conda env create --yes --file scripts/conda_environments/conda_vtpk_test_p311_pip.yml

conda_delete_all:
	-conda env remove -n vtpk_devel_p309 --yes
	-conda env remove -n vtpk_devel_p311 --yes
	-conda env remove -n vtpk_test_p309_pip --yes
	-conda env remove -n vtpk_test_p309_pip_bare --yes
	-conda env remove -n vtpk_test_p311_pip --yes

conda_update_all:
	conda env update --prune --file scripts/conda_environments/conda_vtpk_devel_p309.yml
	conda env update --prune --file scripts/conda_environments/conda_vtpk_devel_p311.yml
	conda env update --prune --file scripts/conda_environments/conda_vtpk_test_p309_pip.yml
	conda env update --prune --file scripts/conda_environments/conda_vtpk_test_p309_pip_bare.yml
	conda env update --prune --file scripts/conda_environments/conda_vtpk_test_p311_pip.yml
