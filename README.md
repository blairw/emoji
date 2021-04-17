# emoji

Usage:

```zsh
./emoji.sh sweatsmile | tr -d '\n' | pbcopy
```

Consider adding to your `.zshrc` or `.bashrc`:

```
alias emoji='/path/to/emoji.sh'
```

Then you can just do (from anywhere):

```zsh
emoji sweatsmile | tr -d '\n' | pbcopy
```