# AUTOTEST MOS.RU

Проект автотестов mos.ru

#### Стэк
- язык программирования - [Python 3.8](https://www.python.org/downloads/)
- тестовый фреймворк - [pytest](https://docs.pytest.org/en/latest/)
- ui-автоматизация: [Selenium](https://selenium-python.readthedocs.io/index.html), [Selene](https://github.com/yashaka/selene)
- отчеты - [allure](https://docs.qameta.io/allure/)

#### Структура
```bash
.
├── core
│   ├── api                 # описание api-классов
│   ├── data                # тестовые данные
│   ├── locators            # Локаторы  
│   ├── models              # описание моделей запросов и ответов
│   ├── pages               # описание классов страниц (PageObjects)
│   ├── resources           # папка для хранения бинарных данных
│   ├── utils               # утилиты и хелперы текущего проекта
│   └── backend.py          # фасад для api-классов проекта, управление сессией
├── pages                   # страницы
├── tests
│   ├── test_suite_name.py  # тесты 
├── conftest.py             # фикстуры 
└── requirements.txt        # подключение внешних библиотек
```


#### Результаты теста
Есть проблема с шагом 3. Тесты падают на проверке статусов, так как одна из страниц отдает 404 ошибку.
![Screenshot_11](https://user-images.githubusercontent.com/56396220/179838780-7a0bc91c-c7ca-45a7-957a-3b1df1db51e7.png)
При пропуске шага 3, на шаге 4 опять же есть проблема, если исходить из ТЗ, проверка ссылки в адресной строке производится при открытии страницы, но т.к. ссылка сразу редиректит на авторизацию тесты тоже падают. Тут нужны доп.условия на проверку в ТЗ.
![Screenshot_10](https://user-images.githubusercontent.com/56396220/179838775-efea17b0-71a7-4e0c-ba84-ec0b0960ffb4.png)

