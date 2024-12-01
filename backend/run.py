"""run uvicorn."""

import subprocess

subprocess.run(["uvicorn", "main:app", "--reload"], check=False)
