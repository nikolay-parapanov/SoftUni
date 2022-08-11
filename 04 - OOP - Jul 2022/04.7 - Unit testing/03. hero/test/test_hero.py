from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Warrior", 10, 100, 50)
        self.enemy = Hero('Defender', 1, 100, 50)

    def test_hero_init(self):
        username = "username 1"
        level = 10
        health = 100
        damage = 50
        hero = Hero(username, level, health, damage)

        self.assertEqual(username, hero.username)
        self.assertEqual(level, hero.level)
        self.assertEqual(health, hero.health)
        self.assertEqual(damage, hero.damage)

    def test_if_hero_returns_proper_string(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"
        actual_result = str(self.hero)

        self.assertEqual(expected_result, actual_result)

    def test_battle_raises_when_hero_attacks_himself(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(context.exception))

    def test_battle_raises_when_hero_is_death(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle_raises_when_enemy_is_death(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(context.exception))

    def test_battle_returns_draw_when_both_heros_are_death(self):
        actual_result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", actual_result)
        self.assertEqual(-400, self.hero.health)
        self.assertEqual(-400, self.enemy.health)

    def test_battle_returns_hero_won(self):
        enemy = Hero('Defender', 1, 100, 50)
        result = self.hero.battle(enemy)
        self.assertEqual('You win', result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(55, self.hero.damage)
        self.assertEqual(-400, enemy.health)

    def test_battle_returns_hero_lost(self):
        hero = Hero('Warrior',1, 100, 20 )
        enemy = Hero('Defender', 1, 100, 30)
        result = hero.battle(enemy)
        self.assertEqual('You lose', result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(85, enemy.health)
        self.assertEqual(35, enemy.damage)
        self.assertEqual(70, hero.health)


if __name__ == "__main__":
    main()
