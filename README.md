# IT-Paradigm

---
### How to Start
1. You need to create a Github account
2. You need to fork this repository
3. You need to install GIT in your PC or in your mobile phone [Tutorial](#git-installation)
4. You need to execute this `git branch <Your Github_name>` example is `git branch RyannKim327`

---
### Git Installation
**PC**
1. Download and install Git [Link](https://git-scm.com/)
2. Go to Command Prompt or in the terminal of your vscode and start using Git
3. And login your github account

**Mobile Phone**
1. Download and install Termux [Link](https://f-droid.org/en/packages/com.termux/)
2. Enable the storage permission using `termux-setup-storage`
3. Next is install git thru this commands:
```Bash
apt update
apt upgrade
api install git
```
4. Then go to your phone storage using the cd and ls method like
```Bash
cd ../../../../../..
cd /storage/emulated/0/
```
5. Next is you need to git clone your forked repo using: `git clone [link here]` example is:
```Bash
git clone https://github.com/RyannKim27/IT-Paradigm
```
5. Next is go to the directory of your paradigm using `cd IT-Paradigm` command
6. Then use `git config --global --add safe.directory [Repo Directory]` to start example is
```Bash
git config --global --add safe.directory /storage/emulated/0/IT-Paradigm
```
7. Then use `git add .` and start coding now

**Git Commit**
```Bash
git commit -m "Your changes"
```

**Git Pull and Push**
**Git Pull**
```Bash
git pull
```
**Git Push**
```Bash
git push origin <branch>
```

> Where branch is your branch name, the default is main