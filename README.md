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
2. Next is install git thru this commands:
```Bash
apt get && apt upgrade
api install git openssh
```
3. Next is you need to sign up your github account into your termux by executing:
```Bash
ssh-keygen -t rsa -C "YOUR_EMAIL_ADDRESS"
ssh -T git@github.com
```