# CLAUDE.md - AI Assistant Guide for Rock-Paper-Scissors

## Project Overview

**Project Name**: Rock-Paper-Scissors Game
**Type**: Educational Python CLI Game
**Language**: Python 3
**Complexity**: Beginner-level
**License**: MIT License (Copyright 2021 Veluri Bharath)

This is a simple command-line rock-paper-scissors game implemented as a single Python script. The project is designed for educational purposes and demonstrates basic Python concepts including functions, user input, random selection, and conditional logic.

## Repository Structure

```
/home/user/rock-paper-scissors/
├── .git/                       # Git repository metadata
├── .gitignore                  # Python-specific gitignore (comprehensive)
├── LICENSE                     # MIT License
└── rock-paper-scissors.py      # Main game implementation (28 lines)
```

**Structure Type**: Flat/Simple - Single-file application with no subdirectories or modules.

## Codebase Architecture

### Design Pattern
- **Paradigm**: Procedural/Imperative programming
- **No OOP**: No classes or objects used
- **Function-based**: Three simple functions with clear separation of concerns

### File: rock-paper-scissors.py

**Functions**:

1. **`is_win(user, computer)` (lines 3-9)**
   - **Purpose**: Determines if the user won the game
   - **Parameters**:
     - `user`: string ('r', 'p', or 's')
     - `computer`: string ('r', 'p', or 's')
   - **Returns**: Boolean
   - **Logic**: Implements game rules: rock > scissors, scissors > paper, paper > rock
   - **⚠️ KNOWN BUG**: Return logic is inverted (returns False when user wins, True otherwise)

2. **`play()` (lines 11-21)**
   - **Purpose**: Main game logic - handles user input, computer choice, and game outcome
   - **Parameters**: None
   - **Returns**: String message describing game result
   - **Flow**:
     1. Prompts user for input
     2. Generates random computer choice
     3. Checks for tie
     4. Evaluates winner using `is_win()`
     5. Returns result message

3. **`main()` (lines 23-24)**
   - **Purpose**: Entry point wrapper
   - **Parameters**: None
   - **Returns**: None
   - **Action**: Calls `play()` and prints the result

**Execution Pattern**: Uses standard `if __name__ == "__main__"` idiom for script execution.

### Dependencies
- **Standard Library**: `random` module only
- **External Dependencies**: None
- **Python Version**: Python 3 (no specific version requirement)

## Known Issues and Bugs

### 🐛 Critical Bug: Inverted Win Logic

**Location**: `rock-paper-scissors.py:6-9`

**Issue**: The `is_win()` function has inverted return logic. The comment says "returns True if you've won" but the code returns `False` when the user wins.

**Current Behavior**:
```python
if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
    return False  # ❌ Should return True
return True       # ❌ Should return False
```

**Expected Fix**:
```python
if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
    return True   # ✓ User wins
return False      # ✓ User loses
```

**Impact**: Game results are correct because `play()` function compensates by checking if `is_win()` returns True to declare "You Won!" (which happens when user actually loses).

### Other Limitations

1. **No Input Validation**: Accepts any input without validation or error handling
2. **Single Round**: No loop for multiple rounds or replay functionality
3. **No Score Tracking**: Cannot track wins/losses across multiple games
4. **No Error Handling**: No try/except blocks or validation
5. **Missing Docstrings**: Functions lack documentation strings

## Development Workflows

### Running the Game

```bash
python rock-paper-scissors.py
# Or
python3 rock-paper-scissors.py
```

**Expected Interaction**:
```
What's your choice? 'r' for rock, 'p' for paper, 's' for scissors
> r
You Won!  # or "You Lost!" or "It's a Tie! Try again!"
```

### Testing

**Current State**: No automated tests exist.

**Recommended Test Coverage** (if implementing tests):
- Test all win conditions (9 scenarios: 3 choices × 3 choices)
- Test tie conditions
- Test input validation
- Test edge cases

**Example Test Cases**:
```python
# User wins
assert is_win('r', 's') == True  # rock beats scissors
assert is_win('s', 'p') == True  # scissors beats paper
assert is_win('p', 'r') == True  # paper beats rock

# User loses
assert is_win('r', 'p') == False  # paper beats rock
assert is_win('s', 'r') == False  # rock beats scissors
assert is_win('p', 's') == False  # scissors beats paper

# Ties (shouldn't call is_win)
# Handled in play() function before calling is_win()
```

### Code Style

**Current Style**:
- No consistent PEP 8 compliance checking
- Simple, readable code
- Minimal comments
- No type hints

**Recommended Improvements**:
- Add type hints: `def is_win(user: str, computer: str) -> bool:`
- Add docstrings to all functions
- Follow PEP 8 naming conventions (currently compliant)
- Add input validation

## Git Workflow

### Branch Strategy

**Current Branch**: `claude/claude-md-mi6muchdpuy2t3b2-01XuydtQMvmjA4pPs2Lb4PAa`

**Important**: All development should occur on the designated Claude branch.

### Commit History

```
b2164ff - added script.py (current)
e589d9d - Initial commit
```

### Making Changes

When making changes to this repository:

1. **Work on the correct branch**: Ensure you're on `claude/claude-md-mi6muchdpuy2t3b2-01XuydtQMvmjA4pPs2Lb4PAa`
2. **Test changes**: Run the script manually to verify behavior
3. **Commit with clear messages**: Follow conventional commit style if possible
4. **Push to remote**: Use `git push -u origin <branch-name>`

### Git Commands

```bash
# Check current branch
git branch --show-current

# Create branch if needed
git checkout -b claude/claude-md-mi6muchdpuy2t3b2-01XuydtQMvmjA4pPs2Lb4PAa

# Stage changes
git add <file>

# Commit
git commit -m "descriptive message"

# Push (with retry on network errors)
git push -u origin claude/claude-md-mi6muchdpuy2t3b2-01XuydtQMvmjA4pPs2Lb4PAa
```

## Key Conventions for AI Assistants

### When Analyzing This Code

1. **Recognize the bug**: The `is_win()` function has inverted logic, but the overall game works correctly because `play()` compensates
2. **Simple is intentional**: This is educational code; don't over-engineer solutions
3. **No dependencies**: Keep the project dependency-free unless explicitly requested
4. **Preserve simplicity**: Maintain the beginner-friendly nature when making improvements

### When Making Changes

1. **Fix bugs carefully**: If fixing the `is_win()` bug, you must also update the `play()` function logic
2. **Add features incrementally**: New features should be optional and not break existing functionality
3. **Maintain compatibility**: Keep the basic user interaction pattern consistent
4. **Document changes**: Update this CLAUDE.md file when making significant architectural changes

### When Adding Features

**Common Enhancement Requests**:

1. **Multiple Rounds**:
   - Add a game loop in `main()`
   - Track score across rounds
   - Allow user to quit

2. **Input Validation**:
   - Validate user input is 'r', 'p', or 's'
   - Handle invalid input gracefully
   - Add error messages

3. **Extended Gameplay**:
   - Add rock-paper-scissors-lizard-spock variant
   - Add difficulty levels
   - Add computer AI strategies

4. **Better UX**:
   - Show computer's choice
   - Display running score
   - Add colored output

### Testing Strategy

Since there are no automated tests:

1. **Manual testing is required** for all changes
2. **Test all three outcomes**: Win, lose, tie
3. **Test with all input combinations**: 9 total scenarios (3×3 grid)
4. **Test edge cases**: Empty input, invalid input, special characters

**Quick Test Script**:
```bash
# Test each choice once
echo "r" | python rock-paper-scissors.py
echo "p" | python rock-paper-scissors.py
echo "s" | python rock-paper-scissors.py
```

## Common Tasks

### Task: Fix the Win Logic Bug

**Location**: `rock-paper-scissors.py:3-9` and `rock-paper-scissors.py:18-21`

**Option 1**: Fix `is_win()` function only
```python
def is_win(user, computer):
    """Returns True if user has won."""
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True  # Changed from False
    return False     # Changed from True
```

Then update `play()`:
```python
if is_win(user_choice, computer_choice):
    return "You Won!"  # Keep same, now correct
return "You Lost!"     # Keep same, now correct
```

**Option 2**: Keep `is_win()` as is, rename it to clarify intent
```python
def did_computer_win(user, computer):
    """Returns True if computer won (user lost)."""
    # Keep existing logic
```

### Task: Add Input Validation

```python
def play():
    valid_choices = ['r', 'p', 's']
    user_choice = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors \n").lower()

    if user_choice not in valid_choices:
        return "Invalid choice! Please choose 'r', 'p', or 's'"

    computer_choice = random.choice(valid_choices)
    # ... rest of function
```

### Task: Add Multiple Rounds

```python
def main():
    score = {"wins": 0, "losses": 0, "ties": 0}

    while True:
        result = play()
        print(result)

        # Update score
        if "Won" in result:
            score["wins"] += 1
        elif "Lost" in result:
            score["losses"] += 1
        else:
            score["ties"] += 1

        print(f"Score - Wins: {score['wins']}, Losses: {score['losses']}, Ties: {score['ties']}")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break
```

### Task: Add Tests (using pytest)

Create `test_rock_paper_scissors.py`:
```python
import pytest
from rock_paper_scissors import is_win

def test_rock_beats_scissors():
    assert is_win('r', 's') == True  # Assuming bug is fixed

def test_scissors_beats_paper():
    assert is_win('s', 'p') == True

def test_paper_beats_rock():
    assert is_win('p', 'r') == True

def test_user_loses():
    assert is_win('r', 'p') == False
    assert is_win('s', 'r') == False
    assert is_win('p', 's') == False
```

Run with: `pytest test_rock_paper_scissors.py`

## Project Context

### Purpose
This appears to be a learning/educational project or coding exercise demonstrating:
- Basic Python syntax
- Functions and control flow
- User input handling
- Random number generation
- Game logic implementation

### Audience
- Python beginners
- Coding tutorial participants
- Students learning programming fundamentals

### Future Direction

This project could evolve into:
1. A more complex game with additional features
2. A web-based version using Flask/Django
3. A GUI version using tkinter or PyGame
4. A multiplayer networked version
5. An AI training environment for reinforcement learning

## Quick Reference

### File Locations
- Main script: `/home/user/rock-paper-scissors/rock-paper-scissors.py`
- License: `/home/user/rock-paper-scissors/LICENSE`
- Gitignore: `/home/user/rock-paper-scissors/.gitignore`

### Key Functions
- `is_win(user, computer)`: Game logic (⚠️ has bug)
- `play()`: Main game flow
- `main()`: Entry point

### Commands
```bash
# Run game
python rock-paper-scissors.py

# Check Python version
python --version

# Run with Python 3 explicitly
python3 rock-paper-scissors.py
```

---

**Last Updated**: 2025-11-19
**Repository Owner**: Veluri Bharath
**Documentation Maintained By**: AI Assistant (Claude)
