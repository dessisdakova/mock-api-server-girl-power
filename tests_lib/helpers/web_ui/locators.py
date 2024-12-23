from selenium.webdriver.common.by import By

# Login page
USERNAME_FIELD = (By.CSS_SELECTOR, "input[data-test='username']")
PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-test='password']")
LOGIN_BUTTON = (By.CSS_SELECTOR, "input[data-test='login-button']")
LOGO_DIV = (By.CLASS_NAME, "login_logo")  # for explicit wait

# Inventory Page
SHOPPING_CART_LINK = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
ADD_BACKPACK_BUTTON = (By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
ADD_BIKE_LIGHT_BUTTON = (By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-bike-light']")
SHOPPING_CART_BADGE = (By.CSS_SELECTOR, "span[data-test='shopping-cart-badge']")
INVENTORY_CONTAINER = (By.ID, "inventory_container")  # for explicit wait

# Cart Page
CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[data-test='checkout']")
ITEMS_IN_CART = (By.CSS_SELECTOR, "div[data-test='inventory-item']")  # Also used on Checkout Step Two Page
CART_CONTENTS_CONTAINER = (By.ID, "cart_contents_container")  # for explicit wait

# Checkout Step One Page
FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[data-test='firstName']")
LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[data-test='lastName']")
ZIP_CODE_FIELD = (By.CSS_SELECTOR, "input[data-test='postalCode']")
CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[data-test='continue']")
CHECKOUT_INFO_CONTAINER = (By.ID, "checkout_info_container")  # for explicit wait

# Checkout Step Two Page
FINISH_BUTTON = (By.CSS_SELECTOR, "button[data-test='finish']")
SUMMARY_INFO_DIV = (By.CLASS_NAME, "summary_info")  # for explicit wait

# Checkout Complete Page
MESSAGE_HEADER = (By.CSS_SELECTOR, "h2[data-test='complete-header']")
CHECKOUT_COMPLETE_CONTAINER = (By.ID, "checkout_complete_container")  # for explicit wait
