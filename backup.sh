now=$(date '+%d/%m/%Y %H:%M')
sudo chmod -R 777 moodledata
git add .
git commit -m "Versao $now"
git push origin master
cd html
git add .
git commit -m "Versao $now"
git push origin master
