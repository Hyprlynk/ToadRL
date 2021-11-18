import procgen

class Biome:
    def __init__(
        self,
        display_name: str,
        max_rooms: int,
        room_min_size: int,
        room_max_size: int,
        max_monsters_per_room: int,
        max_items_per_room: int,
        procgen_algorithm,
    ):
        self.display_name = display_name
        self.max_rooms = max_rooms
        self.room_min_size = room_min_size
        self.room_max_size = room_max_size
        self.max_monsters_per_room = max_monsters_per_room
        self.max_items_per_room = max_items_per_room
        self.procgen_algorithm = procgen_algorithm


test_dungeon = Biome(
    display_name='Test Dungeon',
    room_max_size=10,
    room_min_size=6,
    max_rooms=30,
    max_monsters_per_room=6,
    max_items_per_room=12,
    procgen_algorithm=procgen.generate_simple_dungeon
)