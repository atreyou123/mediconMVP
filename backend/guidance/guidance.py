class GuidanceModule:
    """
    AI Guidance and Recommendation Module.

    Provides textual recommendations based on the triage level,
    according to the SRS:

        - Level 1: advise emergency services
        - Level 2: guide to medical consultation / booking
        - Level 3: provide self-care recommendations
    """

    def get_recommendation(self, level: str) -> str:
        if level == "Level 1":
            return (
                "Emergency detected. Call emergency medical services immediately "
                "and do not delay seeking in-person care."
            )

        if level == "Level 2":
            return (
                "A medical consultation is recommended. Please book an appointment "
                "with a doctor or local clinic as soon as possible."
            )

        if level == "Level 3":
            return (
                "Your symptoms appear compatible with a mild condition. "
                "Follow self-care advice such as rest, hydration and monitoring. "
                "If symptoms worsen, seek medical attention."
            )

        # Fallback (should not happen in normal flow)
        return "No recommendation available for the provided level."
