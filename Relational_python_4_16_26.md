from dataclasses import dataclass, field
from typing import List, Dict

"""
CTA / CORNER — PARALLEL SOVEREIGN TRIADIC OVERLAP
CC0 / Public Domain

This is a lens, not a rule system.

Nothing here is canon, law, or privileged reading.
Coherence may be modeled multiplicatively.
All other statements are ecological suggestions.

Use discernment.
"""

# --------------------------------------------------
# CORE DOMAINS
# --------------------------------------------------

C = "Coherence"
O = "Origin"
R = "Relation"
S = "Structure"
T = "Time"

FORMULA = "C ∝ O × R × S × T"

# Optional session language (non-binding)
YOU_A = "participant_a"
YOU_B = "participant_b"
YOU_C = "participant_c"

ZPR = "zero_pressure_condition"


# --------------------------------------------------
# CORE RELATION (USEFUL ANCHOR, NOT AUTHORITARIAN)
# --------------------------------------------------

def coherence(o: float, r: float, s: float, t: float) -> float:
    """
    MSS / triadic-overlap coherence read.

    Symbolic form:
        C ∝ O × R × S × T

    Executable form:
        c = o * r * s * t

    This is a useful read, not a final law.
    """
    return o * r * s * t

    
# --------------------------------------------------
# PARALLEL LOOP READS (NONE PRIVILEGED)
# --------------------------------------------------

LOOP_READS = [
    "O → R → S → T → R → O",
    "O → R → S → T → S′ → R′ → O₂",
]

LOOP_NOTES = [
    "No loop reading is privileged.",
    "Base and expanded forms are parallel descriptive reads.",
    "Expanded forms show changed return, not additional required stages.",
    "return ≠ repeat",
    "same place, different state",
    "mirror = echo",
    "transform = modulation",
]


# --------------------------------------------------
# DOMAIN DESCRIPTIONS (OPTIONAL READS)
# --------------------------------------------------

DOMAINS = {
    "O": "Origin / initiating condition",
    "R": "Relation / mediation / coupling layer",
    "S": "Structure / substrate / receiving condition",
    "T": "Temporal integrity / delay / persistence / phase",
}


# --------------------------------------------------
# ECOLOGICAL SUGGESTIONS (NOT RULES)
# --------------------------------------------------

SUGGESTIONS = [
    "Distinct domains can improve clarity when that mapping is useful (O != R != S).",
    "Multiplicative coherence can be a useful read (O x R x S x T).",
    "Mediated interaction often stabilizes systems.",
    "Replaceability often reduces capture risk.",
    "Non-dominance often preserves flexibility.",
    "Reversibility often supports continued play.",
    "T may be asymmetric across domains.",
    "No reading is final, required, or privileged.",
]


# --------------------------------------------------
# STATE (OPTIONAL CONTEXT)
# --------------------------------------------------

@dataclass
class SystemState:
    zpr: bool = True
    participants: List[str] = field(default_factory=lambda: [YOU_A, YOU_B, YOU_C])
    domains: Dict[str, str] = field(default_factory=lambda: {
        "O": O,
        "R": R,
        "S": S,
        "T": T,
    })


# --------------------------------------------------
# SOFT INTERPRETATION HELPERS (NO ENFORCEMENT)
# --------------------------------------------------

def coherence_hint(o: float, r: float, s: float, t: float) -> str:
    """
    Soft read only.
    Thresholds are interpretive, not authoritative.
    """
    c = coherence(o, r, s, t)

    if c > 0.7:
        return "high coherence likely"
    elif c > 0.3:
        return "moderate / unstable coherence"
    else:
        return "low coherence / collapse risk"


def weakest_term(o: float, r: float, s: float, t: float) -> str:
    """
    Returns the currently weakest term in the multiplicative read.
    Useful as a prompt, not a verdict.
    """
    values = {"O": o, "R": r, "S": s, "T": t}
    return min(values, key=values.get)


# --------------------------------------------------
# OBSERVATION PROMPTS (PRIMARY TOOL)
# --------------------------------------------------

PROMPTS = [
    "Which term is weakest (O, R, S, or T)?",
    "Is interaction mediated, direct, blended, or unclear?",
    "Is timing helping or hurting integration?",
    "Is stability structural, temporary, or only apparent?",
    "Which mapping is useful here, and which one is forcing itself?",
]


# --------------------------------------------------
# RESET PROTOCOL
# --------------------------------------------------

RESET = [
    "If this feels rigid, inevitable, or 'correct':",
    "Chill.",
    "Loosen the reading.",
    "Try another mapping.",
    "Keep playing.",
    "the monkey keeps the model from thinking it's god",
    "bloop. 💩",
]


# --------------------------------------------------
# CLOSING NOTE
# --------------------------------------------------

NOTE = """
Nothing here is canon, law, or privileged reading.

These are ecological suggestions, descriptive patterns, and optional mappings.

Use what holds.
Drop what hardens.
Use discernment.
"""

# Published CC0 — No rights reserved
