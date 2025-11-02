from playwright.sync_api import Page, Locator

class CookiePolicyModal:
    """
    Page Object representing the initial cookie policy modal/dialog box 
    of ING Bank Śląski, containing the primary acceptance/rejection buttons.
    """

    def __init__(self, page: Page):
        self.page = page
        
        self.modal_container: Locator = page.locator(".cookie-policy-content[role='dialog']")
        self.customize_button: Locator = page.locator("button.js-cookie-policy-main-settings-button", has_text="Dostosuj")
        self.decline_all_button: Locator = page.locator("button.js-cookie-policy-main-decline-button", has_text="Odrzuć wszystkie")
        self.accept_all_button: Locator = page.locator("button.js-cookie-policy-main-accept-button", has_text="Zaakceptuj wszystkie")

    def accept_all_cookies(self):
        """Clicks the 'Accept all' button."""
        self.accept_all_button.click()

    def decline_all_cookies(self):
        """Clicks the 'Decline all' button."""
        self.decline_all_button.click()

    def click_customize(self):
        """Clicks the 'Customize' button to open settings."""
        self.customize_button.click()
        
    def is_visible(self) -> bool:
        """Checks if the entire cookie policy modal is visible."""
        return self.modal_container.is_visible()