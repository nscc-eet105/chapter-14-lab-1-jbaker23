#My name is Jacob Baker and this is Chapter 14 Lab 1 being done on July 12
import vehicle
def main():
    jacobscar = vehicle.Vehicle(0)



    print("Accelerating...")
    jacobscar.accelerate()
    jacobscar.display_speed()

    print("Accelerating...")
    jacobscar.accelerate()
    jacobscar.display_speed()

    print("\nDecelerating...")
    jacobscar.decelerate()
    jacobscar.display_speed()

    print("Decelerating...")
    jacobscar.decelerate()
    jacobscar.display_speed()

if __name__ == "__main__":
    main()

