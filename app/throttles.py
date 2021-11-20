from rest_framework.throttling import UserRateThrottle


# Create throttle using scope
class LimitThrottle(UserRateThrottle):
    scope = 'limited'


class RateThrottle(UserRateThrottle):
    scope = 'burst'


class VeryLimitedThrottle(UserRateThrottle):
    scope = 'custom_limited'
