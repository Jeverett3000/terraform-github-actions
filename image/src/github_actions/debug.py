"""Actions debug logging"""

import sys


def debug(msg: str) -> None:
    """Add a message to the actions debug log."""
    
    # Optimize for the common case of single-line messages
    if '\n' not in msg:
        sys.stderr.write(f'::debug::{msg}\n')
    else:
        for line in msg.splitlines():
            sys.stderr.write(f'::debug::{line}\n')

def warning(msg: str) -> None:
    """Add a warning message to the workflow log."""
    
    # Optimize for the common case of single-line messages
    if '\n' not in msg:
        sys.stderr.write(f'::warning::{msg}\n')
    else:
        for line in msg.splitlines():
            sys.stderr.write(f'::warning::{line}\n')
