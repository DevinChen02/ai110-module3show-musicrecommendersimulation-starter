import csv
from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Tuple


DEFAULT_TASTE_PROFILE: Dict[str, Any] = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.80,
    "likes_acoustic": False,
}


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


def _normalize_text(value: Any) -> str:
    """Normalize text-like values for case-insensitive comparisons."""
    return str(value).strip().lower()


def _coerce_song_dict(song: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a raw CSV song row into typed song fields."""
    return {
        "id": int(song["id"]),
        "title": song["title"],
        "artist": song["artist"],
        "genre": song["genre"],
        "mood": song["mood"],
        "energy": float(song["energy"]),
        "tempo_bpm": float(song["tempo_bpm"]),
        "valence": float(song["valence"]),
        "danceability": float(song["danceability"]),
        "acousticness": float(song["acousticness"]),
    }


def _score_song_against_profile(user_prefs: Dict[str, Any], song: Dict[str, Any]) -> Tuple[float, List[str]]:
    """Compute a song's score and human-readable reasons for a user profile."""
    score = 0.0
    reasons: List[str] = []

    favorite_genre = _normalize_text(user_prefs.get("favorite_genre", ""))
    favorite_mood = _normalize_text(user_prefs.get("favorite_mood", ""))
    song_genre = _normalize_text(song.get("genre", ""))
    song_mood = _normalize_text(song.get("mood", ""))

    if favorite_genre and song_genre == favorite_genre:
        score += 1.0
        reasons.append("genre match (+1.0)")

    if favorite_mood and song_mood == favorite_mood:
        score += 2.0
        reasons.append("mood match (+2.0)")

    target_energy = float(user_prefs.get("target_energy", 0.5))
    song_energy = float(song.get("energy", 0.0))
    energy_match = max(0.0, 1.0 - abs(song_energy - target_energy))
    energy_points = energy_match * 5.0
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    likes_acoustic = bool(user_prefs.get("likes_acoustic", False))
    song_acoustic = float(song.get("acousticness", 0.0))
    acoustic_match = song_acoustic >= 0.5
    if acoustic_match == likes_acoustic:
        score += 0.5
        reasons.append("acousticness match (+0.5)")
    else:
        score -= 0.25
        reasons.append("acousticness mismatch (-0.25)")

    return score, reasons


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initialize the recommender with a catalog of songs."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs ranked by profile match score."""
        scored_songs = sorted(
            self.songs,
            key=lambda song: score_song(asdict(user), asdict(song))[0],
            reverse=True,
        )
        return scored_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song matches a user's profile preferences."""
        _, reasons = score_song(asdict(user), asdict(song))
        return "; ".join(reasons) if reasons else "This song matches the profile."


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return [_coerce_song_dict(row) for row in reader]


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    return _score_song_against_profile(user_prefs, song)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = [
        (
            song,
            score,
            "; ".join(reasons) if reasons else "This song matches the profile.",
        )
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    return sorted(scored_songs, key=lambda item: item[1], reverse=True)[:k]
