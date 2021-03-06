from bubblebooking.models.accounts import Account
from bubblebooking.models.accounts import Permissions

class AdminAccount(Account):
    """Inherit from Account Class"""
    def __init__(self):
        super().__init__()
        self.acc_type = "admin"
        self.permissions = Permissions("admin")
