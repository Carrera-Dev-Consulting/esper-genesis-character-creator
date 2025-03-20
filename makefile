.PHONY: unit-test
unit-test:
	pytest tests/unit --cov=espie_character_gen --cov-report=term --cov-report=xml --cov-report=html --html=htmlcov/report.html
.PHONY: int-test
int-test:
	pytest tests/integration --cov=espie_character_gen --cov-report=term --cov-report=xml --cov-report=html --html=htmlcov/report.html
.PHONY: all-test
all-test:
	pytest tests --cov=espie_character_gen --cov-report=term --cov-report=xml --cov-report=html --html=htmlcov/report.html
.PHONY: db-test
db-test:
	pytest tests -m mongo --cov=espie_character_gen --cov-report=term --cov-report=xml --cov-report=html --html=htmlcov/report.html
.PHONY: docs
docs:
	pdoc ./espie_character_gen
.PHONY: build-pdocs
build-pdocs:
	pdoc ./espie_character_gen -o ./docs
.PHONY: build-docs
build-docs:
	make cov-all
	make build-pdocs
.PHONY: serve-docs
serve-docs:
	python -m http.server -d docs 8080
.PHONY: cov-all
cov-all:
	pytest tests --cov=espie_character_gen --cov-report=html:docs/coverage --html=docs/coverage/report.html
.PHONY: render-cov
render-cov:
	python -m http.server -d htmlcov 8081
.PHONY: format
format:
	black .
.PHONY: install
install:
	pip install . -r requirements-dev.txt
.PHONY: lint
lint:
	black . --check
.PHONY: package
package:
	ytt -f deployment/lib/schema.yaml -f deployment/envs/${ENVIRONMENT}/values.yaml -f deployment/deployment.yaml -f deployment/ingress.yaml -f deployment/namespace.yaml -f deployment/service.yaml > espie-character-gen-${ENVIRONMENT}.yaml
.PHONY: ensure-resources
ensure-resources:
	echo "ensuring resources, none exist currently"
start:
	python -m espie_character_gen --port 8080