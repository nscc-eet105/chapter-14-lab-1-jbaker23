import vehicle
def main():
    jacobs_car = vehicle.Vehicle(0)

    print("Accelerating...")
    jacobs_car.accelerate()
    jacobs_car.display_speed()

    print("Accelerating...")
    jacobs_car.accelerate()
    jacobs_car.display_speed()

    print("\nDecelerating...")
    jacobs_car.decelerate()
    jacobs_car.display_speed()

    print("Decelerating...")
    jacobs_car.decelerate()
    jacobs_car.display_speed()

if __name__ == "__main__":
    main()

