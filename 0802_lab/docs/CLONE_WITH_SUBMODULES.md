# Клонирование с submodules

```bash
git clone --recurse-submodules git@gitlab.com:username/parent-project.git
# или для уже склонированного:
git submodule update --init --recursive
# обновление submodule до последней версии:
cd libs/shared && git pull origin main && cd ../..
git add libs/shared && git commit -m "chore: update shared-library submodule"
```
