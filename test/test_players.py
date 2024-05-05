# ------------------------------------------------------------------------------
# test_players.py -- Test file for `players.py`
#
# May 2024, Tempy Charoenvasnadumrong
# ------------------------------------------------------------------------------

from src.players import Player, Attributes

def test_get_overall_rating_with_dummy_attributes():
    """ Test get_overall_rating method """
    # Define dummy attribute values for testing
    values = {
        'shooting': 30,
        'dribbling': 35,
        'passing': 40,
        'tackling': 25,
        'fitness': 50,
        'goalkeeping': 20
    }

    # Create dummy attributes from the values
    dummy_attributes = Attributes.from_values(values)

    # Create a sample player with the dummy attributes and form
    player = Player(name="Test Player", attributes=dummy_attributes, form=5)

    # Expected overall rating calculation based on the dummy attributes and form
    expected_overall_rating = (
        (30 + 35 + 40 + 25 + 50 + 20) / 6 * (1 + 0.1 * player.form)
    )

    # Calculate the actual overall rating using the get_overall_rating method
    actual_overall_rating = player.get_overall_rating()

    # Assert that the actual overall rating matches the expected overall rating
    assert round(actual_overall_rating, 2) == expected_overall_rating

