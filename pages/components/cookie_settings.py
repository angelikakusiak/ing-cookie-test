from playwright.sync_api import Page, Locator

class CookieSettingsModal:
    """
    Page Object representing the detailed cookie settings modal 
    (after clicking 'Dostosuj' / 'Customize').
    """

    def __init__(self, page: Page):
        self.page = page
        
        self.modal_container: Locator = page.locator(".cookie-policy-content[role='dialog']")
        self.back_button: Locator = page.locator("button.js-cookie-policy-settings-cancel-button")
        
        self.decline_all_settings_button: Locator = page.locator(".js-cookie-policy-settings-decline-all-button")
        self.accept_selected_button: Locator = page.locator(".js-cookie-policy-settings-decline-button", has_text="Zaakceptuj zaznaczone")
        
        self.technical_toggle: Locator = page.locator("div[name='CpmTechnicalOption'][role='switch']")
        self.analytical_toggle: Locator = page.locator("div[name='CpmAnalyticalOption'][role='switch']")
        self.marketing_toggle: Locator = page.locator("div[name='CpmMarketingOption'][role='switch']")
    
    def set_analytical_cookies(self, state: bool):
        """Sets the Analytical cookies toggle to ON (True) or OFF (False)."""
        current_state = self.analytical_toggle.get_attribute("aria-checked") == "true"   
        if current_state != state:
            self.analytical_toggle.click()
            
    def set_marketing_cookies(self, state: bool):
        """Sets the Marketing cookies toggle to ON (True) or OFF (False)."""
        current_state = self.marketing_toggle.get_attribute("aria-checked") == "true"
        if current_state != state:
            self.marketing_toggle.click()
            
    def accept_selected(self):
        """Clicks the 'Accept selected' button."""
        self.accept_selected_button.click()
        
    def decline_all_from_settings(self):
        """Clicks the 'Decline all' button from the settings screen."""
        self.decline_all_settings_button.click()
            
    def is_visible(self) -> bool:
        """Checks if the settings modal is visible."""
        return self.modal_container.is_visible()