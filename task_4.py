class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = self.get_hours(hours, rest_days)
        self.email = self.get_email(name, email)
    
    @classmethod
    def get_hours(cls, hours=None, rest_days=0):
        if hours is None:
            return (7 - rest_days) * 8
        return hours

    @classmethod
    def get_email(cls, name, email=None):
        if email is None:
            return f"{name}@email.com"
        return email

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment
