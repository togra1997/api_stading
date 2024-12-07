"""run uvicorn."""

import subprocess

subprocess.run(["uvicorn", "main:app", "--reload", "--port=8001"], check=False)
