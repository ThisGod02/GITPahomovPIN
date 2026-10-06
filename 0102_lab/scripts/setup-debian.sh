#!/bin/bash
set -e
# Lab 01: установка и настройка Git, SSH-ключ, первый репозиторий (Debian)
USER_NAME="${USER_NAME:-Ivanov Ivan}"
USER_EMAIL="${USER_EMAIL:-ivanov@example.com}"
sudo apt update
sudo apt install git -y
git --version
git config --global user.name "$USER_NAME"
git config --global user.email "$USER_EMAIL"
git config --global core.editor nano
git config --global color.ui auto
if [ ! -f ~/.ssh/id_ed25519 ]; then
  ssh-keygen -t ed25519 -C "$USER_EMAIL" -f ~/.ssh/id_ed25519 -N ""
fi
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
ssh -T git@gitlab.com || true
mkdir -p ~/hello-git
cd ~/hello-git
git init -b main
git add README.md .gitignore
git commit -m "feat: add README.md with project description"
git log --oneline
# git remote add origin git@gitlab.com:username/hello-git.git
# git push -u origin main
