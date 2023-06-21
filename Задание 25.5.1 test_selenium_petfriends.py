import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('alexandrn-mail@yandex.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('Ly3571@')
    # Указывем неявное ожидание
    pytest.driver.implicitly_wait(10)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Указываем переменную явного ожидания:
    wait = WebDriverWait(pytest.driver, 5)
    # Проверяем, что мы оказались на главной странице пользователя
    # Ожидаем в течение 5с, что на странице есть тег h1 с текстом "PetFriends"
    assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), "PetFriends"))
    # Нажимаем на кнопку перехода к выбору списка питомцев
    pytest.driver.find_element_by_xpath('//button[@class="navbar-toggler"]').click()
    # Нажимаем на кнопку для перехода к списку своих питомцев
    pytest.driver.find_element_by_xpath('//*[@href="/my_pets"]').click()
    # Проверяем, что мы оказались на  странице пользователя.
    # Ожидаем в течение 5с, что на странице есть тег h2 с текстом "Александр" -именем пользователя
    assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), "Александр3571"))


    # Ищем на странице все фотографии, имена, породу (вид) и возраст питомцев:
    data_my_pets = pytest.driver.find_element_by_css_selector('tbody/tr')
    # Ожидаем, что данные всех питомцев, видны на странице:
    for i in range(len(data_my_pets)):
        assert wait.until(EC.visibility_of(data_my_pets[i]))
    # Ищем все фотографии своих питомцев
    images = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//img')
    # Проверяем наличие фотографии в карточке
    for i in range(len(images)):
        assert images[i].get_attribute('src') != ''
    # Ищем все имена своих питомцев
    names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    # Проверяем наличие имени в карточке
    for i in range(len(names)):
        assert names[i].text != ''
    # Ищем породы питомцев
    descriptions = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
    # Проверяем наличие породы в карточке
    for i in range(len(descriptions)):
        assert descriptions[i].text != ''
    # Ищем возрасты питомцев
    ages = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
    # Проверяем наличие возраста в карточке
    for i in range(len(ages)):
        assert ages[i].text != ''


    # Ищем на странице /my_pets всю статистику пользователя,и находим из полученных данных количество моих питомцев.
    # Здесь в переменную all_statistics присваивается текст из тега div: "Имя_пользователя \n Питомцев: 6 \n (разрыв строки) Друзей: 0 \n Сообщений: 0" все это одной строкой.
    # Применяю к этому тексту метод .split(\n), т.е. делю его на части по разрыву строки (\n) и получается четыре отдельных текста: ("Имя_пользователя", "Питомцев: 6", "Друзей: 0", "Сообщений: 0")
    all_statistics = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split("\n")
    # В переменную statistics_pets записываю из предыдущей переменной только второй элемент: "Питомцев: 7", его индекс[1] в списке.
    # К этому тексту опять применяю метод разделения .split(" "), но уже делю по пробелу, в итоге получается ("Питомцев", "7").
    statistics_pets = all_statistics[1].split(" ")
    # В переменную all_my_pets записываю число из списка, который получился в statistics_pets, а число стоит последним, поэтому его индекс[-1] и преобразовываю его в int, чтобы текст "7" перевести в число.
    all_my_pets = int(statistics_pets[-1])

    # Проверяем, что количество строк в таблице с моими питомцами равно общему количеству питомцев, указанному в статистике пользователя:
    assert len(data_my_pets) == all_my_pets

    # Проверяем, что хотя бы у половины питомцев есть фотографии
    S = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            S += 1
        assert S >= all_my_pets / 2

    # Проверяем, что у всех питомцев есть имя:
    for i in range(len(names)):
        assert names[i].text != ''

    # Проверяем, что у всех питомцев есть порода:
    for i in range(len(descriptions)):
        assert descriptions[i].text != ''

    # Проверяем, что у всех питомцев есть возраст:
    for i in range(len(ages)):
        assert ages[i].text != ''

    # Проверяем, что у всех питомцев разные имена:
    list_name_my_pets = []
    for i in range(len(names)):
        list_name_my_pets.append(names[i].text)
    set_name_my_pets = set(list_name_my_pets) # преобразовываем список в множество
    assert len(list_name_my_pets) == len(set_name_my_pets) # сравниваем длину списка и множества

