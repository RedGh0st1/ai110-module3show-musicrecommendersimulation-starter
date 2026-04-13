# Profile Comparison Reflections

Each section below compares two profiles side by side, describing what changed in
the output and why the difference makes sense given the preferences being tested.

---

## 1. High-Energy Pop vs. Chill Lo-Fi
*Energy opposites — same scoring formula, completely opposite catalogs*

**High-Energy Pop top 3:** Gym Hero (pop/intense, energy 0.93), Sunrise City (pop/happy, energy 0.82), Neon Seoul (k-pop/energetic, energy 0.85)
**Chill Lo-Fi top 3:** Midnight Coding (lofi/chill, energy 0.42), Library Rain (lofi/chill, energy 0.35), Focus Flow (lofi/focused, energy 0.40)

These two profiles pull the catalog in exactly opposite directions on energy. The Pop profile targets energy 0.88, so the Gaussian rewards songs above 0.75 heavily and ignores anything below 0.60. The Lo-Fi profile targets energy 0.40, so quiet, slow songs cluster at the top and high-intensity songs earn almost nothing. Neither top-3 overlaps at all — they occupy entirely different regions of the catalog. This makes sense and is the clearest sign that the energy signal is working as intended: two users describing opposite listening moods get opposite recommendations without any manual filtering.

What is also worth noting is that Lo-Fi's top 3 are all lofi-genre songs (scores 10.98, 10.89, 10.00), while Pop's top 2 are pop-genre songs but #3 is k-pop (no genre match). The Lo-Fi catalog has three songs in the genre vs. Pop's two, which partly explains why the lo-fi results look tighter and more consistent. The catalog density gap is visible in the scores.

---

## 2. High-Energy Pop vs. Deep Intense Rock
*Same energy target, opposite emotional character*

**High-Energy Pop top 3:** Gym Hero (pop/intense, energy 0.93, valence 0.77), Sunrise City (pop/happy, energy 0.82, valence 0.84), Neon Seoul (k-pop/energetic, energy 0.85, valence 0.86)
**Deep Intense Rock top 3:** Storm Runner (rock/intense, energy 0.91, valence 0.48), Iron Curtain (metal/aggressive, energy 0.96, valence 0.30), Fracture Point (drum and bass/frantic, energy 0.92, valence 0.60)

Both profiles want high energy — 0.88 and 0.93 respectively — yet their top fives share zero songs. The difference is entirely in valence and mood. The Pop profile targets valence 0.82 (bright, positive) and the Rock profile targets valence 0.35 (dark, driven). Songs like Sunrise City (valence 0.84) and Neon Seoul (valence 0.86) score near maximum valence points for Pop but near zero for Rock. Meanwhile, Iron Curtain (valence 0.30) is almost invisible to the Pop profile but ranks #2 for Rock because its darkness matches the Rock user's emotional target.

This comparison demonstrates that energy alone does not define a listening experience. Two users can want the same physical intensity but want completely different feelings inside it — one bright and euphoric, one dark and aggressive — and the scoring correctly separates them through valence rather than energy. The genre and mood signals reinforce the separation further: Rock's preferred_mode is minor (0) while Pop's is major (1), which adds another 1-point push in opposite directions.

---

## 3. Chill Lo-Fi vs. The Lyric Lover
*Same genre, same energy — different instrumentalness target*

**Chill Lo-Fi top 3:** Midnight Coding (inst 0.85), Library Rain (inst 0.90), Focus Flow (inst 0.88)
**Lyric Lover top 3:** Library Rain (inst 0.90), Midnight Coding (inst 0.85), Focus Flow (inst 0.88)

These two profiles are nearly identical — same genre, same subgenre, same energy target (0.40 vs. 0.38), same preferred mode — with one difference: Chill Lo-Fi targets instrumentalness 0.87, while Lyric Lover targets 0.95. The top-3 songs are the same three songs in a different order. Library Rain (inst 0.90) is marginally closer to 0.95 than Midnight Coding (inst 0.85), so it moves from #2 to #1. The swap is small — a 0.04-point difference in instrumentalness, translating to a fraction of the 0.5-point max for that signal — but it is consistent and real.

What this comparison reveals is that instrumentalness, even at its current low maximum weight, can break ties between otherwise equivalent songs when everything else is matched. The Lyric Lover's target of 0.95 is extreme enough that it also fires the ×0.60 multiplicative penalty on any song with instrumentalness below 0.25, but since no lo-fi song in the catalog is that vocal-heavy, the penalty never activates for this profile. The result is that Lyric Lover gets the same recommendations as a standard Lo-Fi user but with a slightly different internal ordering — a subtle but valid shift.

---

## 4. High-Energy Pop vs. The Minor Happy
*Same genre, same mood — opposite key preference*

**High-Energy Pop top 5:** Gym Hero (mode=major, score 10.37), Sunrise City (mode=major, score 9.85), Neon Seoul (mode=major, score 8.45), Rooftop Lights (mode=major, score 8.44), Salsa Fuego (mode=major, score 7.91)
**Minor Happy top 5:** Sunrise City (mode=major, score 8.77), Rooftop Lights (mode=major, score 7.99), Crown Walk (mode=minor, score 7.79), Neon Seoul (mode=major, score 7.06), Funky Parliament (mode=major, score 6.88)

Both profiles want pop, happy songs with high valence. The only meaningful difference is preferred_mode: Pop wants major (1), Minor Happy wants minor (0). Every song in the top 5 for Pop is major-key, earning the +1.0 mode match bonus each time. For Minor Happy, the same major-key songs still appear at #1 and #2 because their genre + mood + energy alignment is strong enough to overcome the missing mode point. But at #3, Crown Walk (hip-hop, minor-key, energy 0.72) appears — a song that would never reach the top 5 for the standard Pop user because it earns no genre or mood points. It climbs because it is one of the few minor-key songs with high enough energy and valence to partially compensate for missing genre and mood.

This comparison shows how a single preference — key feel — can reshape the mid-table without affecting the clear winner. It also exposes a real tension: the Minor Happy user genuinely wants happy pop music but prefers the emotional texture of minor keys. Very few pop songs are written in minor keys, so the system cannot fully satisfy both preferences simultaneously. Instead of flagging this conflict, it quietly settles for major-key pop at the top and inserts an unrelated minor-key song at #3 as a partial substitute.

---

## 5. Deep Intense Rock vs. The Contradiction
*Same energy target — one profile is coherent, one is internally conflicted*

**Deep Intense Rock top 3:** Storm Runner (rock/intense, valence 0.48), Iron Curtain (metal/aggressive, valence 0.30), Fracture Point (drum and bass/frantic, valence 0.60)
**The Contradiction top 3:** Gym Hero (pop/intense, valence 0.77), Iron Curtain (metal/aggressive, valence 0.30), Storm Runner (rock/intense, valence 0.48)

Both profiles target energy around 0.92–0.93, so the same high-intensity songs compete for both. The difference is that Rock is internally coherent — high energy, low valence, minor key, aggressive mood all point toward the same type of song — while The Contradiction sends opposite signals. The Contradiction wants pop genre (bright, produced) with sad mood and valence 0.10 (dark, negative) at high energy. Those three preferences cannot be satisfied simultaneously by any song in the catalog.

The result is that Gym Hero (pop, energy 0.93, valence 0.77) ranks #1 for The Contradiction because it wins the genre + subgenre + energy match, even though its valence of 0.77 is almost as far as possible from the user's target of 0.10. The system has no way to notice or report that the genre preference and the valence preference contradict each other — it just adds up whatever points each song can earn. Rock's Storm Runner ranks #3 for The Contradiction despite earning zero genre points, purely because its minor key, low valence, and high energy all align with the numerical targets. In a coherent profile, genre is the first filter. In a contradictory profile, genre becomes a misleading anchor that pulls the #1 result away from what the continuous signals actually point toward.

---

## 6. The Genre Ghost vs. The Agnostic
*Both lose their strongest categorical signal — but for different reasons*

**The Genre Ghost top 3:** Coffee Shop Stories (jazz/relaxed, score 9.48), Focus Flow (lofi/focused, score 7.94), Library Rain (lofi/chill, score 7.93)
**The Agnostic top 3:** Midnight Coding (lofi/chill, score 7.32), Island Morning (reggae/uplifting, score 7.25), Focus Flow (lofi/focused, score 7.10)

The Genre Ghost's favorite genre ("bossa nova") is not in the catalog, so the full genre exact bonus (1.0 pts after the weight shift) is unavailable. The Agnostic's favorite genre is "pop" and it exists in the catalog, but all continuous targets are set to 0.50, which means every song earns some partial energy and valence credit and no song stands out numerically.

Despite reaching similar situations — weakened differentiation — the two profiles resolve differently. The Genre Ghost still has a strong mood preference ("relaxed") and a specific energy target (0.38), so once the genre map routes "bossa nova" to jazz and Coffee Shop Stories earns the mapped genre bonus, it pulls far ahead (#1 at 9.48) because mood, energy, and valence all align tightly. The #1 result is genuinely meaningful. The Agnostic, by contrast, gets Midnight Coding at #1 not because it is a great pop or happy match — it is neither — but because its energy (0.42) happens to sit close to the neutral midpoint of 0.50 and it shares a major key with the user's preference. The gap between #1 and #5 is only 0.47 points, meaning the ranking is essentially a coin toss among songs with similar proximity to 0.50 on every axis. The Genre Ghost loses one signal but compensates with others. The Agnostic has no strong signal to compensate with, so the recommendations drift toward whatever the catalog happens to cluster around — which turns out to be lofi and low-energy songs.

---

## 7. The Mismatch Maximizer vs. Everyone Else
*What happens when almost every song fails*

**The Mismatch Maximizer top 3:** Moonlight Study (classical/serene, score 8.23), Spacewalk Thoughts (ambient/chill, score 4.40), Library Rain (lofi/chill, score 3.59)

Every other profile in this project has a clear #1 winner scoring above 7.0 and a top-5 that clusters within a few points. The Mismatch Maximizer's #1 (Moonlight Study) scores 8.23 — reasonable — but #2 falls to 4.40, a gap of nearly 4 full points. The remaining four results hover between 3.0 and 3.6, practically tied.

This is what the scoring system looks like when the catalog has nothing close to what the user wants. Moonlight Study is the only classical song, earns both genre and mood exact matches, and its energy (0.18) and instrumentalness (0.98) are the closest in the catalog to the user's extreme targets of 0.05 and 0.99. After it, the system is scraping for partial credit wherever it can find it. Spacewalk Thoughts appears at #2 not because it is a good recommendation but because its low energy (0.28) and high instrumentalness (0.95) are the next-best numerical fits among 24 remaining songs. Library Rain appears at #3 for the same reason. The system gives the appearance of a ranked recommendation list when in reality it is ranking degrees of failure. This comparison more than any other illustrates that a recommender system can only be as good as the catalog behind it — when the right songs simply do not exist, ranked output is a fiction.