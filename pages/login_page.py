class LoginPage:
    def __init__(self, page):
        self.page = page
        self._username_input = page.locator("[data-test='username']")
        self._password_input = page.locator("[data-test='password']")
        self._login_btn = page.locator("[data-test='login-button']")
    
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_btn.click()