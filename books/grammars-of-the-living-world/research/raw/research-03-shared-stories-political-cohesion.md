# Research 3

 Authentication complete.  
\- gh config set \-h github.com git\_protocol https  
✓ Configured git protocol  
\! Authentication credentials saved in plain text  
✓ Logged in as PlayfulProcess  
\! You were already logged in to this account  
faga\_alves@cloudshell:\~$   
faga\_alves@cloudshell:\~$ cd /tmp && rm \-rf repo-clean && git clone \--bare https://github.com/PlayfulProcess/Jongu-2.0.git repo-clean && cd repo-clean && echo 'faga.alves@gmail.com==\>REDACTED' \> /tmp/replace-text.txt && printf 'PlayfulProcess \<17236172+PlayfulProcess@users.noreply.github.com\> \<faga.alves@gmail.com\>\\n' \> /tmp/mailmap.txt && git filter-repo \--mailmap /tmp/mailmap.txt \--replace-text /tmp/replace-text.txt \--replace-message /tmp/replace-text.txt \--force && git remote add origin https://github.com/PlayfulProcess/Jongu-2.0.git && git push origin \--mirror \--force  
Cloning into bare repository 'repo-clean'...

remote: Enumerating objects: 233, done.  
remote: Counting objects: 100% (233/233), done.  
remote: Compressing objects: 100% (164/164), done.  
remote: Total 233 (delta 52), reused 213 (delta 32), pack-reused 0 (from 0\)  
Receiving objects: 100% (233/233), 233.91 KiB | 5.20 MiB/s, done.  
Resolving deltas: 100% (52/52), done.  
NOTICE: Removing 'origin' remote; see 'Why is my origin removed?'  
        in the manual if you want to push back there.  
        (was https://github.com/PlayfulProcess/Jongu-2.0.git)  
Parsed 11 commits  
New history written in 0.07 seconds; now repacking/cleaning...  
Repacking your repo and cleaning out old unneeded objects  
Enumerating objects: 233, done.  
Counting objects: 100% (233/233), done.  
Delta compression using up to 4 threads  
Compressing objects: 100% (159/159), done.  
Writing objects: 100% (233/233), done.  
Building bitmaps: 100% (11/11), done.  
Total 233 (delta 51), reused 197 (delta 37), pack-reused 0  
Completely finished after 0.16 seconds.  
Enumerating objects: 233, done.  
Writing objects: 100% (233/233), 234.37 KiB | 117.19 MiB/s, done.  
Total 233 (delta 0), reused 0 (delta 0), pack-reused 233  
remote: Resolving deltas: 100% (51/51), done.  
To https://github.com/PlayfulProcess/Jongu-2.0.git  
 \+ 0b16407...c2724fb main \-\> main (forced update)  
faga\_alves@cloudshell:/tmp/repo-clean$   
faga\_alves@cloudshell:/tmp/repo-clean$ cd /tmp && rm \-rf repo-clean && git clone \--bare https://github.com/PlayfulProcess/jongu-7rays-visualization.git repo-clean && cd repo-clean && echo 'faga.alves@gmail.com==\>REDACTED' \> /tmp/replace-text.txt && echo 'julia.alves@pepsico.com==\>REDACTED' \>\> /tmp/replace-text.txt && echo 'juliamtisdale@gmail.com==\>REDACTED' \>\> /tmp/replace-text.txt && printf 'PlayfulProcess \<17236172+PlayfulProcess@users.noreply.github.com\> \<faga.alves@gmail.com\>\\n' \> /tmp/mailmap.txt && git filter-repo \--mailmap /tmp/mailmap.txt \--replace-text /tmp/replace-text.txt \--replace-message /tmp/replace-text.txt \--force && git remote add origin https://github.com/PlayfulProcess/jongu-7rays-visualization.git && git push origin \--mirror \--force  
Cloning into bare repository 'repo-clean'...  
remote: Enumerating objects: 259, done.  
remote: Counting objects: 100% (76/76), done.  
remote: Compressing objects: 100% (50/50), done.  
remote: Total 259 (delta 41), reused 59 (delta 25), pack-reused 183 (from 1\)  
Receiving objects: 100% (259/259), 157.89 MiB | 1.72 MiB/s, done.  
Resolving deltas: 100% (56/56), done.  
NOTICE: Removing 'origin' remote; see 'Why is my origin removed?'  
        in the manual if you want to push back there.  
        (was https://github.com/PlayfulProcess/jongu-7rays-visualization.git)  
Parsed 30 commits  
New history written in 2.87 seconds; now repacking/cleaning...  
Repacking your repo and cleaning out old unneeded objects  
Enumerating objects: 259, done.  
Counting objects: 100% (259/259), done.  
Delta compression using up to 4 threads  
Compressing objects: 100% (218/218), done.  
Writing objects: 100% (259/259), done.  
Building bitmaps: 100% (30/30), done.  
Total 259 (delta 58), reused 191 (delta 25), pack-reused 0  
Completely finished after 4.86 seconds.  
Enumerating objects: 259, done.  
cd /tmp && rm \-rf repo-clean && git clone \--bare https://github.com/PlayfulProcess/grammar-vault.git repo-clean && cd repo-clean && echo 'faga.alves@gmail.com==\>REDACTED' \> /tmp/replace-text.txt && printf 'PlayfulProcess \<17236172+PlayfulProcess@users.noreply.github.com\> \<faga.alves@gmail.com\>\\n' \> /tmp/mailmap.txt && git filter-repo \--mailmap /tmp/mailmap.txt \--replace-text /tmp/replace-text.txt \--replace-message /tmp/replace-text.txt \--force && git remote add origin https://github.com/PlayfulProcess/grammar-vault.git && git push origin \--mirror \--force

Writing objects: 100% (259/259), 157.89 MiB | 1.02 MiB/s, done.  
Total 259 (delta 0), reused 0 (delta 0), pack-reused 259  
remote: Resolving deltas: 100% (58/58), done.  
To https://github.com/PlayfulProcess/jongu-7rays-visualization.git  
 \+ b56cc62...c50da5f 7rays-visualization \-\> 7rays-visualization (forced update)  
 \+ be14103...be8cee7 dev \-\> dev (forced update)  
 \+ 220fabb...c38982c dev-phase1-templates \-\> dev-phase1-templates (forced update)  
 \+ 7781e10...55c0221 main \-\> main (forced update)  
 \+ 2352c0f...f071ba2 new-arch \-\> new-arch (forced update)  
faga\_alves@cloudshell:/tmp/repo-clean$ cd /tmp && rm \-rf repo-clean && git clone \--bare https://github.com/PlayfulProcess/grammar-vault.git repo-clean && cd repo-clean && echo 'faga.alves@gmail.com==\>REDACTED' \> /tmp/replace-text.txt && printf 'PlayfulProcess \<17236172+PlayfulProcess@users.noreply.github.com\> \<faga.alves@gmail.com\>\\n' \> /tmp/mailmap.txt && git filter-repo \--mailmap /tmp/mailmap.txt \--replace-text /tmp/replace-text.txt \--replace-message /tmp/replace-text.txt \--force && git remote add origin https://github.com/PlayfulProcess/grammar-vault.git && git push origin \--mirror \--force  
Cloning into bare repository 'repo-clean'...  
remote: Enumerating objects: 123, done.  
remote: Counting objects: 100% (123/123), done.  
remote: Compressing objects: 100% (116/116), done.  
remote: Total 123 (delta 55), reused 5 (delta 2), pack-reused 0 (from 0\)  
Receiving objects: 100% (123/123), 114.98 KiB | 1.88 MiB/s, done.  
Resolving deltas: 100% (55/55), done.  
NOTICE: Removing 'origin' remote; see 'Why is my origin removed?'  
        in the manual if you want to push back there.  
        (was https://github.com/PlayfulProcess/grammar-vault.git)  
Parsed 29 commits  
New history written in 0.16 seconds; now repacking/cleaning...  
Repacking your repo and cleaning out old unneeded objects  
Enumerating objects: 123, done.  
Counting objects: 100% (123/123), done.  
Delta compression using up to 4 threads  
Compressing objects: 100% (94/94), done.  
Writing objects: 100% (123/123), done.  
Building bitmaps: 100% (29/29), done.  
Total 123 (delta 66), reused 50 (delta 24), pack-reused 0  
Completely finished after 0.29 seconds.  
Enumerating objects: 123, done.  
Writing objects: 100% (123/123), 114.47 KiB | 114.47 MiB/s, done.  
Total 123 (delta 0), reused 0 (delta 0), pack-reused 123  
remote: Resolving deltas: 100% (66/66), done.  
To https://github.com/PlayfulProcess/grammar-vault.git  
 \+ 8c0374f...1806f56 claude/fix-orphaned-cards-metadata-C06E5 \-\> claude/fix-orphaned-cards-metadata-C06E5 (forced update)  
 \+ 4102aa8...2defb92 main \-\> main (forced update)  
faga\_alves@cloudshell:/tmp/repo-clean$   
faga\_alves@cloudshell:/tmp/repo-clean$   
faga\_alves@cloudshell:/tmp/repo-clean$ rm \-rf /tmp/repo-clean /tmp/eco-schemas-clean /tmp/replace-text.txt /tmp/mailmap\*.txt && history \-c && history \-w  
faga\_alves@cloudshell:/tmp/repo-clean$ 

