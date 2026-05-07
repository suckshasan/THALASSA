from dataclasses import dataclass


@dataclass
class Character:
    player_id: int
    player_name: str

    character_name: str
    faction: str
    district: str
    reputation: str

    stress: int = 50
    hunger: int = 50
    credits: int = 50

    alive: bool = True