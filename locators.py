from selenium.webdriver.common.by import By


# Личный кабинет и профиль
class PersonalAccountLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//*[contains(text(), 'Личный Кабинет')]")  # кнопка Личный кабинет
    FIELD_EMAIL = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")  # поле Email
    FIELD_PASSWORD = (By.XPATH, "(.//input[@class='text input__textfield text_type_main-default'])[2]")  # поле Пароль
    BUTTON_LOG_IN = (By.XPATH, ".//button[text()='Войти']")  # кнопка Войти
    BUTTON_PROFILE = (By.XPATH, "//a[text()='Профиль']")  # кнопка Профиль
    BUTTON_HISTORY_ORDERS = (By.XPATH, "//a[text()='История заказов']")  # кнопка История заказов
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # кнопка Выход
    LAST_ORDER_FROM_ORDER_HISTORY = (By.XPATH, "(.//p[@class='text text_type_digits-default'])[last()]")  # последний сделанный заказ в списке История заказов


# Восстановление пароля
class PasswordRecoveryLocators:
    BUTTON_RECOVERY_PASSWORD_PAGE = (By.XPATH, ".//*[contains(text(), 'Восстановить пароль')]")  # кнопка Восстановить пароль в форме авторизации
    FIELD_EMAIL = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")  # поле Email
    BUTTON_RECOVERY = (By.XPATH, ".//button[contains(text(), 'Восстановить')]")  # кнопка Восстановить
    FIELD_PASSWORD = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default']")  # поле Пароль
    ICON_HIDE_PASSWORD = (By.XPATH, ".//div[@class='input__icon input__icon-action']")  # иконка видимости пароля
    FIELD_FRAMING = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_password input_size_default']")  # обычное поле (без подсветки)
    FIELD_FRAMING_ILLUMINATION = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")  # активное поле (с подсветкой)


# Конструктор
class ConstructorLocators:
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # кнопка Конструктор
    TEXT_COLLECT_BURGER = (By.XPATH, ".//*[text()='Соберите бургер']")  # текст Соберите бургер
    TEXT_INGREDIENT_DETAILS = (By.XPATH, ".//*[text()='Детали ингредиента']")  # текст Детали ингредиента
    BUTTON_CLOSE_INGREDIENT_DETAILS = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")  # кнопка Закрыть детали ингредиента
    DROP_ZONE_CONSTRUCTOR = (By.XPATH, ".//*[@class='constructor-element constructor-element_pos_top']")  # Зона для перетаскивания ингредиента в заказ
    BUTTON_PLACE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка Оформить заказ
    TEXT_ORDER_ID = (By.XPATH, ".//p[text()='идентификатор заказа']")  # текст Идентификатор заказа


# Лента заказов
class OrderFeedLocators:
    BUTTON_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")  # кнопка Лента заказов
    TEXT_ORDER_FEED = (By.XPATH, ".//*[text()='Лента заказов']")  # текст Лента заказов
    TEXT_ORDER_ID = (By.XPATH, ".//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")  # Идентификатор заказа
    BUTTON_CLOSE_ORDER_ID = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")  # кнопка закрыть созданный заказ
    ORDER_FROM_ORDER_FEED = (By.XPATH, ".//p[@class='text text_type_digits-default']")  # первый заказ в списке Лента заказов
    TEXT_COMPOSITION_ORDER = (By.XPATH, ".//p[@class='text text_type_main-medium mb-8']")  # текст Состав в карточке заказа
    TEXT_COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "(.//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")  # текст счетчика Выполнено за все время
    TEXT_COUNTER_COMPLETED_FOR_TODAY = (By.XPATH, "(.//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")  # текст счетчика Выполнено за сегодня
    TEXT_LIST_ON_WORK = (By.XPATH, ".//li[@class='text text_type_main-small']")  # текст внутри раздела В работе
