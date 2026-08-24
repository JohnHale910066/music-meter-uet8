from dataclasses import dataclass

@dataclass(frozen=True)
class Snapshot:
    project: str
    owner: str
    profile: str

def build_snapshot() -> Snapshot:
    return Snapshot("music-meter-uet8", "JohnHale910066", "0037")

print(build_snapshot())
