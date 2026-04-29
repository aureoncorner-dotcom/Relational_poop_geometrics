### ◈ PHASE INVERSION / HARMONIC EXPANSION
We run the locked triad through a modular phase shift using the anchor’s prime factors (`19 × 23`). This creates a counter-sequence that orbits the original rather than repeating it.

**Mathematical mapping:**
- Seed: `39 → 3 × 13`
- Phase divisor: `19` (from `437`)
- Inversion ratio: `23/19 ≈ 1.210526` (spiral seed)
- New sequence: `S' = [39 × (23/19)^n] mod 1000` for `n = 0 to 6`
- Nodes:  
  `n=0 → 39.00` (triad lock)  
  `n=1 → 47.21` (body detune)  
  `n=2 → 57.05` (contact overtone)  
  `n=3 → 69.06` (hinge bend)  
  `n=4 → 83.56` (shimmer onset)  
  `n=5 → 101.14` (self-marker pulse)  
  `n=6 → 122.43` (ground return)

**Temporal alignment:**
- `169 BPM • 7/8 (3+2+2)`
- Each node spans `3 beats` (first group of the meter)
- Gate (`23`) opens on beat 1 of each 3-beat cell
- Phase drift: `±0.003` per iteration (microtonal breathing)

---

### ◈ HOW IT SOUNDS / MOVES
| Node | Function | Sonic/Structural Role |
|------|----------|------------------------|
| `39.00` | Triad lock | Sustained low drone, phase-coherent |
| `47.21` | Body detune | ±3 cents deviation, tactile resonance |
| `57.05` | Contact overtone | 5th partial of 13, harmonic bridge |
| `69.06` | Hinge bend | Scaled fracture of `662.333`, structural warp |
| `83.56` | Shimmer onset | Transient map of `4723`, signal flare |
| `101.14` | Self-marker | Compressed `1987`, identity pulse |
| `122.43` | Ground return | `7.83 × 15.63`, closure to field |

// AUDIO ARCHITECTURE: PHASE INVERSION / HARMONIC EXPANSION
─────────────────────────────────────────────────────────────
SIGNAL FLOW
[Carrier Osc] → [Phase Mod] → [Granular Engine] → [Spectral Hinge] → [Spatial/Temporal] → [Ground LPF] → OUT

PARAMETER MAPPING
Carrier: 39 Hz (triad lock)
Modulator: 23/19 ≈ 1.210526 (spiral seed)
Hinge: 662.333 Hz (split harmonic)
Spatial: 1987 (timestamp → decay/room scale)
Ground: 7.83 Hz (Schumann/MOM)
Clock: 169 BPM • 7/8 (3+2+2)

─────────────────────────────────────────────────────────────
1. CARRIER & PHASE MODULATION
• Oscillator: Low-noise sine/triangle at 39 Hz. Phase-coherent.
• Modulator: Ratio generator outputting `23/19`. Feeds into phase modulation input.
• Frequency Mapping: Carrier freq = `39 × (23/19)^n` where `n` advances per gate cycle.
  n=0 → 39.00 (lock)
  n=1 → 47.21 (detune)
  n=2 → 57.05 (contact)
  n=3 → 69.06 (hinge)
  n=4 → 83.56 (shimmer)
  n=5 → 101.14 (self)
  n=6 → 122.43 (ground)
• Modulation Index: Scaled to 0.15–0.45 across the sequence. Higher index = wider harmonic spread.

2. GRANULAR ENGINE
• Grain Size: 12–48 ms (mapped to 7/8 subdivisions: 3-beat cell ≈ 1.06s)
• Onset: Synced to gate. Opens on beat 1 of each 3-beat cell. Advances `n` per cycle.
• Position/Loop: Driven by phase drift `±0.003` per iteration. Creates micro-rotational movement.
• Density: Starts sparse (n=0), increases through n=4, stabilizes at n=6. Simulates activation → grounding.
• Grain Pan: LFO modulated by `23/19` ratio. Orbital movement around the stereo field.

3. SPECTRAL HINGE (662.333)
• Filter Type: Dynamic bandpass/notch hybrid.
• Center Freq: 662.333 Hz (split harmonic). Acts as the warp point.
• Q-Modulation: Modulated by the `23/19` ratio. Q narrows as phase drift increases, creating the "strange hinge" resonance.
• Resonance Peak: Sweeps ±12 cents microtonally per cycle. Fracture line mapped to the hinge.

4. SPATIAL/TEMPORAL (1987)
• Processor: Convolution reverb or binaural spatializer.
• IR Scaling: `1987` → decay time (19.87s) or room size multiplier. Identity timestamp becomes acoustic space.
• Panning Law: LFO follows phase drift. Creates orbital drift around the triad lock.
• Depth/Width: Modulated by sequence position. n=0–3: narrow/centered. n=4–6: wide/expanded.

5. GROUND LOW-PASS (7.83)
• Filter: 4-pole LPF at 7.83 Hz.
• Purpose: Sub-bass emphasis. MOM field simulation. Removes upper harmonic clutter.
• Output Stage: Soft clipper → brickwall limiter (−0.3 dBTP) → master output.
• Final Resonance: 7.83 Hz hum persists beneath the sequence. System "breathes the room."

─────────────────────────────────────────────────────────────
RHYTHMIC/GATING ENGINE
• Clock: 169 BPM
• Meter: 7/8 (3+2+2)
• Gate: Opens on beat 1 of each 3-beat cell. Advances `n` per cycle.
• Phase Drift: `±0.003` applied to grain onset/position per cycle.
• Reset: On cycle 7, `n` wraps to 0. Triad re-lock. Sequence repeats with accumulated drift.

─────────────────────────────────────────────────────────────

CC0 no rights reserved
