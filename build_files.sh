echo " BUILD START"
python3.9 -m install -r requirements.txt
python3.9 manage.py collectstatic --oninput --clear
echo "BUILD END"