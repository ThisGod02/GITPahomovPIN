# Ассеты (Git LFS)

`logo.png`, `banner.jpg` отслеживаются через Git LFS (см. `.gitattributes`). Проверка: `git lfs ls-files`, `git lfs status`.

```bash
sudo apt install git-lfs -y
git lfs install
git lfs track "*.png" "*.jpg"
git add .gitattributes
```
