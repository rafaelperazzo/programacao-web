now=$(date '+%d/%m/%Y %H:%M')
sudo chmod -R 777 moodledata
git add .
git commit -m "Versao $now"
git push origin master
/var/www/html/backup/./mysql.backup.sh
cd html
git add .
git commit -m "Versao $now"
git push origin master
