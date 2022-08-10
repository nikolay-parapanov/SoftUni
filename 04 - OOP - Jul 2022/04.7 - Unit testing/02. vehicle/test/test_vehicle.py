from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 150)

    def test_vehicle_init(self):
        fuel = 100
        horse_power = 150
        vehicle = Vehicle(fuel, horse_power)

        self.assertEqual(fuel, vehicle.fuel)
        self.assertEqual(fuel, vehicle.capacity)
        self.assertEqual(horse_power, vehicle.horse_power )
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)

    def test_vehicle_string_returns_proper_string(self):
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
                        f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual_result = str(self.vehicle)

        self.assertEqual(expected_result, actual_result)

    def test_drive_raises_when_destination_is_not_reachable(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test_reduce_avaiblable_fuel_when_destination_is_reachable(self):
        self.vehicle.drive(10)
        self.assertEqual(87.5, self.vehicle.fuel)

    def test_refuel_raises_when_tank_full(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_if_refuel_is_within_fuel_tank_capacity(self):
        self.vehicle.fuel = 80
        self.vehicle.refuel(20)

        self.assertEqual(100, self.vehicle.fuel)

if __name__ == '__main__':
    main()
