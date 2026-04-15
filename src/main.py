"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import DEFAULT_TASTE_PROFILE, load_songs, recommend_songs


USER_PREFERENCE_PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.90,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.35,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.95,
        "likes_acoustic": False,
    },
}


ADVERSARIAL_USER_PROFILES = {
    "Conflicting Mood-Energy": {
        "favorite_genre": "ambient",
        "favorite_mood": "sad",
        "target_energy": 0.95,
        "likes_acoustic": True,
    },
    "String Bool Trap": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.40,
        "likes_acoustic": "False",
    },
    "Out-Of-Range High Energy": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 5.0,
        "likes_acoustic": False,
    },
    "Out-Of-Range Low Energy": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": -2.0,
        "likes_acoustic": False,
    },
    "Unknown Category Labels": {
        "favorite_genre": "hyperpop",
        "favorite_mood": "ecstatic",
        "target_energy": 0.75,
        "likes_acoustic": False,
    },
    "Empty Category Inputs": {
        "favorite_genre": "",
        "favorite_mood": "",
        "target_energy": 0.80,
        "likes_acoustic": False,
    },
    "Whitespace Casing": {
        "favorite_genre": "  PoP  ",
        "favorite_mood": " HAPPY ",
        "target_energy": 0.82,
        "likes_acoustic": False,
    },
    "Type Coercion Categories": {
        "favorite_genre": ["pop"],
        "favorite_mood": None,
        "target_energy": 0.82,
        "likes_acoustic": False,
    },
    "Acoustic Preference Conflict": {
        "favorite_genre": "folk",
        "favorite_mood": "nostalgic",
        "target_energy": 0.90,
        "likes_acoustic": True,
    },
    "Tie Heavy Baseline": {
        "favorite_genre": "none",
        "favorite_mood": "none",
        "target_energy": 0.50,
        "likes_acoustic": False,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    all_profiles = {**USER_PREFERENCE_PROFILES, **ADVERSARIAL_USER_PROFILES}

    print(f"Loaded songs: {len(songs)}")

    # Pick any key from USER_PREFERENCE_PROFILES or ADVERSARIAL_USER_PROFILES.
    selected_profile = "Deep Intense Rock"
    user_prefs = all_profiles.get(
        selected_profile,
        DEFAULT_TASTE_PROFILE,
    ).copy()

    print(f"Using profile: {selected_profile}")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 72)
    print("TOP RECOMMENDATIONS")
    print("=" * 72)

    for index, rec in enumerate(recommendations, start=1):
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]

        print(f"\n{index}. {song['title']}")
        print(f"   Final score: {score:.2f}")
        print("   Reasons:")
        for reason in reasons:
            print(f"   - {reason}")

    print("\n" + "=" * 72)


if __name__ == "__main__":
    main()
