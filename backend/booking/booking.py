class BookingModule:
    """
    Consultation Booking Module.

    Simulates appointment booking as described in SRS section 4.3.
    For the prototype, we assume a booking is always available.
    """

    def book(self, name: str, symptom: str) -> str:
        return (
            f"Appointment successfully booked for {name}. "
            f"Reason for consultation: '{symptom}'."
        )
