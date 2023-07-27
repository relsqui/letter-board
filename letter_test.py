import textwrap

BOARD_ROWS = 8
BOARD_COLS = 13

def make_letter_map(letter_string):
  letters = {}
  for letter in letter_string:
    if letter not in "\n\t ":
      letters[letter] = letters.get(letter, 0) + 1
  return letters

def s(number):
  return "" if number == 1 else "s"

def sort_string(string):
  return "".join(sorted(list(string)))

def file_to_uppercase(filename):
  with open(filename) as f:
    return f.read().upper()

def compare_letter_maps(board, message):
  board_letters = make_letter_map(board)
  message_letters = make_letter_map(message)
  missing = ""
  for letter in message_letters:
    diff = message_letters[letter] - board_letters.get(letter, 0)
    if diff > 0:
      missing += letter * diff
  return missing

def preview_board(rows, cols, wrapped_message):
  width = cols + 2
  preview = ""
  line = f"+{'-' * width}+"
  preview += line
  if len(wrapped_message) < rows:
    wrapped_message += [""] * (rows - len(wrapped_message))
  for message_line in wrapped_message[:rows]:
    message_line = message_line.strip()
    padding = " " * (cols - len(message_line))
    preview += f"\n| {message_line}{padding} |"
  preview += "\n" + line
  return preview

def wrap_message(cols, message):
  lines = []
  # split this ourselves to preserve line breaks in the original
  for line in message.splitlines():
    lines += textwrap.wrap(line, width=cols, drop_whitespace=False)
  return lines

def main():
  board = file_to_uppercase("board_letters.txt")
  message = file_to_uppercase("board_message.txt")
  missing = compare_letter_maps(board, message)
  wrapped = wrap_message(BOARD_COLS, message)

  print(f"You're missing these letters: {missing}" if missing else "You have enough letters.")
  if len(wrapped) > BOARD_ROWS:
    print("You might not have enough space.")
  print("\nPreview:")
  print(preview_board(BOARD_ROWS, BOARD_COLS, wrapped))

if __name__ == "__main__":
  main()