.DEFAULT: help

help:
    @echo "make clean"
    @echo "       prepare development environment, use only once"
    @echo "make clean-build"
    @echo "       Clear all build directories"
    @echo "make isort"
    @echo "       run isort command cli in development features"
    @echo "make lint"
    @echo "       run lint"
    @echo "make test"
    @echo "       run tests"
    @echo "make run"
    @echo "       run the web application"