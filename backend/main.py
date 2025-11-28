from ui.interface import ConsoleUI
from triage.classifier import TriageClassifier
from guidance.guidance import GuidanceModule
from booking.booking import BookingModule
from database.database import DatabaseModule

ui = ConsoleUI()
triage = TriageClassifier()
guidance = GuidanceModule()
booking = BookingModule()
db = DatabaseModule()

symptom = ui.get_user_input()

level = triage.classify(symptom)
ui.show(f"Urgency level: {level}")

recommendation = guidance.get_recommendation(level)
ui.show(recommendation)

db.save({"symptom": symptom, "level": level})

if level == "Level 2":
    name = input("Enter your name to book an appointment: ")
    booking_result = booking.book(name, symptom)
    ui.show(booking_result)
    db.save({"symptom": symptom, "level": level, "name": name})
