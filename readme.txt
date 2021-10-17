# HowTo update doc.orbitalwaves.net content:

```
cd into local repo
source bin/activate
make edits to source/
make html
deactivate
eval `ssh-agent`
ssh-add your github key
git add -A
git commit -m "your edits"
git push

ssh -A orbitalwaves.net
cd /usr/share/nginx/doc.orbitalwaves.net/public_html
git pull
```
