# stepik-parametrisation
Automated pararmetrized test for Stepik [task](https://stepik.org/lesson/237240/step/9?unit=209628)
Page used for [test](http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/)

## USAGE

Test can be run with following parameters:
- browser, run tests in chosen browser. 
Supported values: chrome, firefox. Default: chrome 
```
pytest -v --tb=line test_items.py --lang=fr --browser=firefox
```
- language, run tests in chosen language.
**NOTE**: No default language
```
pytest -v --tb=line test_items.py --lang=en --browser=chrome
```