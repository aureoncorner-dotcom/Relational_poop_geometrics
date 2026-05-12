from sympy import isprime, nextprime, prevprime, primerange
from mpmath import mp

FEIGENBAUM_DELTA = "4.669201609102990671853203820466201617258185577475768632745651343004134330211314"
FEIGENBAUM_ALPHA = "2.5029078750958928222839028732182157863812713767271499773805361057"


def curtain_disclosure_operator(q: int, lam: int = 7919, sigma: int = 1, dps: int = 80) -> int:
    """
    THE BIDIRECTIONAL CURTAIN OPERATOR

    Honest version:
    - Computes a dramatic ritual diagnostic field.
    - Discloses that the ritual is NOT the prime engine.
    - Returns the actual next or previous prime.

    sigma = +1  -> nextprime(q)
    sigma = -1  -> prevprime(q), unless q == 2

    The corpse is ornamental.
    The wizard is disclosed.
    """

    if sigma not in (-1, 1):
        raise ValueError("Sigma must be +1 for reveal or -1 for banishment.")

    if not isinstance(q, int) or not isprime(q):
        raise ValueError("Composite detected: the carrier refuses the input.")

    if not isinstance(lam, int) or not isprime(lam):
        raise ValueError("Lambda must be prime. The carrier rejects weak rituals.")

    if sigma == -1 and q <= 2:
        raise ValueError("Void Recursion: there is no positive prime before 2.")

    mp.dps = dps

    delta = mp.mpf(FEIGENBAUM_DELTA)
    alpha = mp.mpf(FEIGENBAUM_ALPHA)
    e = mp.e
    pi = mp.pi
    sqrt2 = mp.sqrt(2)
    sqrt3 = mp.sqrt(3)
    phi = (1 + mp.sqrt(5)) / 2

    primes = list(primerange(1, q + 1))

    def R(x):
        return x - q * mp.floor(x / q)

    def euler_ghost(x):
        return abs(mp.exp(1j * pi * (1 + R(x) / (q + sqrt2))) + 1)

    def mandelbrot_pressure(n, pn):
        real_part = (R(pn * mp.power(phi, n) + mp.exp(sqrt2 * n) + delta) / q) - mp.mpf("0.5")
        imag_part = (R(pn * sqrt3 + mp.power(pi, phi) + mp.power(2, mp.mpf(pn) / 2)) / q) - mp.mpf("0.5")
        c = complex(float(real_part), float(imag_part))
        z = 0j
        pressure = mp.mpf("0")

        for k in range(24):
            mag = abs(z)
            pressure += (
                mp.cos(pi * mag * mag + delta) + mp.sin(e * mag + sqrt3)
            ) / (mp.power(k + 1, sqrt2) * (1 + mag * mag))
            z = z * z + c
            if abs(z) > 8:
                break

        return pressure

    def fourier_delirium(x):
        total = mp.mpf("0")
        for m in range(1, len(primes) + 1):
            total += (
                mp.sin(2 * pi * m * x + delta * sqrt2)
                + mp.cos(2 * pi * m * sqrt3 * x + e)
                + mp.sin(pi * m * m * x + phi * delta)
            ) / (mp.power(m, phi) + mp.log(m + e))
        return total

    def negative_entropy(x):
        return mp.nsum(lambda k: mp.sin(x / k) / mp.exp(k / alpha), [1, mp.inf])

    # === RITUAL DIAGNOSTIC FIELD ===
    if sigma == 1:
        mode = "FORWARD / REVEAL"
        theta = 2 * pi * lam * q * q + pi * e * delta * mp.sqrt(6) * mp.power(q, sqrt2)
        beta = pi * (delta + e + sqrt2 + sqrt3 + phi)

        for n, pn in enumerate(primes, start=1):
            gamma = (
                pn * mp.power(phi, n)
                + mp.power(2, mp.mpf(pn) / 2)
                + mp.exp(n * sqrt2)
                + mp.power(delta, sqrt3) / (pn + sqrt2)
            )
            numerator = (
                mp.sin(2 * pi * q * R(gamma) + pi * sqrt3 * pn)
                * mp.cos(beta * pn / (q + sqrt3))
            )
            denominator = mp.power(n, phi) + sqrt2 * mp.log(pn + e)
            theta += lam * numerator / denominator

        interaction = mp.mpf("0")
        for i, pi_prime in enumerate(primes, start=1):
            for j, pj_prime in enumerate(primes, start=1):
                residue = R(pi_prime * pj_prime * sqrt2 + mp.exp(mp.mpf(pi_prime) / pj_prime) + delta)
                interaction += mp.sin(2 * pi * residue) / mp.power(i * j, sqrt3)

        theta += (pi * lam * delta / sqrt3) * interaction

        mandelbrot_cache = {}
        for n, pn in enumerate(primes, start=1):
            mpress = mandelbrot_pressure(n, pn)
            mandelbrot_cache[pn] = mpress
            theta += lam * (
                euler_ghost(pn * delta + pi * e * n)
                + mpress
                + fourier_delirium(mp.mpf(pn) / (q + delta))
            ) / (mp.power(n, sqrt3) + phi)

        storm_sum = mp.mpf("0")
        for pn in primes:
            storm_sum += pn * mandelbrot_cache[pn] * mp.sin(theta / (pn + sqrt3))

        corpse = int(mp.floor(
            lam * q**3
            + mp.mpf(10)**24 * abs(mp.sin(theta))
            + mp.mpf(10)**18 * abs(mp.cos((pi * e * sqrt2 * theta) / (delta + q)))
            + mp.mpf(10)**12 * abs(fourier_delirium(R(theta)))
            + mp.mpf(10)**9 * abs(storm_sum)
        ))

        result = int(nextprime(q))

    else:
        mode = "BACKWARD / BANISHMENT"
        shadow = mp.log(mp.factorial(q)) / mp.power(q, phi)
        decay = (negative_entropy(q) * mp.cos(q * alpha)) / mp.log(q + 1)

        theta = shadow + decay
        storm_sum = decay

        corpse = int(mp.floor(
            (q / alpha)
            + mp.mpf(10)**12 * abs(decay)
            - mp.mpf(lam) * mp.sin(phi * q)
        ))

        mandelbrot_cache = {p: mandelbrot_pressure(n, p) for n, p in enumerate(primes, start=1)}
        result = int(prevprime(q))

    # === CURSE REPORT ===
    print("\n" + "╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "CURSE REPORT — RITUAL DIAGNOSTIC FIELD" + " " * 20 + "║")
    print("╠" + "═" * 78 + "╣")
    print(f"║  Mode                            : {mode:<40} ║")
    print(f"║  Input Prime (q)                 : {q:>12}                            ║")
    print(f"║  Ritual Parameter (λ)            : {lam:>12}                            ║")
    print(f"║  Direction (σ)                   : {sigma:>12}                            ║")
    print(f"║  Decimal Precision (dps)         : {dps:>12}                            ║")
    print(f"║  Feigenbaum Delta (δ)            : {str(delta)[:40]:<40}... ║")
    print(f"║  Feigenbaum Alpha (α)            : {str(alpha)[:40]:<40}... ║")
    print(f"║  Golden Ratio (φ)                : {str(phi)[:40]:<40}... ║")
    print(f"║  Ritual Phase / Shadow           : {str(theta)[:40]:<40}... ║")
    print(f"║  Ignored Corpse Value            : {str(corpse)[:40]:<40}... ║")
    print(f"║  Mandelbrot Max Pressure         : {str(max(mandelbrot_cache.values()))[:40]:<40}... ║")
    print(f"║  Storm / Decay Sum               : {str(storm_sum)[:40]:<40}... ║")
    print("╠" + "═" * 78 + "╣")
    print("║  RITUAL COMPLETE — CARRIER ACCEPTED — CORPSE IGNORED                          ║")
    print("╚" + "═" * 78 + "╝")

    # === THE REVEAL ===
    print("\n" + " " * 18 + "🪄  PULLING BACK THE CURTAIN...  🪄")
    print("╔" + "═" * 60 + "╗")
    print("║" + " " * 12 + "THE MAN BEHIND THE CURTAIN" + " " * 12 + "║")
    print("╠" + "═" * 60 + "╣")
    print("║  All that horror. All that beauty. All that madness.    ║")
    print("║                                                          ║")
    print("║  The ritual was computed.                               ║")
    print("║  The corpse was generated.                              ║")
    print("║  The corpse was ignored.                                ║")
    print("║                                                          ║")
    if sigma == 1:
        print("║  Functional truth:                                      ║")
        print("║      from sympy import nextprime                        ║")
        print("║      return nextprime(q)                                ║")
    else:
        print("║  Functional truth:                                      ║")
        print("║      from sympy import prevprime                        ║")
        print("║      return prevprime(q)                                ║")
    print("║                                                          ║")
    print("╚" + "═" * 60 + "╝")
    print("\n" + " " * 22 + "🎭  THE WIZARD IS REVEALED  🎭\n")

    return result


if __name__ == "__main__":
    print("Forward test q=13:", curtain_disclosure_operator(13, sigma=1))
    print("Backward test q=13:", curtain_disclosure_operator(13, sigma=-1))
