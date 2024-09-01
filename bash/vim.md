## Basic Navigation

`1h`, `j`, `k`, `l` - Move the cursor left, down, up, and right, respectively.

1. `w` - Move the cursor to the beginning of the next word.
1. `b` - Move the cursor to the beginning of the previous word.
1. `0` - Move the cursor to the beginning of the line.
1. `$` - Move the cursor to the end of the line.
1. `G` - Move the cursor to the last line of the file.
1. `gg` - Move the cursor to the first line of the file.

## Editing

1. `i` - Enter Insert mode before the cursor.
1. `a` - Enter Insert mode after the cursor.
1. `x` - Delete the character under the cursor.
1. `dd` - Delete the current line.
1. `yy` - Yank (copy) the current line.
1. `p` - Paste after the cursor.
1. `u` - Undo the last change.
1. `Ctrl + r` - Redo the last undone change.

## Search and Replace

1. `/` - Search for a pattern in the file (press n to go to the next match).
1. `?` - Search backward for a pattern (press N to go to the previous match).
1. `:%s/old/new/g` - Replace all occurrences of old with new in the file.

## Window Management

1. `:split` - Split the window horizontally.
1. `:vsplit` - Split the window vertically.
1. `Ctrl + w + w` - Switch between split windows.

## Favorites

1. `d$` - delete everything until the EOL
1. `5dd`- delete next 5 lines
