# !/bin/bash
python3 -m venv venv
. venv/bin/activate
pip install -U pip
pip install wheel
pip install -r requirements.txt
git clone https://github.com/AmanGupta0112/elevator_system.git
cd elevator_system
