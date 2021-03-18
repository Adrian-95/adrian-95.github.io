pelican content -o output -s publishconf.py
ghp-import -m "Generate Pelican site" -b master output
git push origin master
git add content
git commit -m 'update'
git push origin content