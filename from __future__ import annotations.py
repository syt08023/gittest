from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import json


@dataclass
class RunLog:
    message: str
    created_at: str

    @staticmethod
    def now(message: str) -> "RunLog":
        return RunLog(message=message, created_at=datetime.now().isoformat(timespec="seconds"))


def append_log(log_path: Path, message: str) -> RunLog:
    log = RunLog.now(message)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logs = []
    if log_path.exists():
        try:
            logs = json.loads(log_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            logs = []

    logs.append(log.__dict__)
    log_path.write_text(json.dumps(logs, ensure_ascii=False, indent=2), encoding="utf-8")
    return log


def main() -> None:
    log_path = Path("logs") / "runs.json"
    log = append_log(log_path, "Hello GitHub — second push!")
    print(f"[OK] saved: {log_path}")
    print(f"[LOG] {log.created_at} | {log.message}")


if __name__ == "__main__":
    main()
    
print("Program finished successfully.")