# Submodules, LFS и Container Registry

- `libs/shared` — общая библиотека (submodule, см. `.gitmodules` и `docs/CLONE_WITH_SUBMODULES.md`).
- `assets/` + `.gitattributes` — крупные файлы через Git LFS.
- `Dockerfile` + `.gitlab-ci.yml` — сборка, тестирование и публикация образа в GitLab Container Registry (`$CI_REGISTRY_IMAGE`).
