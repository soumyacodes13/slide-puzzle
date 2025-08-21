# 🧩 Slide Puzzle (3x3) in Python

A simple **console-based sliding puzzle game** written in Python.  
Rearrange the shuffled tiles into the correct order using `u`, `d`, `l`, `r` moves.  
Built with only Python’s standard library — no extra dependencies required.  

---
<!--
## 🎥 Live Demo

![Slide Puzzle Demo](demo.gif)

👉 Try it online: ## 🚀 [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
-->





## 🎮 How to Play

- The board starts in a shuffled state.
- One space is left empty (`" "`) so you can slide tiles around.
- Your goal is to rearrange the numbers into order:

```
1 2 3
4 5 6
7 8  
```

- Controls:  
  - `u` → Move **up**  
  - `d` → Move **down**  
  - `l` → Move **left**  
  - `r` → Move **right**

---

## ▶️ Running the Game

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/slide-puzzle.git
   cd slide-puzzle
   ```

2. Run the Python script:
   ```bash
   python slide_puzzle.py
   ```

---

## 📝 Example Gameplay

```
Initial board (shuffled):
4 1 3
2   6
7 5 8

Enter your move (up/down/left/right): r

4 1 3
2 6  
7 5 8
```

Keep sliding until the board is solved!

---

## ⚙️ Requirements

- Python 3.x  
- No external libraries needed (uses only built-in modules)

---

## 📌 Features

- Random board shuffle each game  
- Simple console-based interface  
- Classic puzzle mechanics  
- Works on Linux, macOS, and Windows  

---

## 🚀 Future Improvements (Ideas)

- Add **win detection** when the board is solved  
- Track **number of moves** made  
- Add a **timer** to measure solving time  
- Create a **GUI version** with Tkinter or Pygame  

---

## 🧑‍💻 Author

Developed by [Soumyajit](https://github.com/soumyacodes13)

---

## 📜 Source Code

Here’s the complete Python code (`slide_puzzle.py`):

```python
import random
import os

# 🎮 Draw the board
def draw_board(board):
    print(f"{board[0]} {board[1]} {board[2]}")
    print(f"{board[3]} {board[4]} {board[5]}")
    print(f"{board[6]} {board[7]} {board[8]}")
    print()

# 🔍 Find empty space (" ")
def box_pos(board):
    return board.index(" ")

# 🎯 Check if puzzle is solved
def is_solved(board):
    return board == [1, 2, 3, 4, 5, 6, 7, 8, " "]

# 👤 Handle player move
def player_move(board, move):
    y = box_pos(board)

    if move in ['u', 'd']:
        x = 3
    elif move in ['l', 'r']:
        x = 1
    else:
        return board  # invalid move, do nothing

    if move == 'u' and y not in [0, 1, 2]:
        board[y], board[y - x] = board[y - x], board[y]
    elif move == 'd' and y not in [6, 7, 8]:
        board[y], board[y + x] = board[y + x], board[y]
    elif move == 'l' and y not in [0, 3, 6]:
        board[y], board[y - x] = board[y - x], board[y]
    elif move == 'r' and y not in [2, 5, 8]:
        board[y], board[y + x] = board[y + x], board[y]

    return board


if __name__ == "__main__":
    # 🔀 Shuffle board
    board = [1, 2, 3, 4, 5, 6, 7, 8, " "]
    random.shuffle(board)

    moves = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🧩 3x3 Slide Puzzle")
        print("-------------------")
        draw_board(board)

        if is_solved(board):
            print(f"🎉 Congratulations! You solved the puzzle in {moves} moves.")
            break

        move = input("Enter your move (u=up, d=down, l=left, r=right): ").lower().strip()
        if move in ['u', 'd', 'l', 'r']:
            board = player_move(board, move)
            moves += 1
        else:
            print("❌ Invalid move! Use u/d/l/r.")
            input("Press Enter to continue...")
```
