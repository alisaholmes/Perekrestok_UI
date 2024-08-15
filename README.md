# Проект по тестированию сайта сети магазинов "Перекресток"

### [Ссылка на сайт магазина](https://www.perekrestok.ru/)
![This is an image](design/images/picture.png)

## Содержание
- [Технологии и инструменты](#)
- [Архитектура проекта](#)
- [Список проверок, реализованных в автотестах и ручных тестах](#)
- [Сборка проекта и запуск тестов в Jenkins с параметрами](#)
- [Отчет о результатах тестирования в Allure-reports](#)
- [Автоматическое оповещение о результатах сборки Jenkins в Telegram-бот](#)
- [Возможности Allure TestOps](#)
- [Интеграция с Jira](#)
- [Пример видео-отчета прохождения автотеста на Selenoid](#)


## Технологии и инструменты
Проект реализован с использованием Python, PyCharm, Pytest, Selene, Allure Report, Jenkins, Selenoid, Allure TestOps, Telegram, Jira.
<p align="left">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="40" width="40"/>
<img src="design/icons/selene.png" height="40" width="40"/>
<img src="design/icons/Allure_Report.svg" height="40" width="40"/>     
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40"/>     
<img src="design/icons/selenoid.png" height="40" width="40"/>     
<img src="design/icons/allure_testops.svg" height="40" width="40"/>     
<img src="design/icons/telegram.png" height="40" width="40"/>     
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jira/jira-original.svg" height="40" width="40"/>     

## Архитектура проекта

## Список проверок, реализованных в автотестах и ручных тестах
- [x] Прохождение авторизации под несуществующим номером телефона. Проверка содержимого оповещения о неверном значении
- [x] Наличие возможности выбора адреса доставки при добавлении товара в корзину. Проверка, что открылась соответствующая страница и содержимое строки поиска соответствует заданному значению
- [x] Наличие перехода из пустой корзины в каталог товара
- [x] Выполнение поиска города и его выбора 
- [x] Наличие формы обратной связи. Проверка отправления отзыва 
#### Список проверок ручного тестирования
- [x] Проверка адаптивности верстки к разным типам устройств и расширениям экрана
- [x] Проверка адаптивности страницы к масштабированию


## Сборка проекта и запуск тестов в Jenkins с параметрами
> [Ссылка на сборку в Jenkins](https://jenkins.autotests.cloud/job/Perekrestok_UI/)  
### Для запуска автотестов в Jenkins  
> 1. Открыть [задачу в Jenkins](https://jenkins.autotests.cloud/job/Perekrestok_UI/)  
> 2. Нажать "**Build with Parameters**"  
> 3. Выбрать парметры 
> 4. Нажать "**Build**"

## Отчет о результатах тестирования в Allure-reports  
Результат запуска сборки можно посмотреть в отчёте Allure. 

### Дашборд по результатам запуска
![This is an image](design/images/дашборд.png)

### Пример развернутого отчета автотеста

![This is an image](design/images/отчет.png)



## Автоматическое оповещение о результатах сборки Jenkins в Telegram-бот

![This is an image](design/images/телеграм.png)

## Возможности Allure TestOps

## Интеграция с Jira

## Пример видео-отчета прохождения автотеста на Selenoid

![autotest](design/images/selenoid.gif)