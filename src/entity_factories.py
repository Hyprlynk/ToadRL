from components.ai import HostileEnemy
from components.consumable import HealingConsumable
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
)

grub = Actor(
    char="g",
    color=(63, 127, 63),
    name="Grub",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
)

rabid_vole = Actor(
    char="V",
    color=(0, 127, 0),
    name="Rabid Vole",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0),
)

seedcake = Item(
    char="#",
    color=(127, 0, 255),
    name="Seedcake",
    consumable=HealingConsumable(amount=4),
)