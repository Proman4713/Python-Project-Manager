Pretty much the first python project I make, I previously just played with python.

Provides one command to CD into any of your project directories.

Currently only works on Windows and WSL.

## Setup

1. Clone this repo

```bash
gh repo clone Proman4713/Python-Project-Manager
```

2. Add this to your `~/.bashrc` or `~/.zshrc` file in WSL

```bash
alias pm="python3 \"path/to/Python-Project-Manager/main.py\""
```

3. If on Windows, create a new text file named pm.bat (not tested), add the following content to it:

```bat
@echo off
python "path\to\Python-Project-Manager\main.py" %*
```
And either move this to a directory in your PATH or add it to your PATH environment variable.

4. Run `pm` to get started

## Usage

Configure your project manager with `pm -c directories` or show the current configuration with `pm -c show`