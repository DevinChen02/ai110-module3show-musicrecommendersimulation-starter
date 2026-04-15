# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeMatch Classroom 1.0**

---

## 2. Intended Use  

This recommender suggests songs from a small catalog.
It uses a few user preferences like genre, mood, energy, and acoustic taste.
It assumes users can describe their taste with those simple settings.
This project is for classroom exploration, not for production users.

---

## 3. How the Model Works  

Each song has features like genre, mood, energy, and acousticness.
The user also gives favorite genre, favorite mood, target energy, and acoustic preference.
The model gives points for genre and mood matches.
It also gives more points when song energy is close to the user target.
I kept the starter scoring style but added clearer explanations for why each song was ranked.

---

## 4. Data  

The catalog has 17 songs.
It includes genres like pop, lofi, rock, ambient, jazz, hip hop, funk, folk, metal, and classical.
It includes moods like happy, chill, intense, dreamy, dark, reflective, and nostalgic.
I did not add or remove songs.
The dataset is small, so many music styles and cultures are still missing.

---

## 5. Strengths  

The system works well when a user has clear preferences.
The Chill Lofi profile got calm, lower-energy songs, which felt correct.
The Deep Intense Rock profile ranked Storm Runner near the top, which made sense.
The explanations are easy to read and help users understand the ranking.

---

## 6. Limitations and Bias 

One weakness is that energy can dominate the score.
Because of that, very energetic songs can rank high even when genre or mood is only a partial match.
This can create a filter bubble, where users keep seeing songs with similar intensity.
The small dataset also increases bias because some genres have fewer choices.

---

## 7. Evaluation  

I tested High-Energy Pop, Chill Lofi, and Deep Intense Rock profiles.
I checked whether the top songs matched the profile vibe and whether the reasons were believable.
One surprise was that Gym Hero showed up for both Happy Pop and Deep Intense Rock users.
That makes sense because the song has very high energy, and energy has a strong effect in scoring.

---

## 8. Future Work  

I would reduce the energy weight so genre and mood matter more.
I would add more user controls, like tempo range and danceability preference.
I would add a diversity step so the top 5 are not all the same style.
I would expand the song catalog so the model can serve more tastes fairly.

---

## 9. Personal Reflection  

My biggest learning moment was seeing that one weight change can completely reshuffle the top songs.
AI tools helped me move faster by suggesting test ideas, edge cases, and clearer explanations.
I still had to double-check AI suggestions by running profiles, because some ideas sounded good but did not match the actual outputs.
I was surprised that a simple point system can still feel personal when the profile settings clearly match the song features.
If I extend this project, I would add more songs, add a diversity step, and let users tune how much genre, mood, and energy each matter.
