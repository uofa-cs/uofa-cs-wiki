# Tools and Developer Environment Setup

Your development environment is where you spend all your time. A bad setup costs you hours every week through friction, slowness, and confusion. A good setup disappears and lets you focus on actually building things. This guide covers the practical tooling every UofA CS student should have configured.

---

## Git: Beyond the Basics

UofA's CMPUT 301 introduces Git, but "introduced to Git" and "can actually use Git" are different things. Most students graduate knowing `git add`, `git commit`, and `git push`. That's not enough.

### What You Actually Need to Know

**Branching.** Never commit directly to `main` on any project you care about. Create a branch for every feature or fix (`git checkout -b feat/user-auth`), do your work there, then merge it back. This keeps `main` always in a working state.

**Merging vs rebasing.** `git merge` creates a merge commit that preserves the full history of both branches. `git rebase` replays your commits on top of the target branch, producing a linear history. Rebasing is cleaner for feature branches before merging; merging is safer for shared branches. Learn both, understand when to use each.

**Interactive rebase.** `git rebase -i HEAD~5` opens an editor letting you reorder, squash, edit, or drop the last 5 commits. This is how you clean up a messy branch before opening a pull request. Your reviewers will appreciate it.

**Cherry-pick.** `git cherry-pick <commit-hash>` applies a single commit from one branch to another. Useful when you want just one specific change without taking everything else.

**Stash.** `git stash` saves your current working changes without committing them. `git stash pop` brings them back. Indispensable when you need to quickly switch branches without half-finished work getting in the way.

**git blame and git bisect.** `git blame <file>` shows who wrote each line and when. `git bisect` does a binary search through history to find which commit introduced a bug. These are debugging tools that become valuable on real projects.

### Commit Message Conventions

Random commit messages make history useless. Use **Conventional Commits** — a lightweight standard that makes history readable and enables automated changelogs:

```
feat: add JWT authentication to login endpoint
fix: handle null user ID in profile fetch
refactor: extract database connection into module
chore: update dependencies to latest versions
docs: add API usage examples to README
test: add integration tests for payment flow
```

The format is `type: short description in present tense`. Keep the subject line under 72 characters. Add a body if the "why" isn't obvious. This takes ten seconds per commit and makes you look professional.

### .gitignore Files

Every project needs a `.gitignore`. Never commit `node_modules/`, `__pycache__/`, `.env` files, compiled binaries, or IDE-specific files. Use [gitignore.io](https://www.toptal.com/developers/gitignore) to generate a correct `.gitignore` for your stack (e.g., "Python, Django, VSCode").

### SSH Keys for GitHub

Stop using HTTPS with a password. Set up SSH key authentication:

```bash
ssh-keygen -t ed25519 -C "your@email.com"
cat ~/.ssh/id_ed25519.pub
```

Copy the output and add it to GitHub under Settings > SSH and GPG keys. Then clone repos with the SSH URL (`git@github.com:user/repo.git`). You'll never type a password again.

### Useful Git Aliases

Add these to `~/.gitconfig` under `[alias]`:

```ini
[alias]
    st = status
    co = checkout
    br = branch
    lg = log --oneline --graph --decorate --all
    unstage = reset HEAD --
    last = log -1 HEAD
```

`git lg` especially — it shows your branch history as a visual graph in the terminal. Far more useful than the default `git log`.

---

## Linux and WSL Setup

The UofA CS labs run Linux (Ubuntu). If you're on Windows, you are at a disadvantage unless you address this.

### WSL2 on Windows

Windows Subsystem for Linux 2 (WSL2) runs a real Linux kernel inside Windows. It's excellent. Install it:

```powershell
wsl --install
```

This installs Ubuntu 22.04 LTS by default. After setup, you have a full Linux terminal, can install any Linux packages, and can run Docker natively. VS Code integrates seamlessly with WSL via the Remote-WSL extension.

### Terminal Commands You Must Know

If any of these are unfamiliar, learn them now:

| Command | What it does |
|---|---|
| `ls -la` | List files, including hidden, with details |
| `cd`, `pwd` | Navigate directories, print current path |
| `cp`, `mv`, `rm` | Copy, move, delete files |
| `grep -r "pattern" .` | Search for text recursively in current directory |
| `find . -name "*.py"` | Find files matching a pattern |
| `chmod 755 script.sh` | Change file permissions |
| `ssh user@host` | Connect to remote server |
| `ps aux`, `kill` | List processes, kill a process |
| `df -h`, `du -sh *` | Disk usage |
| `curl`, `wget` | Make HTTP requests, download files |

Pipes (`|`) and redirects (`>`, `>>`, `<`) are fundamental. `cat file.txt | grep "error" | sort | uniq -c` is the kind of command that becomes second nature.

### Shell Scripting

Even basic Bash scripts save hours. Automate things you do repeatedly: setting up a project, running test suites, deploying to a server. A 10-line script that runs daily has enormous ROI.

### Zsh and Oh My Zsh

Zsh is an improved shell that's now the default on macOS and popular on Linux. **Oh My Zsh** is a framework that adds themes, plugins, and useful defaults on top.

```bash
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Recommended plugins to add to `.zshrc`:
- `git` — adds git status to your prompt and useful aliases
- `zsh-autosuggestions` — suggests commands as you type based on history
- `zsh-syntax-highlighting` — highlights valid/invalid commands as you type

These seem like cosmetic improvements but they genuinely reduce errors and speed up terminal work.

---

## Editor: VS Code vs JetBrains

This is not a religious debate. Both are good. Here's when to use each.

### VS Code

Free, fast, open source, massive extension ecosystem. Works well for Python, JavaScript/TypeScript, Go, Rust, Markdown, and almost everything else. VS Code is the safe choice for most things.

**Essential extensions:**
- **GitLens**: supercharges Git integration — inline blame, history browser, commit search
- **Python + Pylance**: language support and type checking for Python
- **Docker**: manage containers and images from VS Code
- **Remote - SSH**: edit files on remote servers as if they're local
- **Remote - WSL**: develop inside WSL from Windows
- **GitHub Copilot**: AI autocomplete — free for students (see GitHub Student Pack below)
- **Error Lens**: shows error messages inline instead of requiring a hover
- **Prettier**: automatic code formatting for JS/TS/CSS/JSON

### JetBrains IDEs

JetBrains makes purpose-built IDEs for specific languages: PyCharm (Python), IntelliJ IDEA (Java/Kotlin), CLion (C/C++), GoLand (Go), Rider (C#), WebStorm (JS/TS).

They are heavier than VS Code but the code intelligence is deeper. Refactoring tools are superior — renaming a class, extracting a method, finding all usages — these work more reliably in JetBrains products.

**The student license is free.** Apply at [jetbrains.com/student](https://www.jetbrains.com/student/) with your UofA email. This gives you access to all JetBrains IDEs.

**Recommendation:** VS Code for most projects and languages. PyCharm for larger Python projects where refactoring matters. IntelliJ when working with Java or Kotlin.

---

## Dotfiles: Your Environment is Infrastructure

Dotfiles are configuration files that live in your home directory: `~/.bashrc`, `~/.zshrc`, `~/.gitconfig`, `~/.vimrc`, `~/.ssh/config`. They control your shell, editor, git behavior, and more.

**Keep your dotfiles in a GitHub repository.** This means:
1. Your environment is reproducible — set up a new machine in minutes
2. It shows prospective employers that you care about your tooling
3. You have version history if you break something

A minimal `.zshrc` aliases section worth having:

```bash
# Navigation
alias ..="cd .."
alias ...="cd ../.."
alias ll="ls -la"

# Git shortcuts
alias gs="git status"
alias ga="git add"
alias gc="git commit"
alias gp="git push"
alias gpl="git pull"
alias gl="git log --oneline --graph --decorate"

# Safety nets
alias rm="rm -i"  # Ask before deleting
alias cp="cp -i"  # Ask before overwriting

# Python
alias python="python3"
alias pip="pip3"
```

---

## SSH into UofA Servers

The CS department has remote machines you can SSH into: `gpu.cs.ualberta.ca` and other lab machines. Useful for running long jobs, accessing department resources, or testing on Linux when you're on a different OS.

### Setting Up SSH Keys for UofA Servers

Generate a key (if you haven't already), then copy the public key to the server:

```bash
ssh-copy-id yourccid@gpu.cs.ualberta.ca
```

Now you can connect without a password.

### ~/.ssh/config for Named Connections

Instead of typing `ssh yourccid@gpu.cs.ualberta.ca` every time, add this to `~/.ssh/config`:

```
Host uofa-gpu
    HostName gpu.cs.ualberta.ca
    User yourccid
    IdentityFile ~/.ssh/id_ed25519
```

Now `ssh uofa-gpu` connects you immediately.

### tmux for Persistent Sessions

If you SSH into a server and your connection drops, anything running in that terminal dies. `tmux` solves this by running a session on the server that persists regardless of your connection.

Essential tmux commands:
- `tmux new -s mysession` — start a named session
- `Ctrl+B, D` — detach (leave it running)
- `tmux attach -t mysession` — reconnect to it later
- `Ctrl+B, %` — split pane vertically
- `Ctrl+B, "` — split pane horizontally
- `Ctrl+B, arrow keys` — move between panes

Install tmux, spend an hour with a tutorial, and use it for any long-running server process.

---

## GitHub Student Developer Pack

Apply at [education.github.com](https://education.github.com). Use your UofA email. You'll get:

- **GitHub Copilot**: AI code completion. Free while you're a student. Actually useful.
- **JetBrains IDEs**: all of them, free.
- **DigitalOcean credits**: $200 to deploy real projects in the cloud.
- **Namecheap domain**: one free `.me` domain for a year — good for a portfolio site.
- **MongoDB Atlas**: cloud database credits.
- **Various other services**: Heroku, Datadog, Sentry, and more.

Apply for this immediately if you haven't. It's free money and tools.

---

## Package Managers

Every operating system has a package manager that installs and manages software. Use it instead of downloading installers manually.

- **macOS**: [Homebrew](https://brew.sh). `brew install git python node go` — installs anything with one command.
- **Ubuntu/WSL**: `apt`. `sudo apt update && sudo apt install git curl wget`. Pre-installed on Ubuntu.
- **Windows**: `winget` is the Microsoft package manager. Or install WSL and use `apt`.

For Python specifically, use `venv` to create isolated environments per project, and `pip` or `uv` to manage packages within them. Never install Python packages globally — it creates dependency conflicts.

---

## Docker: Install It Early

Docker is covered more in [what-to-learn.md](./what-to-learn.md), but from a setup perspective: install Docker Desktop early and start using it for side projects. The habit of containerizing your applications — even small ones — pays off.

After installation, verify it works:

```bash
docker run hello-world
docker run -it ubuntu bash  # Spin up an Ubuntu container interactively
```

Get comfortable with `docker build`, `docker run`, `docker ps`, `docker logs`, and `docker-compose up`. These are table stakes in most dev jobs.

---

## API Testing: Postman and Bruno

When you're building REST APIs, you need a way to make HTTP requests and inspect responses without writing a full frontend. Two main options:

**Postman** is the industry standard. GUI app, supports collections (organized groups of requests), environments (switch between dev/staging/prod), and automated test scripts. Free tier is sufficient.

**Bruno** is the open-source alternative. Stores your collections as files in your project directory (not in a cloud account), which means they live in Git alongside your code. More privacy-friendly than Postman.

Either one works. The important habit is testing your API endpoints as you build them, not just assuming they work.

---

## Putting It Together

A reasonable setup for a UofA CS student:

1. WSL2 with Ubuntu 22.04 (Windows) or native terminal (macOS/Linux)
2. Zsh + Oh My Zsh with autosuggestions and syntax highlighting
3. VS Code with GitLens, Pylance, Docker, Remote-SSH, Copilot
4. JetBrains student license applied and downloaded
5. SSH keys for GitHub and any servers you use
6. `~/.ssh/config` with named connections
7. Dotfiles in a GitHub repo
8. Docker Desktop installed
9. tmux for server sessions
10. GitHub Student Pack applied

None of this takes more than a few hours to set up. Once it's done, you largely forget about it and just work. That's the point.

Your environment is a tool. Sharpen it.
