class car:
    def __init__(self, make, model, msrp):
        self.make = make
        self.model = model
        self.msrp = msrp

    def discountedprice(self):
        return 0.9 * self.msrp


class sport(car):
    def __init__(self, make, model, msrp):
        super().__init__(make, model, msrp)
        self.optionsprice = {'sportwheels': 1000.00, 'sportengine': 3000.00, 'sportinterior': 2000.00}
        self.options = {'sportwheels': 'N', 'sportengine': 'N', 'sportinterior': 'N'}

    def sportwheels(self, option):
        self.options['sportwheels'] = option

    def sportengine(self, option):
        self.options['sportengine'] = option

    def sportinterior(self, option):
        self.options['sportinterior'] = option

    def pricewithoptions(self):
        updatedprice = self.discountedprice()
        for option, value in self.options.items():
            if value == 'Y':
                updatedprice += self.optionsprice[option]
        return updatedprice

car = sport('Mercedes', 'G63', 180000)
car.sportwheels('Y')
car.sportengine('Y')
print(f"Make: {car.make}")
print(f"Model: {car.model}")
print(f"Sticker price (MSRP): ${car.msrp:,.2f}")
print(f"Price with options: ${car.pricewithoptions():,.2f}")