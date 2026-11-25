# House map
#             |----------|-----------|
# (unlock w/  |          | (unlock w/|
#     Key 2)  |          |   Key 1)  |
#     Outside | Bedroom  X Bathroom  |
#             |          |   *Key 2* |
#   |----X----|---    ---|-----------|
#   |         |          |
#   | Kitchen   Hallway  |
#   |         |   *Key 1*|
#   |---------|----------|

rooms = {
    "Bedroom": {"pathways": {"d": "Bathroom", "s": "Hallway"}, "open_with": ""},
    "Hallway": {"pathways": {"w": "Bedroom", "a": "Kitchen"}, "open_with": ""},
    "Bathroom": {"pathways": {"a": "Bedroom"}, "open_with": "Key 1"},
    "Kitchen": {"pathways": {"d": "Hallway", "w": "Outside"}, "open_with": ""},
    "Outside": {"pathways": {"s": "Kitchen"}, "open_with": "Key 2"},
}

pickable_objects = {
    "Key 1": {"location": "Hallway", "picked": False},
    "Key 2": {"location": "Bathroom", "picked": False}
}

START_LOCATION = "Bedroom"


def print_location(location: str) -> None:
    """
    Print the description of the current location.

    Update this function to check whether the room exists in the rooms dictionary.

    If the room exists, print the current location (e.g., "You are in the Kitchen.")

    Otherwise, print "Unknown location."
    """
    if location in rooms:
        print(f"You are in the {location}.")
    else:
        print("Unknown location.")


def get_directions(location: str) -> dict[str, str]:
    """
    Return possible directions to move from the current location.

    Update this function to read the pathways from the dictionary and return
    the pathways dictionary without printing.

    Example return value: {'d': 'Hallway', 'w': 'Outside'}

    If the room is unknown, return an empty dict: {}
    """
    return rooms.get(location, {}).get("pathways", {})


def find_room_by_direction(location: str, direction: str) -> str:
    """
    Determine the new location based on the current location and direction.

    Modify this function to search the dictionary for the next room to navigate to based
    on the current location and direction provided.

    Return the new location after moving in the specified direction.

    If the current location is unknown, print "Unknown location." and return the
    original location. If the direction is invalid, print an error message and
    return the current location.
    """
    if location not in rooms:
        print("Unknown location.")
        return location

    pathways = rooms.get(location, {}).get("pathways", {})
    if direction in pathways:
        return pathways[direction]
    else:
        print("Invalid direction. Try again.")
        return location


def has_key_for_room(room_id: str) -> bool:
    """
    Check if the player has the key to enter a specified room.

    Modify this function to consult the rooms and pickable_objects dictionaries to
    determine whether the destination room requires a key and if that key has been picked.

    Return True if the player can enter the room, False otherwise.
    """
    if room_id not in rooms:
        return False

    required_key = rooms.get(room_id, {}).get("open_with", "")
