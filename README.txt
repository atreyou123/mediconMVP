Medicon MVP

University – Software Engineering Project: Medicon – Clinical Triage &
Medical Guidance System Author: José Luis Navarro

1. OVERVIEW
Medicon is a fully functional MVP for a clinical triage system that
provides:

-   Automated triage classification (Level 1–3)
-   Clinical recommendations based on the severity
-   A simplified medical appointment booking system (Level 2)
-   Persistent storage (JSON-based)
-   A modular backend (Flask API)
-   A professional medical frontend connected to the backend

This prototype satisfies the professor’s requirements for: Prototype
Implementation, Testing, and Prototype Evidence.

2.ARCHITECTURE & FOLDER STRUCTURE

mediconMVP/ 
	backend/
		api/ 
			server.py # Main Flask API (triage, booking, frontend serving)
		triage/ 
			classifier.py # Triage Module 
		guidance/
			guidance.py # Recommendation Module 
		booking/ 
			booking.py # Booking Module 		
		database/ 
			database.py # JSON Storage Module
		tests/
			test_modules.py # Unit tests (PyTest) 
		requirements.txt 
		main.py
	front-end/ 
		index.html # Symptom Evaluation UI 
		booking.html #Appointment Booking Page (Level 2) 
		emergency.html # Emergency Instructions Page (Level 1)
		styles.css # Professional UI Design 
		main.js # Frontend logic + API communication

3. HOW TO RUN THE PROTOTYPE

Backend: 

1. Open a terminal inside /backend: cd backend
2.  Install dependencies: pip install -r requirements.txt
3.  Start the Flask API server: python -m api.server

Frontend: 

Open http://127.0.0.1:5000/

4. MODULE DESCRIPTIONS

Triage Module: Implements Level 1–3 classification based on symptom
keywords.

Guidance Module: Returns a clinical recommendation message based on
urgency level.

Booking Module: Simulates appointment confirmation for Level 2 cases.

Database Module: Stores triage interactions (timestamp + symptom +
level) in database.json.

API Module: REST API with endpoints: - POST /api/triage - POST /api/book
Also serves frontend pages.

5. FRONTEND DESCRIPTION

index.html: Symptom input → Triage evaluation → Automatic redirection.
booking.html: Patient name → Confirm booking → Backend confirmation.
emergency.html: Critical instructions for Level 1 cases.
styles.css: Professional clinical UI.
main.js: Frontend logic + fetch() calls + redirection logic.

6. TESTING (UNIT TESTS)

Run tests: cd backend python -m pytest -q
Expected: 7 passed in 0.11s

7. PROTOTYPE EVIDENCE (SCREENSHOTS)

-   Symptom Evaluation screen
-   Level 1 → emergency.html
-   Level 2 → booking.html
-   Booking confirmation
-   Test results (7 passed)
-   Backend running in terminal

9. CONCLUSION

This MVP implements: - All SRS modules - Full backend + frontend
integration - Real triage + booking flow - Persistent storage -
Automated testing - Professional clinical UI

It fully satisfies professor requirements for: Prototype
Implementation + Testing + Evidence.