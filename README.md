# Esper Genesis Character Creator

Small application to be able to build your own character to play the game Esper Genesis Role Playing Game

[![Test and Deploy Docs](https://github.com/Carrera-Dev-Consulting/esper-genesis-character-creator/actions/workflows/deploy-docs.yaml/badge.svg)](https://github.com/Carrera-Dev-Consulting/esper-genesis-character-creator/actions/workflows/deploy-docs.yaml)

## Table of Contents

- [Useful Links](#useful-links)
- [Installation](#installation)
- [Usage](#usage)
- [Running Locally](#running-locally)
- [GraphQL Usage](#graphql-usage)
  - [Queries](#queries)
  - [Mutations](#mutations)

## Useful Links

Links to result of code coverage and pytest of latest builds.

- [Coverage Report](https://consulting.gxldcptrick.dev/esper-genesis-character-creator/coverage/)
- [Latest Test Run](https://consulting.gxldcptrick.dev/esper-genesis-character-creator/coverage/report.html)
- [Documentation](https://consulting.gxldcptrick.dev/esper-genesis-character-creator/)

## Installation

`pip install esper-character-gen`

We require at least python 3.10 to be able to run properly.

## Usage

To launch the app you will just need to run the package directly.

```bash
    > esper-character-gen --port 8080
INFO:     Started server process [16240]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:5000 (Press CTRL+C to quit)
```

CLI Support the following params

- `--host/-h` hostname you want to server your api from. defaults to `"localhost"`
- `--port/-p` port you want to listen on. defaults to `5000`
- `--worker-count/-w` amount of worker tasks to run concurrently. defaults to `1`

```bash
    > esper-character-gen -p 5000 -h 0.0.0.0 -w 10
```

### Configurations

<details>
    <summary>Cross Origin Resource Sharing (CORS)</summary>

| Environment Variables    | Description                                                |
| ------------------------ | ---------------------------------------------------------- |
| `CORS_ORIGINS`           | Comma separated list of origins to allow. Default: `["*"]` |
| `CORS_ALLOW_CREDENTIALS` | Whether or not to allow credentials. Default: `True`       |
| `CORS_METHODS`           | Comma separated list of methods to allow. Default: `["*"]` |
| `CORS_HEADERS`           | Comma separated list of headers to allow. Default: `["*"]` |

</details>

<details>
    <summary>Logging</summary>

| Environment Variables | Description                              |
| --------------------- | ---------------------------------------- |
| `LOG_LEVEL`           | The log level to use. Default: `"DEBUG"` |

</details>

## Running locally

To run the service locally you simply need to run the module directly with python like:

```bash
    > python -m espie_character_gen
```

To run the unit tests locally you can use the `unit-test` make target like:

```bash
    > make unit-test
```

To run the integration tests locally you can use the `int-test` make target but please run `ensure-resources` before which will require docker to have been installed and or install and run mongo using the default port with no username or password.

```bash
# If not running mongo already please use the docker config we provided in the compose file
    > make ensure-resources
# actually running the tests
    > make int-test
```

The same also applies for all-test since this will run both the integration tests as well as unit tests.
Use the `all-test` make target.

```bash
# If not running mongo locally already run this
    > make ensure-resources
# actually running the tests
    > make all-test
```

Running tests that relate to databases which currently is only mongo will be run with `db-test` make target. This is useful when you mark your tests properly with the `pytest.mark.mongo` so that you can disitinguish a test that uses mongo components with it.

```bash
# If not running mongo locally already run this
    > make ensure-resources
# actually running tests
    > make db-test
```

All these test configs are configured to also output coverage results to help you see how many lines you are covering with three reports: terminal, xml, html

To view the xml you can configure most any tool in vscode to read the file but I use `coverage gutters` to be able to display it visually when I am inspecting the src files.

To view the html, you can run the `render-cov` make target to spin up a simple http server built into python to inspect and view the `htmlcov` folder html and render it properly in your browser at `8081`. This is super useful when you want to really investigate and key into areas that are not covered.

To view the terminal output, you will just be shown it immediately after you run the make commands in the terminal so you can enjoy it!!

## Contribution

For details of conduct and expactations please refer to [CONTRIBUTION.md](https://github.com/Carrera-Dev-Consulting/esper-genesis-character-creator/blob/main/CONTRIBUTING.md)

Pull requests will be pending review of at least one maintainer.

Pull requests are required to have finished the template checklist before they will be reviewed by a maintainer.

All code is formatted with the black formatter and we expect types and may run mypy to check that your code is properly typed as expected.

Names should make sense and be self descriptive of the proposed changes.
