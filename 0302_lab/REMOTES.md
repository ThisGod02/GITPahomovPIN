# Работа с remotes и Merge Request
```bash
git remote -v
git remote add upstream git@gitlab.com:original-owner/collab-project.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```
MR: push ветки в форк -> New merge request (source `feature/...`, target `main`) -> Changes/Code Review -> Merge (Merge commit / Squash / Rebase and merge).
Защита `main`: Settings -> Repository -> Protected Branches, merge — Maintainers, push — No one (только через MR).
