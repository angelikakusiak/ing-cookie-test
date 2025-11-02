

from typing import List, Optional
from http.cookiejar import Cookie

GDPR_COOKIE_NAME = 'cookiePolicyGDPR'

def get_cookie_by_name(cookies: List[Cookie], name: str) -> Optional[Cookie]:
    """
    Returns the cookie dict with the given name from a list of cookies, or None if not found.
    """
    return next((cookie for cookie in cookies if cookie['name'] == name), None)