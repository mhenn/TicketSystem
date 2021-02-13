while [ ! -f home/package.json ]
do
  sleep 2 # or less like 0.2
done
cd home
npm run serve
