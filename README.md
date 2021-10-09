# emoji

## Why?

There are a few emoji that I use regularly in my communications. I want to be able to quickly get them using only my keyboard, not having to fiddle with Googling, picker GUIs, etc.

## Usage

```zsh
❯ emoji sweatsmile
😅
```

For full list of emojis named so far: `emoji --list`

## Setup

Before running, you will need to `sudo pip3 install pandas`.

Then add these aliases to your `~/.zshrc` or `~/.bashrc`:

```
alias emoji='python3 /path/to/emoji.py'
alias emojicopy='. python3 /path/to/emojicopy.sh'
```

(Dot trick adapted from https://unix.stackexchange.com/questions/1496/why-doesnt-my-bash-script-recognize-aliases)

Then you can just do (from anywhere):

```zsh
emoji sweatsmile | tr -d '\n' | pbcopy
# or...
emojicopy sweatsmile # copies to your clipboard using pbcopy
```