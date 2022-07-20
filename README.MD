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
![Screenshot_12](https://user-images.githubusercontent.com/56396220/179911017-441a18b5-667d-49e3-96ce-64c2a5e50f3a.png)

При пропуске шага 3, на шаге 4 опять же есть проблема, если исходить из ТЗ, проверка ссылки в адресной строке производится при открытии страницы, но т.к. ссылка сразу редиректит на авторизацию тесты тоже падают. Тут нужны доп.условия на проверку в ТЗ.

![Screenshot_13](https://user-images.githubusercontent.com/56396220/179911054-b5e232ef-c546-4bba-a397-3b01b1c6e187.png)
