import pytest

from triage.classifier import TriageClassifier
from guidance.guidance import GuidanceModule
from booking.booking import BookingModule

@pytest.fixture
def triage():
    return TriageClassifier()

@pytest.fixture
def guidance():
    return GuidanceModule()

@pytest.fixture
def booking():
    return BookingModule()


def test_triage_level1(triage):
    """Symptoms indicating emergency must return Level 1."""
    result = triage.classify("severe chest pain and difficulty breathing")
    assert result == "Level 1"


def test_triage_level2(triage):
    """Moderate symptoms (pain/fever) should return Level 2."""
    result = triage.classify("mild arm pain")
    assert result == "Level 2"


def test_triage_level3(triage):
    """Mild symptoms should return Level 3."""
    result = triage.classify("small cough")
    assert result == "Level 3"


def test_guidance_level1(guidance):
    """Check correct emergency instructions."""
    message = guidance.get_recommendation("Level 1")
    assert "emergency" in message.lower()


def test_guidance_level2(guidance):
    """Check correct consultation instructions."""
    message = guidance.get_recommendation("Level 2")
    assert "consult" in message.lower() or "appointment" in message.lower()


def test_guidance_level3(guidance):
    """Check self-care advice."""
    message = guidance.get_recommendation("Level 3")
    assert "self-care" in message.lower() or "mild" in message.lower()


def test_booking(booking):
    """Booking should include the name and symptom in confirmation message."""
    name = "John Doe"
    symptom = "fever"
    result = booking.book(name, symptom)

    assert name in result
    assert symptom in result
