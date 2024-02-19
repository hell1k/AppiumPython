from pages.base_page import BasePage


class WelcomeActivity(BasePage):
    skip_tutorial_btn = "com.yapmap.yapmap:id/activity_welcome_button"

    def close_tutorial(self):
        try:
            self.click(self.skip_tutorial_btn)
        except:
            pass