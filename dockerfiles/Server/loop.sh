while [ ! -f home/start.sh ]
do
  sleep 2 # or less like 0.2
done
cd home
sh start.sh
