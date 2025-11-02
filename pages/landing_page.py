from playwright.sync_api import Page
from .components.cookie_policy import CookiePolicyModal 
from .components.cookie_settings import CookieSettingsModal 

class LandingPage:
    """
    Represents the main landing page of ing.pl. 
    """
    
    BASE_URL = "https://www.ing.pl/"

    def __init__(self, page: Page):
        self.page = page
          
    def nagivate(self):
        """Navigates to landing page"""
        self.page.goto(self.BASE_URL)
        
        
    def set_custom_cookies(self, analytical: bool, marketing: bool):
            """
            Sets custom cookie preferences.
            
            Args:
                analytical (bool): Whether to accept analytical cookies.
                marketing (bool): Whether to accept marketing cookies.
            """
            
            cookie_modal = CookiePolicyModal(self.page)
            cookie_modal.click_customize()
            
            cookie_settings = CookieSettingsModal(self.page)
            cookie_settings.set_analytical_cookies(analytical)
            cookie_settings.set_marketing_cookies(marketing)
            cookie_settings.accept_selected()
    