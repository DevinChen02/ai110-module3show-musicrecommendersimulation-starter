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

Real-world recommenders use patterns from user behavior and item metadata to predict what someone will enjoy next. This simulation focuses on a transparent content-based approach: it compares each song's attributes to a user taste profile, assigns a score, and returns the highest-scoring songs. The goal is to make the logic easy to inspect while still producing recommendations that feel relevant.

Features used in the simulation:

- `Song` fields: `id`, `title`, `artist`, `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, `acousticness`
- `UserProfile` fields: `favorite_genre`, `favorite_mood`, `target_energy`, `likes_acoustic`

Finalized Algorithm Recipe:

- Start each song at `0.0` points.
- If `song.genre == user.favorite_genre`: add `+2.0`.
- If `song.mood == user.favorite_mood`: add `+2.0`.
- Compute energy similarity: `energy_match = max(0, 1 - abs(song.energy - user.target_energy))`.
- Add weighted energy points: `+ (energy_match * 2.5)`.
- Acoustic preference rule:
   - If `(song.acousticness >= 0.5) == user.likes_acoustic`: add `+0.5`.
   - Otherwise: subtract `-0.25`.
- Final score is the sum of all parts above.

Compact formula:

`score = 2.0*genre_match + 2.0*mood_match + 2.5*max(0, 1 - |energy - target_energy|) + acoustic_adjustment`

where `acoustic_adjustment` is `+0.5` for a match and `-0.25` for a mismatch.

Potential bias note:

This system may over-prioritize exact genre and mood matches, so it can miss songs that are musically very close in energy and feel but use different labels. It can also under-recommend niche or less-represented genres if the dataset is imbalanced.

How recommendations are chosen:

- Score every song in the catalog
- Sort songs from highest score to lowest score
- Return the top `k` songs (for example, top 5) with short explanations of why they matched

Simple flow:

`UserProfile + Song features -> feature match scores -> total score -> sort -> top-k recommendations`

Data flow diagram (Mermaid.js):

```mermaid
flowchart LR
   A[Input: User Preferences\nFavorite Genre, Mood, Target Energy, Likes Acoustic]
   B[Load Songs from CSV\nSong Catalog]
   C[Process Loop\nFor each song, compute score]
   D[Scoring Logic\nGenre + Mood + Energy Similarity + Acoustic Bonus/Penalty]
   E[Store Song + Score]
   F[Rank All Songs\nSort by score descending]
   G[Output: Top K Recommendations]

   A --> C
   B --> C
   C --> D --> E --> F --> G
```



---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### CLI Output Screenshot

![CLI verification screenshot](CLIveri.png)

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

