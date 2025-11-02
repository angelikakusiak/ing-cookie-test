from playwright.sync_api import Page
from pages.landing_page import LandingPage # Assuming pages/ is in your PYTHONPATH
from utils.cookie_utils import GDPR_COOKIE_NAME, get_cookie_by_name

def test_accept_analytics_cookie(page: Page):
    """ 
    Go to the website ing.pl
    In the cookie consent menu, select “Dostosuj” (Customize)
    Give consent for analytical cookies
    Click “Zaakceptuj wybrane” (Accept selected)
    Verify that the appropriate cookies have been stored in the browser
    """
    
    landing_page = LandingPage(page)
    landing_page.nagivate()
    landing_page.set_custom_cookies(analytical=True, marketing=False)
    
    # check browser cookies to verify if analytical cookies are set
    cookies = page.context.cookies()
    cookie_policy_gdpr = get_cookie_by_name(cookies, GDPR_COOKIE_NAME)
    
    assert cookie_policy_gdpr is not None, "gdpr cookie not found"
    assert cookie_policy_gdpr['value'] == '3', f"Expected gdpr cookie value to be '3', but got '{cookie_policy_gdpr['value']}'"