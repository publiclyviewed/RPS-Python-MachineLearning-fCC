def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # Default move for the first play
    if not opponent_history:
        return "R"

    # Track patterns in opponent history
    n = 4  # Pattern length to search for
    if len(opponent_history) >= n:
        recent_moves = ''.join(opponent_history[-n:])  # Get the last n moves
        pattern_dict = {}

        # Create a dictionary of patterns and their follow-ups
        for i in range(len(opponent_history) - n):
            pattern = ''.join(opponent_history[i:i + n])
            next_move = opponent_history[i + n] if i + n < len(opponent_history) else None
            if pattern not in pattern_dict:
                pattern_dict[pattern] = {"R": 0, "P": 0, "S": 0}
            if next_move:
                pattern_dict[pattern][next_move] += 1

        # Predict the next move
        if recent_moves in pattern_dict:
            predicted_move = max(pattern_dict[recent_moves], key=pattern_dict[recent_moves].get)
            counter_moves = {"R": "P", "P": "S", "S": "R"}
            return counter_moves[predicted_move]

    # Fallback: Most frequent counter strategy
    counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        counts[move] += 1
    predicted_move = max(counts, key=counts.get)
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted_move]
