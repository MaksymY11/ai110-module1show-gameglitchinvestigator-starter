from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Bug 2: The hint messages in check_guess are swapped — "Too High" returns
# "Go HIGHER!" and "Too Low" returns "Go LOWER!", which is the opposite of
# what the player needs.  These tests verify the returned message steers the
# player in the correct direction.
def test_too_high_message_says_go_lower():
    _, message = check_guess(60, 50)
    assert "LOWER" in message.upper(), (
        f"Guess too high should say go lower, but got: '{message}'"
    )


def test_too_low_message_says_go_higher():
    _, message = check_guess(40, 50)
    assert "HIGHER" in message.upper(), (
        f"Guess too low should say go higher, but got: '{message}'"
    )
