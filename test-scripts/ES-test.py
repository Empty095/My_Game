from GameEffects.effects import Effect
from entities.Entity import Entity

Entity = Entity(hp=100, defender=100, damage=200)
Entity.effects.append(Effect(Entity, "bleeding"))
Entity.effects.append(Effect(Entity, "bleeding"))
Entity.effects.append(Effect(Entity, "bleeding"))

counter = 10
while counter >= 0:
    for x in Entity.effects:
        x.using()


    print(f"Характеристики тестовой сущности:"
          f"hp: {Entity.hp} "
          f"defender: {Entity.defender} "
          f"damage: {Entity.damage}")

    counter -= 1