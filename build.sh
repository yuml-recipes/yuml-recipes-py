echo "Initialize venv ..."
source venv.sh

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Lint with flake8 ..."
# stop the build if there are Python syntax errors or undefined names
flake8 yuml tests --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings
flake8 yuml tests --count --exit-zero --max-complexity=10 --max-line-length=180 --statistics

echo "Run tests ..."
pytest

echo "All is well!"
