
all:

tests:
	$(MAKE) -C lib-{{cookiecutter.project_slug}} tests

tests-clean:
	$(MAKE) -C lib-{{cookiecutter.project_slug}} tests-clean

