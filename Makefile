export PYTHONPATH = .venv

.PHONY: uv
uv:
	pip install --upgrade 'uv>=0.5.6,<0.6'
	uv venv

setup:
	@if [ ! -d ".venv" ] || ! command -v uv > /dev/null; then \
		echo "UV not installed or .venv does not exist, running uv"; \
		make uv; \
	fi
	@if [ ! -f "uv.lock" ]; then \
		echo "Can't find lock file. Locking"; \
		uv lock; \
	fi
	uv sync --alll-extras --all-groups
	uv pip install -no-deps -e .