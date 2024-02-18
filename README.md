Финальный проект из курса Автоматизация тестирования с помощью Selenium и Python.

pytest -v --tb=line --language=en -m need_review

Ниже находятся критерии по которым оценивался проект

Критерий 1 /
Убедитесь, что в проекте присутствуют следующие файлы.

requirements.txt /
conftest.py /
__init__.py /
test_main_page.py /
test_product_page.py /
pytest.ini 

В папке pages:
base_page.py /
basket_page.py /
locators.py /
login_page.py /
product_page.py /
main_page.py 

Критерий 2 /
Откройте файл test_product_page.py.

В файле есть следующие тесты:

test_user_can_add_product_to_basket /
test_guest_can_add_product_to_basket /
test_guest_cant_see_product_in_basket_opened_from_product_page /
test_guest_can_go_to_login_page_from_product_page /
Тесты помечены как @pytest.mark.need_review 

Критерий 3 /
Запустите тесты командой pytest -v --tb=line --language=en -m need_review.

Убедитесь, что все тесты проходят.
Должны запуститься следующие тесты:

test_user_can_add_product_to_basket /
test_guest_can_add_product_to_basket /
test_guest_cant_see_product_in_basket_opened_from_product_page /
test_guest_can_go_to_login_page_from_product_page

Критерий 4 /
Посмотрите внимательнее на то, как написаны эти 4 теста. Убедитесь, что они написаны в стиле PageObject:

нет assert в теле тестов (в файле test_product_page.py) /
все методы действия и проверки выделены в отдельные методы внутри классов PageObject /
все локаторы лежат в locators, их нет в коде страниц или тестов /

Критерий 5 /
Тест test_user_can_add_product_to_basket находится в классе TestUserAddToBasketFromProductPage.

В классе есть setup. /
В setup есть регистрация нового пользователя.


