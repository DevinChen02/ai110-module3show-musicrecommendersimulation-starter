"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import DEFAULT_TASTE_PROFILE, load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    print(f"Loaded songs: {len(songs)}")

    # Specific profile for comparing high-energy songs against calmer lo-fi tracks.
    user_prefs = DEFAULT_TASTE_PROFILE.copy()

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
