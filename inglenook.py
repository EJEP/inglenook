"""Generate a starting and ending order for a 3-2-2 or 5-3-3 inglenook shunting
puzzle."""

from random import sample, choice, shuffle, randint
import argparse

def get_args():

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='subparser_name')

    parser_322 = subparsers.add_parser('322',
                                       help='Generate for a 322 inglenook')
    parser_322.add_argument('wagons', nargs=6)
    parser_322.set_defaults(func=get_starting_setup_322)

    parser_533 = subparsers.add_parser('533',
                                       help='Generate for a 533 inglenook')
    parser_533.add_argument('wagons', nargs=8)
    parser_533.set_defaults(func=get_starting_setup_533)

    return parser.parse_args()


def get_starting_setup_322(args):
    """Generate the starting positions of the wagons."""

    wagons = args.wagons
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

def get_starting_setup_533(args):
    """Generate the starting positions of the wagons."""

    wagons = args.wagons
    # First decide where the wagons will go
    # The longest siding must start with between 2 and 5 wagons
    num_back = randint(2, 5)

    # If there are two in the long siding, both the short sidings are full
    if num_back == 2:
        num_mid = 3
        num_front = 3

    # If there are three or more wagons in the long siding, then the total
    # number in the short sidings is 8 - num_back
    if num_back >= 3:
        # If there are five wagons in the long siding, mid can have 0 to
        # 3 wagons: minimum of 8 - (num_long + 3)
        # If there are four in the long siding, mid must have at least one
        # wagon in: 8 - (num_long + 3)
        # If there are three in the long siding, mid must have at least two in:
        # 8 - (num_long + 3)

        min_short = 8 - (num_back + 3)
        num_mid = randint(min_short, 3)
        num_front = 8 - num_back - num_mid


    # Randomise the order of the wagons
    shuffle(wagons)

    back = wagons[0:num_back]
    mid = wagons[num_back:num_back+num_mid]
    front = wagons[num_back+num_mid:]

    print("The starting setup is:")
    print("Back: " + str(back))
    print("Middle: " + str(mid))
    print("Front: " + str(front))

def get_target(wagons, inglenook_type):
    """Set the target train to be assembled. Length depends on the type of
    inglenook"""

    if inglenook_type == '322':
        target = sample(wagons, 4)
    else:
        target = sample(wagons, 5)

    print("The target order is: ")
    print(target)

def main():

    args = get_args()

    get_target(args.wagons, args.subparser_name)

    args.func(args)

if __name__ == "__main__":
    main()
