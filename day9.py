class Client:
    def __init__(self, name, business_type, budget, problem):
    
        super().__init__()
        
        self.name = name
        self.business_type = business_type
        self.budget = budget
        self.problem = problem
    
    def __str__(self):
        return f"{self.name} | {self.business_type} | ${self.budget} | {self.problem}"


class ClientManager:
    
    def __init__(self):
        super().__init__()
        self.clients = []
    
    def add_client(self, name, business_type, budget, problem):
        client = Client(name, business_type, budget, problem)
        self.clients.append(client)
        return client
    
    def show_all_clients(self):
        print("\n=== CLIENT MANAGER ===")
        print("\nAll Clients:")
        for client in self.clients:
            print(f"- {client.name} | {client.business_type} | ${client.budget} | {client.problem}")
    
    def find_clients_above_budget(self, min_budget):
        filtered_clients = [client for client in self.clients if client.budget > min_budget]
        
        print(f"\nHigh Budget Clients (above ${min_budget}):")
        for client in filtered_clients:
            print(f"- {client.name} | ${client.budget}")
        
        return filtered_clients
    
    def show_highest_paying_client(self):
        if not self.clients:
            print("No clients in the system.")
            return None
        
        highest_paying = max(self.clients, key=lambda client: client.budget)
        
        print(f"\nHighest Paying Client:")
        print(f"{highest_paying.name} — ${highest_paying.budget}")
        
        return highest_paying


if __name__ == "__main__":
    manager = ClientManager()
    

    manager.add_client("ABC Company", "E-commerce", 500, "Needs automation")
    manager.add_client("XYZ Business", "Healthcare", 1500, "Needs data tracking")
    manager.add_client("Nepal Startup", "Finance", 300, "Needs email automation")
    
    manager.show_all_clients()
    manager.find_clients_above_budget(400)
    manager.show_highest_paying_client()