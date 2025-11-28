async function evaluateSymptom() {
    const symptom = document.getElementById("symptomInput").value;

    if (!symptom) {
        alert("Please enter a symptom.");
        return;
    }

    const response = await fetch("http://127.0.0.1:5000/api/triage", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symptom })
    });

    const data = await response.json();
    const level = data.level;
    const guidance = data.recommendation;

    updateUI(level, guidance, symptom);
}

function updateUI(level, guidance, symptom) {

    // Save for booking page
    localStorage.setItem("lastSymptom", symptom);

    if (level === "Level 1") {
        alert("⚠ Emergency detected! Redirecting to emergency instructions...");
        window.location.href = "emergency.html";
        return;
    }

    if (level === "Level 2") {
        alert("This case requires a medical consultation. Redirecting to booking...");
        window.location.href = "booking.html";
        return;
    }

    if (level === "Level 3") {
        alert("Your symptoms appear mild. Recommended self-care: rest, hydration, and monitor symptoms. Seek help if symptoms worsen.");
    }

    // Level 3 (self-care)
    const resultDiv = document.getElementById("result");
    const levelSpan = document.getElementById("level");
    const guidanceP = document.getElementById("guidance");

    resultDiv.classList.remove("level1", "level2", "level3");
    resultDiv.classList.add("level3");

    levelSpan.textContent = level;
    guidanceP.textContent = guidance;

    resultDiv.classList.remove("hidden");
}


async function confirmBooking() {
    const name = document.getElementById("nameInput").value;
    const symptom = localStorage.getItem("lastSymptom");

    if (!name) {
        alert("Please enter your name.");
        return;
    }

    const response = await fetch("http://127.0.0.1:5000/api/book", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, symptom })
    });

    const data = await response.json();
    document.getElementById("bookingResult").textContent = data.message;
}

