cd ~/saa
python -m http.server 9090&
while true; do
    echo haku
    python saa.py
    sleep 60
    done
