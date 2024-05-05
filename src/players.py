# ------------------------------------------------------------------------------
# players.py -- Module for player information.
#
# May 2024, Tempy Charoenvasnadumrong
# ------------------------------------------------------------------------------
import trueskill

from dataclasses import dataclass


@dataclass
class Attributes:
    """
    A dataclass representing each player's attribute rating.

    :shooting:
        A player's shooting ability.

    :dribbling:
        A player's dribbling ability.

    :passing:
        A player's passing ability.

    :tackling:
        A player's tackling ability.

    :fitness:
        A player's fitness.

    :goalkeeping:
        A player's goalkeeping ability.

    """

    shooting: trueskill.Rating
    dribbling: trueskill.Rating
    passing: trueskill.Rating
    tackling: trueskill.Rating
    fitness: trueskill.Rating
    goalkeeping: trueskill.Rating

    @classmethod
    def from_values(cls, values: dict[str, float]) -> "Attributes":
        """Create an Attributes class from the passed-in values."""
        return cls(
            shooting=trueskill.Rating(
                mu=values.get("shooting", 25), sigma=values.get("shooting_sigma", 8.333)
            ),
            dribbling=trueskill.Rating(
                mu=values.get("dribbling", 25),
                sigma=values.get("dribbling_sigma", 8.333),
            ),
            passing=trueskill.Rating(
                mu=values.get("passing", 25), sigma=values.get("passing_sigma", 8.333)
            ),
            tackling=trueskill.Rating(
                mu=values.get("tackling", 25), sigma=values.get("tackling_sigma", 8.333)
            ),
            fitness=trueskill.Rating(
                mu=values.get("fitness", 25), sigma=values.get("fitness_sigma", 8.333)
            ),
            goalkeeping=trueskill.Rating(
                mu=values.get("goalkeeping", 25),
                sigma=values.get("goalkeeping_sigma", 8.333),
            ),
        )
    


@dataclass
class Player:
    """
    A dataclass representing a player.

    :name:
        The player's name.

    :attributes:
        An 'Attributes' object, representing a player's attributes.

    :form:
        A player's form.

    """

    name: str
    attributes: Attributes
    form: int

    def get_overall_rating(self) -> float:
        """
        Get a player's overall rating, taking form into account.
        """
        total_rating = sum(
            self.attributes.__dict__[attribute].mu
            for attribute in self.attributes.__dict__.keys()
        )
        # Multiply the overall rating by the form factor
        return (total_rating / len(self.attributes.__dict__.keys())) * (
            1 + 0.1 * self.form
        )  # Adjust the form factor as needed
