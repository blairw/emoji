# emoji

## Why?

There are a few emoji that I use regularly in my communications. I want to be able to quickly get them using only my keyboard, not having to fiddle with Googling, picker GUIs, etc.

## Setup

Before running, you will need to `sudo pip3 install pandas`.

Usage:

```zsh
./emoji.py sweatsmile | tr -d '\n' | pbcopy
```

Consider adding to your `.zshrc` or `.bashrc`:

```
alias emoji='/path/to/emoji.py'
```

(Dot trick adapted from https://unix.stackexchange.com/questions/1496/why-doesnt-my-bash-script-recognize-aliases)

Then you can just do (from anywhere):

```zsh
emoji sweatsmile | tr -d '\n' | pbcopy
# or...
emoji sweatsmile # copies to your clipboard using pbcopy
```