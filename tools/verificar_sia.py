import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
resultado = subprocess.run(
    [str(root / 'backend/.venv/Scripts/python.exe'), 'manage.py', 'test',
     'mantenimiento', 'compras', 'soporte', 'usuarios',
     '--settings=config.settings_tests', '--noinput'],
    cwd=root / 'backend', capture_output=True, text=True, encoding='utf-8', errors='replace',
)
(root / 'backend/test-sia.log').write_text(resultado.stdout + '\n' + resultado.stderr, encoding='utf-8')
print(resultado.stderr[-10000:] if resultado.returncode else resultado.stderr.strip())
raise SystemExit(resultado.returncode)
