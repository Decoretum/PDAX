class CustomerRepository:
    def __init__(self):
        # Contains Customer Objects
        self.collection = []

    def save(self, customer):
        self.collection.append(customer)

    def find_customer_by_customer_id(self, customer_id):
        for cus in self.collection:
            if cus.customer_id == customer_id:
                return cus