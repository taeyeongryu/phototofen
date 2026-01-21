from typing import List

def generate_fen(board_pieces: List[str], active_color: str = 'w') -> str:
    """
    Constructs a FEN string from a list of 64 piece characters (rank-major order).
    
    Args:
        board_pieces: List of 64 strings, representing the board from a8 to h1 (row by row).
        active_color: 'w' or 'b'.
    """
    rows = []
    for r in range(8):
        row_pieces = board_pieces[r*8 : (r+1)*8]
        empty_count = 0
        fen_row = ""
        for p in row_pieces:
            if p == '1':
                empty_count += 1
            else:
                if empty_count > 0:
                    fen_row += str(empty_count)
                    empty_count = 0
                fen_row += p
        if empty_count > 0:
            fen_row += str(empty_count)
        rows.append(fen_row)
        
    board_fen = "/".join(rows)
    # Default suffix: no castling, no en passant, halfmove 0, fullmove 1
    # We can parameterize these later if needed
    return f"{board_fen} {active_color} - - 0 1"
