import csv
from pathlib import Path

class VoteRepository:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load(self) -> dict:
        if not self.file_path.exists():
            return {"John": 0, "Jane": 0}
        try:
            with self.file_path.open(newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                counts = {"John": 0, "Jane": 0}
                for row in reader:
                    name = row.get("candidate", "")
                    votes = int(row.get("votes", "0"))
                    if name in counts:
                        counts[name] = votes
                return counts
        except Exception:
            return {"John": 0, "Jane": 0}

    def save(self, counts: dict):
        try:
            with self.file_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["candidate", "votes"])
                writer.writeheader()
                for name, votes in counts.items():
                    writer.writerow({"candidate": name, "votes": votes})
        except Exception as e:
            raise e

