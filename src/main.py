"""
ToneMatch 1.0 — Music Recommender Simulation runner.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood":  "happy",
        "target_energy":  0.80,
        "target_valence": 0.80,
        "target_bpm":     120.0,
        "target_acoustic":0.20,
        "target_inst":    0.05,
        "preferred_mode": 1,       # 1 = major
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for idx, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{idx}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.split(" | "):
            print(f"     - {reason}")
        print()


if __name__ == "__main__":
    main()
