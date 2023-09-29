class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> object:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: int,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> object:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.wash_single_car(car)

        return income

    def calculate_washing_price(self, car: Car) -> float:
        clean_mark_diff = self.clean_power - car.clean_mark
        divident = car.comfort_class * clean_mark_diff * self.average_rating
        divider = self.distance_from_city_center
        return round(divident / divider, 1)

    def wash_single_car(self, car: Car) -> float:
        wash_cost = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return wash_cost

    def rate_service(self, rate: float) -> float:
        full_rating = (self.average_rating * self.count_of_ratings + rate)
        self.count_of_ratings += 1
        self.average_rating = round(full_rating / self.count_of_ratings, 1)
        return self.average_rating
