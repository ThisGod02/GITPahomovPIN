from pathlib import Path
import shutil
import subprocess

root = Path(r"D:\GITPahomovPIN")
labs = sorted(
    [path for path in root.iterdir() if path.is_dir() and path.name.endswith("_lab")],
    key=lambda path: path.name,
)

for lab in labs:
    report = lab / "REPORT.md"
    readme = lab / "README.md"
    if report.exists():
        shutil.copyfile(report, readme)
        report.unlink()

subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
subprocess.run(
    ["git", "-C", str(root), "commit", "-m", "docs: use README as laboratory report"],
    check=True,
)

for lab in labs:
    print(
        f"{lab.name}: README={ (lab / 'README.md').exists() } "
        f"REPORT={ (lab / 'REPORT.md').exists() }"
    )
