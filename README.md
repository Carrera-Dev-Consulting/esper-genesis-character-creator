# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/Carrera-Dev-Consulting/esper-genesis-character-creator/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                              |    Stmts |     Miss |   Cover |   Missing |
|-------------------------------------------------- | -------: | -------: | ------: | --------: |
| espie\_character\_gen/\_\_init\_\_.py             |       15 |        0 |    100% |           |
| espie\_character\_gen/\_\_main\_\_.py             |        0 |        0 |    100% |           |
| espie\_character\_gen/app.py                      |       16 |       16 |      0% |      7-34 |
| espie\_character\_gen/rest\_app/\_\_init\_\_.py   |        0 |        0 |    100% |           |
| espie\_character\_gen/rest\_app/authentication.py |       47 |       34 |     28% |12, 25-28, 32-65, 71-86, 91 |
| espie\_character\_gen/rest\_app/model.py          |        3 |        0 |    100% |           |
| espie\_character\_gen/server.py                   |      116 |       39 |     66% |41, 45, 49, 53, 57, 109-118, 128, 133, 163, 171-172, 192-199, 206, 215-229, 234-237, 242 |
|                                         **TOTAL** |  **197** |   **89** | **55%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/Carrera-Dev-Consulting/esper-genesis-character-creator/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/Carrera-Dev-Consulting/esper-genesis-character-creator/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Carrera-Dev-Consulting/esper-genesis-character-creator/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/Carrera-Dev-Consulting/esper-genesis-character-creator/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FCarrera-Dev-Consulting%2Fesper-genesis-character-creator%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/Carrera-Dev-Consulting/esper-genesis-character-creator/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.