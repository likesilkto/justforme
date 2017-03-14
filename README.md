My minimal usage for personal git
===

Just for me

---

## Version

Version-**A.a.1**

**A**: Major version

**a**: Minor Version (Increased added some functionality)

**1**: Bug fix, code refine

## Branch name

**dev_A.a.1** is development branch for version A.a.1

**dev_A.a.1_<purpose>** is branch for development of <purpose>.

**dev_A.a.1_<purpose>** is merged to **dev_A.a.1** with comment '<purpose>' when finished developement.

Commit comment in **dev_A.a.1_<purpose>** is as you want.

Commit comment in **dev_A.a.1** is version.

---

## Development flow

1. Clone repository from the remote repository

1. Create branch in local repository

1. Develop the created branch in local repository

1. Merge the developed branch in local repository

1. Push the merged to the remote repository

### Commands

#### Clone repository from the remote repository

```% git clone <url>```

#### Create branch in local repository

  ```% git branch <branch_name>```

  ```% git checkout <branch_name>```

  or

```% git checkout -b <branch_name>```

#### Develop the created branch in local repository

##### When you create new files

  ```% git add <new_files>```

##### Commit in development branch

  ```% git commit -a -m 'commit messeage'```

#### Merge the developed branch in local repository

  ```% git branch master```

  ```% git merge <branch_name>```


#### Push the merged to the remote repository

  ```% git push origin master```

---

## Useful commands

##### Show newly indexed (added) files

  ```% git diff --cached --name-only```

##### Remove files from indexed

  ```% git rm --cached <filename>```

  If you put forget '--cached', actual file is also removed.

##### Add files to index at first

  ```% git add <filename>```

##### Show differences between working and index

  ```% git diff```

##### Show files modified

  ```% git diff --name-only```


  ##### Commit all modified files in local
  ```% git commit -a -m 'commitment comment'```

  The option '-a' automatically commit all modified files. But, new files before indexed (added) are not committed. First, you should add new files before commit.

##### Cancel the commit

  ```% git reset --soft <commit id>```

  Return (reset) to <commit id>, while workflow files will not be changed.

##### Discard the commit

  ```% git reset --hard <commit id>```

  Return (reset) to <commit id>. Workflow files will also return at <commit id>

##### Show commit id and message history

  ```% git log --oneline```

##### Show commit graphically

  ```% git log --graph```

##### Show branch list

  ```% git branch```

##### Create branch

  ```% git branch <branch_name>```

##### Change branch

  ```% git checkout <branch_name>```

##### Delete branch

  ```% git branch -d <branch_name>```

##### Merge branch

  ```% git merge --no--ff <branch_name>```

  Merge commit of <branch_name> to current branch.

##### Commit to the remote repository

  ```% git push origin master```

  _origin_ is just alias of the server name.

  _master_ is branch name. You can specify different branch name.

##### Update the latest commit from the remote repository

  ```% git pull```

##### Pull from local repository

  ```% git pull . <branch>```
  
  or
  
  ```% git merge <branch>```

---

## Configurations

##### Show configuration list

  ```% git config --list```

##### Set cat for pager

   ```% git config --global core.pager cat```

##### merge withoug fast-forward (I like it!)

   ```git config --global --add merge.ff false```

   But, pull fast-forward
   
   ```git config --global --add pull.ff only```


##### Set name globally

  ```% git config --global user.name 'Masayuki Tanaka'```

##### Set email locally (for each project)

  ```% git config --local user.email 'mail@address'```

---

## References

http://d.hatena.ne.jp/mumoshu/20090408/1239202846

http://qiita.com/2m1tsu3/items/6d49374230afab251337

http://d.hatena.ne.jp/mrgoofy33/20100910/1284069468

http://dqn.sakusakutto.jp/2011/10/git_push_origin_master.html

http://www.backlog.jp/git-guide/stepup/stepup2_5.html

http://qiita.com/shyamahira/items/59ff8aa1cf7b893aab60

http://stackoverflow.com/questions/5613902/how-to-pull-from-a-local-branch-into-another-one

http://qiita.com/nog/items/c79469afbf3e632f10a1

---

## Links

[My official page](http://www.ok.sc.e.titech.ac.jp/~mtanaka/)

[My official github](http://github.com/mastnk/)

[My hobby page](http://like.silk.to/)

[My hobby github](http://github.com/likesilkto/)
