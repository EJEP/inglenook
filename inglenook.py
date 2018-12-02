"""Code to provide a random starting and ending order for a 3-2-2 inglenook,
with 6 wagons."""

from random import sample, choice, shuffle, randint

def get_wagons():
    """Set the wagons which are available"""

    wagons = ['British Steel', 'Van', 'ZKV', 'ZHV', 'Grey 16T', 'Black 16T']

    return wagons

def get_starting_setup(wagons):
    """Generate the starting positions of the wagons."""

    # First decide where the wagons will go
    num_back = randint(2, 3)

    if num_back == 2:
        num_mid = 2
        num_front = 2

    if num_back == 3:
        fill_mid = choice([True, False])
        if fill_mid:
            num_mid = 2
            num_front = 1
        if not fill_mid:
            num_mid = 1
            num_front = 2

    # Randomise the order of the wagons
    shuffle(wagons)

    back = wagons[0:num_back]
    mid = wagons[num_back:num_back+num_mid]
    front = wagons[num_back+num_mid:]

    print("The starting setup is:")
    print("Back: " + str(back))
    print("Middle: " + str(mid))
    print("Front: " + str(front))

def get_target(wagons):
    """Set the target train to be assembled. Four cars long"""

    target = sample(wagons, 4)

    print("The target order is: ")
    print(target)

def main():

    wagons = get_wagons()

    get_target(wagons)

    get_starting_setup(wagons)

if __name__ == "__main__":
    main()
