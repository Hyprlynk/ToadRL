import components
from components.ai import *
from components import consumable
from components.body import Body
from components.inventory import Inventory
from components.talker import *
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    body=Body(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
    talker=Silent()
)

grub = Actor(
    char="g",
    color=(63, 127, 63),
    name="Grub",
    ai_cls=HostileEnemy,
    body=Body(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    talker=Silent()
)

rabid_vole = Actor(
    char="V",
    color=(0, 127, 0),
    name="Rabid Vole",
    ai_cls=HostileEnemy,
    body=Body(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0),
    talker=Silent()
)

toad = Actor(
    char="t",
    color=(209, 141, 23),
    name="Toad",
    ai_cls=PassiveNPC,
    body=Body(hp=13, defense=1, power=2),
    inventory=Inventory(capacity=3),
    talker=Talker(toad_exclamations)
)

seedcake = Item(
    char="#",
    color=(127, 0, 255),
    name="Seedcake",
    consumable=consumable.HealingConsumable(amount=4),
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

molotov = Item(
    char="~",
    color=(255, 0, 0),
    name="Molotov Cocktail",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)