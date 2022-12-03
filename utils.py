import os



BRAND_STATUS = {
    "deleted": 0,
    "not_verified": 1,
    "active": 2,
    "in_active": 3,
}


STATUS = {
    "deleted": 0,
    "active": 1,
}


BRANDPO_WEIGHT_CONSIDER = (
    ('dispatch', '1'),
    ('receving', '2'),
    ('whicheverislower', '3')
)