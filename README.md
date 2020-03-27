# corona_tutor
CS tutoring needs during Corona

All credit goes to CS61, Introduction to Computer Science at UC Berkeley.

# Setting up your git

1. Cloning git
  - Go to your terminal and type the following in order
  ```
  cd ~/Desktop

  git clone https://github.com/Corona-Tutor/corona_tutor.git
  ```
  - This makes a new directory in your desktop called corona_tutor with some
    contents.
2. Config your git
  - Type, substituting your name and you.example.com
  ```
  git config --global user.name "Your Name"
  git config --global user.email you@example.com
  ```     
3. Checking out your branch
  - I created a branch for each of your under your name (eric, andrew, calvin,
    jooyoung, andy)
  - Type the following
  ```
  git checkout --track origin/[insert name]
  ```
# Useful git commands
-- Note this is a very dumb down explanation of git and telling you just what
   you need to know. Do not use this as reference for anything else.

1. Whenever you make a change and want to save your result, type this command
```
git commit -a -m "msg"
```
2. Whenever you want to push into github so that I can see your changes type
   this command only after you commit.
```
git push origin [insert name]
```
3. Whenever you want to add new files that I added, type this command
```
git pull origin master
```
