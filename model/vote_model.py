class VoteModel:
    def __init__(self):
        self.john_votes = 0
        self.jane_votes = 0
        self.voters = set()  # track IDs that already voted

    def cast_vote(self, candidate_name: str, voter_id: str):
        if voter_id in self.voters:
            raise ValueError("Already voted")

        if candidate_name == "John":
            self.john_votes += 1
        elif candidate_name == "Jane":
            self.jane_votes += 1
        else:
            raise ValueError("Invalid candidate")

        self.voters.add(voter_id)

    def get_counts(self) -> dict:
        return {"John": self.john_votes, "Jane": self.jane_votes}

    def total_votes(self) -> int:
        return self.john_votes + self.jane_votes
