import random
from collections import defaultdict

PIZZA_OPTIONS = {'margherita': ['tomato sauce 🥫', 'mozzarella  🧀',
                                'tomatoes 🍅'],
                 'pepperoni': ['tomato sauce 🥫', 'mozzarella 🧀',
                               'pepperoni 🍖'],
                 'hawaiian': ['tomato sauce 🥫', 'mozzarella 🧀',
                              'chicken 🍗', 'pineapples 🍍']}


def log(text_without_time: str):
    """Prints text with random time inserted, then runs a function."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(text_without_time.format(random.randrange(10, 30)))
            func(*args, **kwargs)
        return wrapper
    return decorator


class Pizza:
    """
    Contains information about pizza.
    Pizza type should be one of PIZZA_OPTIONS.
    """

    def __init__(self, name: str = 'pepperoni', size: str = 'L'):
        self.name = name
        self.size = size
        self.ingredients = PIZZA_OPTIONS[name]

    def dict(self) -> dict[str: int]:
        """Returns a dict with required ingredients and amounts."""

        return {i: 1 for i in self.ingredients}

    @log('👩🏻‍🍳 Cooking started. Estimated time: {} seconds.')
    def bake(self) -> None:
        """Adds all the ingredients, each ingredient takes random time."""

        interval = defaultdict()
        for ingredient in self.ingredients:
            interval[ingredient] = random.randrange(2, 7)
            print(f'Added {ingredient} ({interval[ingredient]} seconds).')
        print(f'{self.name.capitalize()} {self.size} is ready. '
              f'Total time: {sum(interval.values())} seconds.')

    @log('🚚 Delivered in {} seconds.')
    def delivery(self) -> None:
        """Delivers pizza."""
        pass
