1. I installed Puthon 3.14.10 from web. After that I ran Install Certificates.command and saw:

"Last login: Wed Oct 28 15:08:45 on ttys010
/Applications/Python\ 3.14/Install\ Certificates.command ; exit;
(base) ivankyrylko@MacBook-Pro-Ivan ~ % /Applications/Python\ 3.14/Install\ Certificates.command ; exit;
 -- pip install --upgrade certifi
Requirement already satisfied: certifi in /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages (2026.10.23)
 -- removing any existing file or link
 -- creating symlink to certifi certificate bundle
 -- setting permissions
 -- update complete

Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.

[Process completed]"
ivankyrylko@MacBook-Pro-Ivan ~ % python3 --version
Python 3.14.10
ivankyrylko@MacBook-Pro-Ivan ~ % which python3
/Library/Frameworks/Python.framework/Versions/3.14/bin/python3

2. I installed Command Line Tools and ran
ivankyrylko@MacBook-Pro-Ivan ~ % git --version
git version 2.55.0

3. I installed VS Code, the code command, the Python extension.

4. I configured Git and ran:

(base) ivankyrylko@MacBook-Pro-Ivan ~ % cd /Users/ivankyrylko/mentor-lab/work/diagnostic
(base) ivankyrylko@MacBook-Pro-Ivan diagnostic % git init
підказка: Використання "master" як назву для початкової гілки. Ця назва гілки за замовчуванням
підказка: зміниться на "main" у Git 3.0. Щоб налаштувати початкову назву гілки,
підказка: яка буде використовуватися у всіх ваших нових сховищах, що приховає це попередження,
підказка: виконайте:
підказка:
підказка: 	git config --global init.defaultBranch <назва>
підказка:
підказка: Замість "master" зазвичай вибирають імена "main", "trunk" і
підказка: "development". Щойно створену гілку можна перейменувати за допомогою цієї команди:
підказка:
підказка: 	git branch -m <name>
підказка:
підказка: Disable this message with "git config set advice.defaultBranchName false"
Ініціалізовано порожнє Git сховище в /Users/ivankyrylko/mentor-lab/work/diagnostic/.git/
(base) ivankyrylko@MacBook-Pro-Ivan diagnostic % git config set init.defaultBranch main
(base) ivankyrylko@MacBook-Pro-Ivan diagnostic % git config --list
credential.helper=osxkeychain
user.name=ivan.kyrylko
user.email=ivan.kyrylko.dev@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
init.defaultbranch=main


5. I created SSH key and confirated it. I ran
(base) ivankyrylko@MacBook-Pro-Ivan .ssh % ssh -T git@github.com
Hi ivankyrylkodev! You've successfully authenticated, but GitHub does not provide shell access.



## Installed
ivankyrylko@MacBook-Pro-Ivan diagnostic % python3 --version
Python 3.14.10
ivankyrylko@MacBook-Pro-Ivan diagnostic % which python3
/Library/Frameworks/Python.framework/Versions/3.14/bin/python3
ivankyrylko@MacBook-Pro-Ivan diagnostic % git --version
git version 2.55.0
ivankyrylko@MacBook-Pro-Ivan diagnostic % code --version
1.136.1
a44adf7f53e00964ab890f9f8758a334f1fc15bc
arm64
ivankyrylko@MacBook-Pro-Ivan diagnostic %  git config --global --show-origin --get init.defaultBranch
file:/Users/ivankyrylko/.gitconfig	main

## Commands
cd /Users/ivankyrylko/mentor-lab/work/diagnostic (i went to folder mentor-lab/work/diagnostic)
git init (i initialized my git)
git add . (I added all files in folder to git)
git commit -m "Add README and .gitignore" (I added comment about what was done)
git branch -M main (I showed that i want to write all files in main branch)
git remote add origin https://github.com/ivankyrylkodev/mentorlab-diagnostic.git (I connected folder with my repository)
git push -u origin main (I send my files on my repository)
python3 --version (I checked version of Python on my Mac)
touch ~/.ssh/config (I created configuration file)
open ~/.ssh/config (I opened configuration file)

## Problem
The longest step was adding SSH. I read a lot documentation to understand how to do it. I don't understand why I did it, but I did it. 
ivankyrylko@MacBook-Pro-Ivan diagnostic %  git remote -v
origin	git@github.com:ivankyrylkodev/mentorlab-diagnostic.git (fetch)
origin	git@github.com:ivankyrylkodev/mentorlab-diagnostic.git (push)
Понятия не имею  почему push теперь идёт через ключ.

## AI use
none
## Time
Learning 20 min
Exersises 30 min


ivankyrylko@MacBook-Pro-Ivan ~ % python3 --version
Python 3.14.10
ivankyrylko@MacBook-Pro-Ivan ~ % which python3
/Library/Frameworks/Python.framework/Versions/3.14/bin/python3
ivankyrylko@MacBook-Pro-Ivan ~ % cd /Users/ivankyrylko/mentor-lab/work/diagnostic
ivankyrylko@MacBook-Pro-Ivan diagnostic % git config --global user.name
ivan.kyrylko
ivankyrylko@MacBook-Pro-Ivan diagnostic % git config --global user.email
ivan.kyrylko.dev@gmail.com
ivankyrylko@MacBook-Pro-Ivan diagnostic % git config --global init.defaultBranch
ivankyrylko@MacBook-Pro-Ivan diagnostic % git config --list
credential.helper=osxkeychain
user.name=ivan.kyrylko
user.email=ivan.kyrylko.dev@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
init.defaultbranch=main
remote.origin.url=https://github.com/ivankyrylkodev/mentorlab-diagnostic.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
ivankyrylko@MacBook-Pro-Ivan diagnostic % git config --global init.defaultbranch
ivankyrylko@MacBook-Pro-Ivan diagnostic % git config --global core.defaultbranch
ivankyrylko@MacBook-Pro-Ivan work % cd ..
ivankyrylko@MacBook-Pro-Ivan mentor-lab % git -C work/diagnostic log --oneline
8005979 (HEAD -> main, origin/main) Add README and .gitignore
ivankyrylko@MacBook-Pro-Ivan mentor-lab % git -C work/diagnostic remote -v
origin	https://github.com/ivankyrylkodev/mentorlab-diagnostic.git (fetch)
origin	https://github.com/ivankyrylkodev/mentorlab-diagnostic.git (push)
ivankyrylko@MacBook-Pro-Ivan mentor-lab % git -C work/diagnostic status
На гілці main
Ваша гілка не відрізняється від "origin/main".

нічого комітити, робоче дерево чисте
ivankyrylko@MacBook-Pro-Ivan mentor-lab % git ls-remote https://github.com/ivankyrylkodev/mentorlab-diagnostic.git main
80059796e03f734d163ebda9da79f5c3a5d72e37	refs/heads/main
ivankyrylko@MacBook-Pro-Ivan mentor-lab % git -C work/diagnostic rev-parse main
80059796e03f734d163ebda9da79f5c3a5d72e37
ivankyrylko@MacBook-Pro-Ivan mentor-lab % git -C work/diagnostic ls-files
.gitignore
D-001/NOTES.md
README.md





ivankyrylko@MacBook-Pro-Ivan ~ % cd /Users/ivankyrylko/mentor-lab/work/diagnostic
ivankyrylko@MacBook-Pro-Ivan diagnostic % git remote set-url --push origin git@github.com:ivankyrylkodev/mentorlab-diagnostic.git
ivankyrylko@MacBook-Pro-Ivan diagnostic % git config list
credential.helper=osxkeychain
user.name=ivan.kyrylko
user.email=ivan.kyrylko.dev@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
init.defaultbranch=main
remote.origin.url=https://github.com/ivankyrylkodev/mentorlab-diagnostic.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
remote.origin.pushurl=git@github.com:ivankyrylkodev/mentorlab-diagnostic.git
branch.main.remote=origin
branch.main.merge=refs/heads/main
user.email=317626512+ivankyrylkodev@users.noreply.github.com
ivankyrylko@MacBook-Pro-Ivan diagnostic % git remote set-url origin git@github.com:ivankyrylkodev/mentorlab-diagnostic.git
ivankyrylko@MacBook-Pro-Ivan diagnostic % git config list
credential.helper=osxkeychain
user.name=ivan.kyrylko
user.email=ivan.kyrylko.dev@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
init.defaultbranch=main
remote.origin.url=git@github.com:ivankyrylkodev/mentorlab-diagnostic.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
remote.origin.pushurl=git@github.com:ivankyrylkodev/mentorlab-diagnostic.git
branch.main.remote=origin
branch.main.merge=refs/heads/main
user.email=317626512+ivankyrylkodev@users.noreply.github.com
ivankyrylko@MacBook-Pro-Ivan diagnostic %  git status
На гілці main
Ваша гілка не відрізняється від "origin/main".

Зміни, не додані до майбутнього коміту:
  (скористайтесь "git add <файл>...", щоб оновити майбутній коміт)
  (скористайтесь "git restore <файл>...", щоб скасувати зміни в робочій директорії)
	змінено:       README.md

не додано жодних змін до коміту (скористайтесь "git add" та/або "git commit -a")
ivankyrylko@MacBook-Pro-Ivan diagnostic % git add .
ivankyrylko@MacBook-Pro-Ivan diagnostic % git commit -m "Add string to README.md
"
[main 948e068] Add string to README.md
 1 file changed, 3 insertions(+), 1 deletion(-)
ivankyrylko@MacBook-Pro-Ivan diagnostic % git push
git Перерахування обʼєктів: 5, готово.
Підрахунок обʼєктів: 100% (5/5), готово.
Дельта компресія з використанням до 14 потоків
Компресія обʼєктів: 100% (3/3), готово.
Запис обʼєктів: 100% (3/3), 444 байти | 444.00 КіБ/с, готово.
Всього 3 (дельта 1), повторно використано 0 (дельта 0), повторно використано пакунків 0 (з 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:ivankyrylkodev/mentorlab-diagnostic.git
   15b11b5..948e068  main -> main
ivankyrylko@MacBook-Pro-Ivan diagnostic % git git status
git: "git" не є командою git. Дивіться git --help.

Найбільш схожою командою є
	init
ivankyrylko@MacBook-Pro-Ivan diagnostic % git status
На гілці main
Ваша гілка не відрізняється від "origin/main".

нічого комітити, робоче дерево чисте
ivankyrylko@MacBook-Pro-Ivan diagnostic % git add .
ivankyrylko@MacBook-Pro-Ivan diagnostic % git commit -m "Correct NOTES.md"
[main fcec661] Correct NOTES.md
 1 file changed, 15 deletions(-)
ivankyrylko@MacBook-Pro-Ivan diagnostic % git push
Перерахування обʼєктів: 7, готово.
Підрахунок обʼєктів: 100% (7/7), готово.
Дельта компресія з використанням до 14 потоків
Компресія обʼєктів: 100% (3/3), готово.
Запис обʼєктів: 100% (4/4), 421 байт | 421.00 КіБ/с, готово.
Всього 4 (дельта 1), повторно використано 0 (дельта 0), повторно використано пакунків 0 (з 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:ivankyrylkodev/mentorlab-diagnostic.git
   948e068..fcec661  main -> main
ivankyrylko@MacBook-Pro-Ivan diagnostic %