# Python virtualenv setup

    virtualenv venv -p python3
    . venv/bin/activate
    pip install -r requirements.txt

    # Initialize bash kernel for Jupyter (see https://github.com/takluyver/bash_kernel)
    python -m bash_kernel.install

# Run Jupyter notebook server

    jupyter notebook