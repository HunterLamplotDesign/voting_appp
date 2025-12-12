def validate_candidate(selected_john: bool, selected_jane: bool) -> str:
    if selected_john and selected_jane:
        raise ValueError("Pick only one candidate")
    if not selected_john and not selected_jane:
        raise ValueError("Please select a candidate")
    return "John" if selected_john else "Jane"
