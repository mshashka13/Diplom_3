# Diplom_3
## __Тестирование UI Stellar Burgers__ 
[Stellar Burgers](https://stellarburgers.nomoreparties.site "Перейти на сайт")

___

### __Тесты (tests):__  
__*test_main_functionality - Тесты на проверку основного функционала:*__
- test_check_go_to_constructor_from_personal_account_unauthorized - Проверка перехода на "Конструктор" из формы авторизации
- test_check_go_to_constructor_from_personal_account_authorized - Проверка перехода на "Конструктор" из Личного кабинета
- test_check_go_to_constructor_from_order_feed - Проверка перехода на "Конструктор" из "Ленты заказов"
- test_check_go_to_order_feed_from_personal_account_unauthorized - Проверка перехода на "Ленту заказов" из формы авторизации
- test_check_go_to_order_feed_from_personal_account_authorized - Проверка перехода на "Ленту заказов" из Личного кабинета
- test_check_go_to_order_feed_from_constructor - Проверка перехода на "Ленту заказов" из Конструктора
- test_check_ingredient_details_go_to_ingredient - Проверка открытия всплывающего окна с деталями ингредиента и закрытия этого окна
- test_drag_and_drop_ingredient_with_counter - Проверка увеличения каунтера ингредиента при добавлении данного ингредиента в заказ
- test_place_order_with_multiple_ingredients - Проверка успешного оформления заказа с разными наборами ингредиентов авторизованным пользователем

__*test_order_feed - Тесты на проверку раздела "Лента заказов":*__
- test_check_window_with_order_details - Проверка всплывающего окна с деталями заказа при клике на заказ
- test_check_show_orders_from_orders_history_on_order_feed - Проверка отображения заказов из "Истории заказов" пользователя в "Ленте заказов"
- test_check_increment_counter_completed_for_all_time_when_creating_order - Проверка увеличения счетчика "Выполнено за все время" при создании нового заказа
- test_check_increment_counter_completed_for_today_when_creating_order - Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа
- test_check_show_order_in_work_when_creating_order - Проверка появления заказа в разделе "В работе" после его оформления

__*test_password_recovery - Тесты на страницу восстановления пароля:*__
- test_check_transition_to_page_recovery_password - Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"
- test_check_input_email_and_click_button_recovery - Проверка ввода почты и клик по кнопке "Восстановить"
- test_click_button_to_show_password - Проверка активности поля при клике на кнопкну "показать/скрыть" пароль

__*test_personal_account - Тесты на личный кабинет:*__
- test_check_transition_to_page_personal_account - Проверка авторизации и перехода по клику на "Личный кабинет"
- test_check_transition_to_page_order_history - Проверка авторизации и перехода в раздел "История заказов"
- test_check_log_out_from_personal_account - Проверка авторизации и выхода из аккаунта



### __Страницы для шагов тестов:__
__*base_page - Базовые методы:*__
- find_element_webdriverwait - Найти элемент
- click_element - Кликнуть элемент
- add_text_to_element - Ввести текст в элементе
- get_text_from_element - Получить текст элемента
- scroll_to_element - Скроллить до элемента
- url_changes - Дождаться, когда поменяется URL
- wait_for_url_change - Получить новый URL

__*main_functionality_page - Основной функционал:*__
- go_to_personal_account_unauthorized - Перейти в "Личный кабинет" без авторизации
- go_to_personal_account_authorized - Перейти в "Личный кабинет" с авторизацией
- go_to_constructor - Перейти в "Конструктор"
- go_to_order_feed - Перейти в "Ленту заказов"
- is_constrictor_visible - Дождаться загрузки заглавного текста в "Конструкторе"
- is_order_feed_visible - Дождаться загрузки заглавного текста в "Ленте заказов"
- burger_ingredient_by_index - Динамический локатор ингредиента по индексу
- go_to_ingredient_by_index - Открыть "Детали ингредиента" по индексу ингредиента
- is_ingredient_details_visible - Дождаться загрузки текста в окне "Детали ингредиента"
- close_ingredient_details - Закрыть окно "Детали ингредиента"
- scroll_to_ingredient - Скроллить до ингредиента
- drag_and_drop_ingredient - Перетащить ингредиент по индексу в зону конструктора
- get_ingredient_by_counter - Динамический локатор каунтера по индексу
- get_counter_value - Получить значение каунтера ингредиента по индексу
- drag_and_drop_ingredient_firefox - Перетащить ингредиент по индексу в зону конструктора в бразуере Firefox
- click_button_place_order - Клик по кнопке "Оформить заказ"
- is_window_order_id_visible - Дождаться появления окна с идентификатором заказа

__*order_feed_page - Лента заказов:*__
- go_to_personal_account - Перейти в личный кабинет
- go_to_order_history - Перейти в историю заказов
- go_to_constructor - Перейти в "Конструктор"
- get_order_id_from_order_history - Получить номер последнего заказа в "Истории заказов"
- click_to_first_order_from_order_feed - Клик на первый заказ в списке "Ленты заказов"
- is_window_with_order_details_visible - Дождаться загрузки текста в окне "Детали заказа"
- burger_ingredient_by_index - Динамический локатор ингредиента по индексу
- go_to_ingredient_by_index - Открыть "Детали ингредиента" по индексу ингредиента
- is_ingredient_details_visible - Дождаться загрузки текста в окне "Детали ингредиента"
- close_ingredient_details - Закрыть окно "Детали ингредиента"
- scroll_to_ingredient - Скроллить до ингредиента
- drag_and_drop_ingredient - Перетащить ингредиент по индексу в зону конструктора
- get_ingredient_by_counter - Динамический локатор каунтера по индексу
- get_counter_value - Получить значение каунтера ингредиента по индексу
- drag_and_drop_ingredient_firefox - Перетащить ингредиент по индексу в зону конструктора в бразуере Firefox
- create_order - Оформить заказ
- click_button_place_order - Клик по кнопке "Оформить заказ"
- is_window_order_id_visible - Дождаться появления окна с идентификатором заказа
- close_window_order_id - Закрыть окно с id заказа
- go_to_order_feed - Перейти в "Ленту заказов"
- order_by_id - Динамический локатор заказа по его id в Ленте заказов
- get_text_from_counter_completed_for_all_time - Получить значение счетчика "Выполнено за все время"
- get_text_from_counter_completed_for_today - Получить значение счетчика "Выполнено за сегодня"
- wait_for_text_in_work_to_change - Дождаться изменения текста в разделе "В работе"

__*password_recovery_page - Восстановление пароля:*__
- check_transition_to_page_recovery_password - Переход на страницу восстановления пароля
- check_input_email_and_click_button_recovery - Ввод почты и клик по кнопке "Восстановить"
- click_button_to_show_password - Клик по иконке "показать пароль"

__*personal_account_page - Личный кабинет:*__
- go_to_personal_account - Перейти в личный кабинет
- go_to_order_history - Перейти в историю заказов
- log_out - Выйти из личного кабинета
- is_profile_visible - Дождаться загрузки кнопки "Профиль"




### __Вспомогательные элементы:__
1. locators - Локаторы: Личный кабинет и профиль, Восстановление пароля, Конструктор, Лента заказов
2. data - Константы: Url, данные для авторизации
3. conftest - Фикстуры: драйверы Chrome и Firefox, авторизация пользователя
4. requirements - Файл с внешними зависимостями
5. README - описание тестируемого функционала







