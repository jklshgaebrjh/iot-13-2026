class Smartphone:
    def __init__(
        self, model, price, memory_capacity, battery_capacity
    ):
        self.price = price
        self.model = model
        self.memory_capacity = memory_capacity
        self.battery_capacity = battery_capacity

    def __del__(self):
        pass

    def print_info(self):
        print(f"model: {self.model}"
              f"\nprice: {self.price} usd"
              f"\nstorage capacity: {self.memory_capacity} gb"
              f"\nbattery capacity: {self.battery_capacity} mAh"
              f"\n{'-' * 30}")


class PhoneStore:
    def __init__(self):
        self.phones = []

    def add_new_phone(self, phone):
        self.phones.append(phone)

    def sort_by_price(self):
        print("\n   phones sorted by price")
        sorted_phones = sorted(self.phones, key=lambda item: item.price)
        for phone in sorted_phones:
            phone.print_info()

    def best_choice(self, budget):
        print(f"\n   best choice for {budget} usd budget")
        below_budget = [
            phone for phone in self.phones if phone.price <= budget
        ]

        if below_budget:
            best_phone = max(
                below_budget,
                key=lambda item: (
                    item.memory_capacity,
                    item.battery_capacity
                    )
                )
            best_phone.print_info()
        else:
            print("no phones that fit the budget")
            
    # def find_phone(self):
    #     print([phone.model for phone in self.phones if phone.price == 300])
             


def main():
    store = PhoneStore()

    store.add_new_phone(Smartphone(
        "Iphone", 950, 512, 3600
    ))
    store.add_new_phone(Smartphone(
        "Xiaomi", 300, 128, 4200
    ))
    store.add_new_phone(Smartphone(
        "Samsung", 800, 1024, 5200
    ))
    store.add_new_phone(Smartphone(
        "Vivo", 300, 512, 4000
    ))
    store.add_new_phone(Smartphone(
        "Poco", 300, 512, 3200
    ))
    
    store.find_phone()
    store.sort_by_price()
    store.best_choice(400)
    
        
    for phone in store.phones:
        print(f"{phone.model} price is: {phone.price} usd")

main()
