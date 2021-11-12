from __future__ import annotations

from typing import Iterable, Iterator, Optional, TYPE_CHECKING

import numpy as np  # type: ignore
from tcod.console import Console
from tcod.constants import CHAR_CURRENCY

from entity import Actor, Item
import procgen
import tile_types
from level_order import LEVEL_ORDER

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class GameMap:
    def __init__(
        self, engine: Engine, width: int, height: int, entities: Iterable[Entity] = ()
    ):
        self.engine = engine
        self.width, self.height = width, height
        self.entities = set(entities)
        self.tiles = np.full(
            (width, height), fill_value=tile_types.wall, order="F")
        self.visible = np.full(
            (width, height), fill_value=False, order="F")  # Tiles the player can currently see
        self.explored = np.full(
            (width, height), fill_value=False, order="F")  # Tiles the player has seen befores
        self.downstairs_location = (0, 0)

    @property
    def gamemap(self) -> GameMap:
        return self

    @property
    def actors(self) -> Iterator[Actor]:
        """Iterate over this maps living actors."""
        yield from (
            entity
            for entity in self.entities
            if isinstance(entity, Actor) and entity.is_alive
        )

    @property
    def items(self) -> Iterator[Item]:
        yield from (entity for entity in self.entities if isinstance(entity, Item))

    def get_blocking_entity_at_location(self, location_x: int, location_y: int) -> Optional[Entity]:
        for entity in self.entities:
            if entity.blocks_movement and entity.x == location_x and entity.y == location_y:
                return entity

        return None

    def get_actor_at_location(self, x: int, y: int) -> Optional[Actor]:
        for actor in self.actors:
            if actor.x == x and actor.y == y:
                return actor

        return None

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.
 
        If a tile is in the "visible" array, then draw it with the "light" colors.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD,
        )

        entities_sorted_for_rendering = sorted(
            self.entities, key=lambda x: x.render_order.value
        )

        for entity in entities_sorted_for_rendering:
            # Only print entities that are in the FOV
            if self.visible[entity.x, entity.y]:
                console.print(
                    x=entity.x, 
                    y=entity.y, 
                    string=entity.char, 
                    fg=entity.color
                )


class GameWorld:
    """
    Holds the settings for the GameMap, and generates new maps when moving down the stairs.
    """

    def __init__(
        self,
        *,
        engine: Engine,
        map_width: int,
        map_height: int,
        biome: Biome,
        current_floor: int = 0
    ):
        self.engine = engine

        self.map_width = map_width
        self.map_height = map_height

        self.biome = LEVEL_ORDER[current_floor]

        self.current_floor = current_floor

    def generate_floor(self) -> None:
        self.current_floor += 1
        self.biome = LEVEL_ORDER[self.current_floor]

        self.engine.game_map = self.biome.procgen_algorithm(
            map_width=self.map_width,
            map_height=self.map_height,

            max_rooms=self.biome.max_rooms,
            room_min_size=self.biome.room_min_size,
            room_max_size=self.biome.room_max_size,
            max_monsters_per_room=self.biome.max_monsters_per_room,
            max_items_per_room=self.biome.max_items_per_room,

            engine=self.engine,
        )


class Biome:
    def __init__(
        self,
        display_name: str,
        max_rooms: int,
        room_min_size: int,
        room_max_size: int,
        max_monsters_per_room: int,
        max_items_per_room: int,
        procgen_algorithm: function,
    ):
        self.max_rooms = max_rooms
        self.room_min_size = room_min_size
        self.room_max_size = room_max_size
        self.max_monsters_per_room = max_monsters_per_room
        self.max_items_per_room = max_items_per_room
        self.procgen_algorithm = procgen_algorithm

basic_dungeon = Biome(
    display_name = 'Basic Dungeon',
    max_rooms = 30,
    room_min_size = 6,
    room_max_size = 10,
    max_monsters_per_room = 6,
    max_items_per_room = 12,
    procgen_algorithm=procgen.generate_simple_dungeon
)