from pathlib import Path
from model.vote_model import VoteModel
from storage.file_repository import VoteRepository
from utils.validators import validate_candidate
from utils.errors import PersistenceError

class VoteController:
    def __init__(self, data_file: Path):
        self.repo = VoteRepository(data_file)
        self.model = VoteModel()

        counts = self.repo.load()
        self.model.john_votes = counts["John"]
        self.model.jane_votes = counts["Jane"]

    def cast_vote(self, selected_john: bool, selected_jane: bool, voter_id: str) -> str:
        try:
            candidate = validate_candidate(selected_john, selected_jane)

            if not voter_id.strip():
                return "Please enter your ID"

            self.model.cast_vote(candidate, voter_id.strip())
            self.repo.save(self.model.get_counts())
            return f"Vote cast for {candidate}"
        except ValueError as ve:
            return str(ve)
        except Exception as e:
            raise PersistenceError(f"Could not save votes: {e}")

    def get_results(self) -> dict:
        return self.model.get_counts()

    def get_total(self) -> int:
        return self.model.total_votes()

