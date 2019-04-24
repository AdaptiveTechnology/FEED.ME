source ~/catkin_ws/devel/setup.bash
export PYTHONPATH=${PYTHONPATH}:/home/niryo/catkin_ws/src/niryo_one_python_api/src/niryo_python_api
python homev3.py
python autocaltest.py
sudo shutdown -h -P now

