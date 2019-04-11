""" Definition of king class and its movement. """

from .piece import Piece

class King(Piece):
    """ King model. """

    symbol = '♚'

    @property
    def movements(self):
        """ King moves one square in any direction.
        Don't mind out-of-bounds relative positions: forbidden ones will be
        silently discarded within the ``Piece.territory()`` method above.
        """
        return set([
            # Horizontal movements.
            (+1, 0), (-1, 0),
            # Vertical movements.
            (0, +1), (0, -1),
            # Diagonal movements.
            (+1, +1), (-1, -1), (-1, +1), (+1, -1),
        ])
