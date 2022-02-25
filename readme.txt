# How to update doc.a3-audio.com content:

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

ssh -A to your server
cd /usr/share/nginx/doc.a3-audio.com/public_html
git pull
```
