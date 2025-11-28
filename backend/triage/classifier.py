class TriageClassifier:
    """
    Triage and Classification Module.
    Implements the 3-level triage system described in the SRS:

        Level 1  -> Emergency
        Level 2  -> Requires medical consultation
        Level 3  -> Self-care

    Rules derived from SRS sections FREQ-001 to FREQ-005.
    """

    def classify(self, symptom: str) -> str:
        text = symptom.lower()

        # Level 1 — EMERGENCY (SRS: FREQ-003)
        if any(word in text for word in [
            "chest pain",
            "difficulty breathing",
            "severe",
            "unconscious",
            "bleeding"
        ]):
            return "Level 1"

        # Level 2 — MEDICAL CONSULTATION (SRS: FREQ-004)
        if any(word in text for word in [
            "pain",
            "fever",
            "infection",
            "rash",
            "swelling"
        ]):
            return "Level 2"

        # Level 3 — SELF-CARE (SRS: FREQ-005)
        if any(word in text for word in [
            "cough",
            "dry throat",
            "snotty nose"
        ]):
            return "Level 3"

