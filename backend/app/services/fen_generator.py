from typing import List, Union
from app.models.api_models import PieceClass

def generate_fen(board_pieces: List[Union[str, PieceClass]], active_color: str = 'w') -> str:
    """
    Constructs a FEN string from a list of 64 piece characters (rank-major order).
    
    Args:
        board_pieces: List of 64 items (PieceClass enum or strings), representing the board from a8 to h1.
        active_color: 'w' or 'b'.
    """
    rows = []
    for r in range(8):
        row_pieces = board_pieces[r*8 : (r+1)*8]
        empty_count = 0
        fen_row = ""
        for p in row_pieces:
            # Handle PieceClass enum or string
            val = p.value if isinstance(p, PieceClass) else p
            
            if val == "empty" or val == '1':
                empty_count += 1
            else:
                if empty_count > 0:
                    fen_row += str(empty_count)
                    empty_count = 0
                fen_row += val
        if empty_count > 0:
            fen_row += str(empty_count)
        rows.append(fen_row)
        
    board_fen = "/".join(rows)
    # Default suffix: no castling, no en passant, halfmove 0, fullmove 1
    # We can parameterize these later if needed
    return f"{board_fen} {active_color} - - 0 1"
