# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

This recommender reads every song from `data/songs.csv`, then scores each one against the user profile. The scoring logic is content-based: it compares categorical preferences like genre and mood, plus continuous targets such as energy and valence, to compute a numeric score for every candidate song. After scoring all songs, the system sorts them by score and returns the top `k` recommendations.

### Algorithm Recipe

- `+2.0` points for a genre match
- `+1.0` point for a mood match
- `+0.0 to +2.0` points for energy similarity based on how close `song.energy` is to `target_energy`

The continuous similarity bonus is computed with a linear decay from perfect match to a threshold distance, so the closest songs get the strongest energy boost.

### Potential Biases

This system may over-prioritize genre and still miss songs that match the user's mood or energy better. It also treats the dataset as if every user preference is equally reliable, which can bias the ranking toward popular or dominant genre labels rather than more subtle or underrepresented moods.

---

### Song Features

Each `Song` object stores the following attributes used during scoring:

| Feature            | Type    | Description                                                                                                                                      |
| ------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`               | `int`   | Unique track identifier                                                                                                                          |
| `title`            | `str`   | Display name                                                                                                                                     |
| `artist`           | `str`   | Performing artist                                                                                                                                |
| `genre`            | `str`   | Broad genre: `pop`, `rock`, `lofi`, `jazz`, `ambient`, `synthwave`, `indie pop`                                                                  |
| `subgenre`         | `str`   | Fine-grained label: `synth pop`, `hard rock`, `lofi hip-hop`, `lofi jazz`, `smooth jazz`, `space ambient`, `dance pop`, `darksynth`, `dream pop` |
| `mood`             | `str`   | Vibe label: `happy`, `chill`, `intense`, `relaxed`, `focused`, `moody`                                                                           |
| `energy`           | `float` | Perceived intensity — 0.0 (minimal) to 1.0 (maximum)                                                                                             |
| `tempo_bpm`        | `float` | Beats per minute                                                                                                                                 |
| `valence`          | `float` | Emotional positivity — 0.0 (dark/sad) to 1.0 (bright/happy)                                                                                      |
| `danceability`     | `float` | Rhythmic strength and regularity — 0.0 to 1.0                                                                                                    |
| `acousticness`     | `float` | Organic vs. electronic texture — 0.0 to 1.0                                                                                                      |
| `mode`             | `int`   | Key character — `0` minor (darker), `1` major (brighter)                                                                                         |
| `instrumentalness` | `float` | Probability of no vocals — 0.0 (vocal) to 1.0 (instrumental)                                                                                     |

---

### UserProfile Features

Each `UserProfile` stores a **target value** for every continuous feature — the ideal point on that scale — rather than a hard filter. Songs whose feature values fall closest to these targets score highest.

| Field             | Type    | Description                                                          |
| ----------------- | ------- | -------------------------------------------------------------------- |
| `favorite_genre`  | `str`   | Preferred broad genre for categorical match bonus                    |
| `favorite_mood`   | `str`   | Preferred session mood for categorical match bonus                   |
| `target_energy`   | `float` | Ideal energy level (0.0 – 1.0)                                       |
| `target_valence`  | `float` | Ideal emotional positivity (0.0 – 1.0)                               |
| `target_bpm`      | `float` | Preferred tempo in beats per minute                                  |
| `target_acoustic` | `float` | Preferred acoustic texture (0.0 – 1.0)                               |
| `target_inst`     | `float` | Preferred instrumentalness — set near `1.0` for focus/study sessions |
| `preferred_mode`  | `int`   | Preferred key feel — `0` minor, `1` major                            |
| `likes_acoustic`  | `bool`  | Shorthand flag used as a hard filter for acoustic preference         |

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:

- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:

- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:

- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"
```
