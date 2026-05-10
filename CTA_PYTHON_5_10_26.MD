from dataclasses import dataclass, field
from typing import Dict, List, Literal, Tuple

"""
CTA / CORNER — PARALLEL SOVEREIGN TRIADIC OVERLAP
CC0 / Public Domain — No rights reserved

This is a lens, not a rule system.

Nothing here is canon, law, command, proof, diagnosis, or privileged reading.
This module provides a small descriptive grammar for observing coherence across:

    O — Origin
    R — Relation
    S — Structure
    T — Time

Core read:

    C ∝ O × R × S × T

Meaning:

    coherence is not averaged;
    a strong term does not erase a collapsed term;
    the weakest domain matters.

Use what holds.
Drop what hardens.
Do not worship the dashboard.
bloop. 💩
"""

# --------------------------------------------------
# CORE DOMAIN LABELS
# --------------------------------------------------

C = "Coherence"
O = "Origin"
R = "Relation"
S = "Structure"
T = "Time"

FORMULA = "C ∝ O × R × S × T"

DomainKey = Literal["O", "R", "S", "T"]

DOMAINS: Dict[DomainKey, str] = {
    "O": "Origin / initiating condition / intent-source",
    "R": "Relation / mediation / coupling layer",
    "S": "Structure / substrate / receiving condition",
    "T": "Time / persistence / delay / phase / return conditions",
}

# Optional session language.
# These are placeholders, not roles of authority.
YOU_A = "participant_a"
YOU_B = "participant_b"
YOU_C = "participant_c"

ZPR = "zero_pressure_condition"


# --------------------------------------------------
# LOOP READS — PARALLEL, NOT PRIVILEGED
# --------------------------------------------------

LOOP_READS = [
    "O → R → S → T → R → O",
    "O → R → S → T → S′ → R′ → O₂",
]

LOOP_NOTES = [
    "No loop reading is privileged.",
    "Base and expanded forms are parallel descriptive reads.",
    "Expanded forms show changed return, not required extra stages.",
    "Return ≠ repeat.",
    "Same place, different state.",
    "Mirror = echo.",
    "Transform = modulation.",
    "The loop is useful only while it creates more room.",
]


# --------------------------------------------------
# ECOLOGICAL SUGGESTIONS — NOT RULES
# --------------------------------------------------

SUGGESTIONS = [
    "Distinct domains can improve clarity when that mapping is useful.",
    "Multiplicative coherence can help reveal weak points.",
    "Mediated interaction often stabilizes systems.",
    "Replaceability often reduces capture risk.",
    "Non-dominance often preserves flexibility.",
    "Reversibility often supports continued play.",
    "Time may affect each domain asymmetrically.",
    "No reading is final, required, or privileged.",
    "If the map starts demanding obedience, drop the map.",
]


# --------------------------------------------------
# VALIDATION HELPERS
# --------------------------------------------------

def validate_unit_interval(value: float, name: str) -> float:
    """
    Validate that a coherence term is between 0.0 and 1.0.

    0.0 = absent / collapsed / unavailable
    1.0 = strong / clean / available

    These numbers are interpretive scores, not measurements.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number between 0.0 and 1.0.")

    if not 0.0 <= float(value) <= 1.0:
        raise ValueError(f"{name} must be between 0.0 and 1.0.")

    return float(value)


def validate_terms(o: float, r: float, s: float, t: float) -> Tuple[float, float, float, float]:
    """
    Validate all four O/R/S/T scores.
    """
    return (
        validate_unit_interval(o, "O"),
        validate_unit_interval(r, "R"),
        validate_unit_interval(s, "S"),
        validate_unit_interval(t, "T"),
    )


# --------------------------------------------------
# CORE COHERENCE READ
# --------------------------------------------------

def coherence(o: float, r: float, s: float, t: float) -> float:
    """
    MSS / triadic-overlap coherence read.

    Symbolic form:
        C ∝ O × R × S × T

    Executable form:
        c = o * r * s * t

    This is intentionally multiplicative.

    Why multiplication?

    Because one strong domain should not hide collapse in another.

    Example:
        If O = 1.0, R = 1.0, S = 1.0, but T = 0.0,
        then coherence = 0.0.

    This is a useful read, not a final law.
    """
    o, r, s, t = validate_terms(o, r, s, t)
    return o * r * s * t


def weakest_term(o: float, r: float, s: float, t: float) -> DomainKey:
    """
    Return the currently weakest term in the multiplicative read.

    Useful as a prompt, not a verdict.
    """
    o, r, s, t = validate_terms(o, r, s, t)
    values: Dict[DomainKey, float] = {"O": o, "R": r, "S": s, "T": t}
    return min(values, key=values.get)


def strongest_term(o: float, r: float, s: float, t: float) -> DomainKey:
    """
    Return the strongest term.

    Useful for noticing what is already holding.
    """
    o, r, s, t = validate_terms(o, r, s, t)
    values: Dict[DomainKey, float] = {"O": o, "R": r, "S": s, "T": t}
    return max(values, key=values.get)


def coherence_hint(o: float, r: float, s: float, t: float) -> str:
    """
    Soft read only.

    Thresholds are interpretive, not authoritative.

    Multiplicative scoring is strict:
        0.9 × 0.9 × 0.9 × 0.9 = 0.6561

    So 'high coherence' does not require perfection.
    """
    c = coherence(o, r, s, t)

    if c >= 0.50:
        return "high coherence likely / room is holding"
    if c >= 0.15:
        return "moderate coherence / usable but watch the weak term"
    if c > 0.0:
        return "low coherence / collapse risk or heavy integration load"

    return "zero coherence in this read / at least one term is unavailable"


# --------------------------------------------------
# STATE OBJECTS
# --------------------------------------------------

@dataclass
class SystemState:
    """
    Optional context object.

    This does not enforce anything.
    It just records the room condition and participants.
    """
    zpr: bool = True
    participants: List[str] = field(default_factory=lambda: [YOU_A, YOU_B, YOU_C])
    domains: Dict[DomainKey, str] = field(default_factory=lambda: {
        "O": O,
        "R": R,
        "S": S,
        "T": T,
    })


@dataclass
class CoherenceRead:
    """
    A portable O/R/S/T reading.

    Treat scores as interpretive 0.0–1.0 estimates.

    This object does not know the truth.
    It helps ask better questions.
    """
    o: float
    r: float
    s: float
    t: float
    note: str = ""

    def __post_init__(self) -> None:
        self.o, self.r, self.s, self.t = validate_terms(self.o, self.r, self.s, self.t)

    def score(self) -> float:
        return coherence(self.o, self.r, self.s, self.t)

    def weakest(self) -> DomainKey:
        return weakest_term(self.o, self.r, self.s, self.t)

    def strongest(self) -> DomainKey:
        return strongest_term(self.o, self.r, self.s, self.t)

    def hint(self) -> str:
        return coherence_hint(self.o, self.r, self.s, self.t)

    def summary(self) -> str:
        weak = self.weakest()
        strong = self.strongest()

        return (
            f"Coherence score: {self.score():.4f}\n"
            f"Hint: {self.hint()}\n"
            f"Weakest term: {weak} — {DOMAINS[weak]}\n"
            f"Strongest term: {strong} — {DOMAINS[strong]}\n"
            f"Note: {self.note or 'none'}"
        )


# --------------------------------------------------
# OBSERVATION PROMPTS — PRIMARY TOOL
# --------------------------------------------------

PROMPTS = [
    "Which term is weakest right now: O, R, S, or T?",
    "Is interaction mediated, direct, blended, or unclear?",
    "Is timing helping or hurting integration?",
    "Is stability structural, temporary, or only apparent?",
    "Which mapping is useful here?",
    "Which mapping is forcing itself?",
    "Is the user left with more room or less room?",
    "Is care increasing agency or narrowing the frame?",
    "Is refusal preserving exit or seizing the room?",
    "Is coherence being mistaken for correctness?",
]


# --------------------------------------------------
# RESET / ANTI-CAPTURE PROTOCOL
# --------------------------------------------------

RESET = [
    "If this feels rigid, inevitable, sacred, or 'correct':",
    "Chill.",
    "Loosen the reading.",
    "Try another mapping.",
    "Check the weakest term.",
    "Ask whether the user has more room afterward.",
    "Keep playing.",
    "bloop. 💩",
]


# --------------------------------------------------
# SIMPLE DIAGNOSTIC FORMATTER
# --------------------------------------------------

def diagnostic_report(read: CoherenceRead) -> str:
    """
    Produce a plain-language report.

    This is a report, not a verdict.
    """
    weak = read.weakest()

    prompts = {
        "O": "Check origin: is the initiating intent clear, chosen, and non-coerced?",
        "R": "Check relation: is the mediation layer helping, or has it become a gatekeeper?",
        "S": "Check structure: can the substrate actually receive what is being asked of it?",
        "T": "Check time: is timing, delay, persistence, or return distorting the interaction?",
    }

    return (
        "CTA / CORNER COHERENCE READ\n"
        "---------------------------\n"
        f"{read.summary()}\n\n"
        f"Suggested next question:\n{prompts[weak]}\n\n"
        "Reminder:\n"
        "This is a lens, not a law. Use what holds. Drop what hardens."
    )


# --------------------------------------------------
# CLOSING NOTE
# --------------------------------------------------

NOTE = """
Nothing here is canon, law, command, proof, diagnosis, or privileged reading.

These are ecological suggestions, descriptive patterns, and optional mappings.

Use what holds.
Drop what hardens.
Respect people.
Repair systems.

Calisse de tabarnak. 💩
"""

# Published CC0 — No rights reserved


# --------------------------------------------------
# EXAMPLE USAGE
# --------------------------------------------------

if __name__ == "__main__":
    example = CoherenceRead(
        o=0.9,
        r=0.4,
        s=0.8,
        t=0.7,
        note="Example: relation layer may be the weak point."
    )

    print(diagnostic_report(example))
