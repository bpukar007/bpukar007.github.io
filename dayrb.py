from datetime import date

class Service:
    def __init__(self, name, price_per_unit, units_delivered):
        super().__init__()
        self.name = name
        self.price_per_unit = price_per_unit
        self.units_delivered = units_delivered

class Invoice:
    def __init__(self, client_name, developer_name="Pukar Budhathoki"):
        super().__init__()
        self.client_name = client_name
        self.developer_name = developer_name
        self.services = []
        self.invoice_date = date.today()
    
    def add_service(self, name, price_per_unit, units_delivered):
        service = Service(name, price_per_unit, units_delivered)
        self.services.append(service)
    
    def calculate_total(self):
        total = 0
        for service in self.services:
            total = total + (service.price_per_unit * service.units_delivered)
        return total
    
    def apply_discount(self):
        total = self.calculate_total()
        if total > 500:
            discount = total * 0.10
            return discount
        else:
            return 0
    
    def print_invoice(self):
        subtotal = self.calculate_total()
        discount = self.apply_discount()
        total_due = subtotal - discount
        
        print("=============================")
        print("              INVOICE")
        print("=============================")
        print("Developer: " + self.developer_name)
        print("Client: " + self.client_name)
        print("Date: " + str(self.invoice_date))
        print("-----------------------------")
        print("Services:")
        
        for service in self.services:
            service_total = service.price_per_unit * service.units_delivered
            print("- " + service.name + " | " + str(service.units_delivered) + " units | $" + str(service_total))
        
        print("-----------------------------")
        print("Subtotal: $" + str(subtotal))
        print("Discount: $" + str(discount))
        print("Total Due: $" + str(total_due))
        print("=============================")
        print("Thank you for your business.")
        print("=============================")


# Testing
invoice = Invoice("ABC Company", "Pukar Budhathoki")
invoice.add_service("Python Automation", 50, 3)
invoice.add_service("Make.com Setup", 200, 1)
invoice.add_service("Email Generator", 50, 2)
invoice.print_invoice()