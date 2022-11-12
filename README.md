This is repo of assignment1 of instro for AI
# The syntax to run program
> Cd to the folder that contain the main.py
> Run command: python3 main.py + options (below)
- For water-sort problem:
```
python3 main.py water-sort all-level a-start visualize
```
- For bloxorz prolblem:
```
python3 main.py bloxorz all-level a-start visualize
```

The synxtax of the program with optional ror water-sort (The visualize option maybe empty but another options must be select one in the list or select all list for each game):
```
python3 main.py water-sort [all-level, level-1, level-2,..] [dfs, bfs, a-start] [visualize,]

python3 main.py bloxorz [all-level, level-1, level-2,..] [dfs, bfs, genertic] [visualize,]
```

- Example water-sort:

```
python3 main.py water-sort level-1 dfs visualize
python3 main.py water-sort level-2 bfs visualize
python3 main.py water-sort level-2 a-start visualize
```


- Example bloxorz:
```
python3 main.py bloxorz level-1 dfs visualize
python3 main.py bloxorz level-2 bfs visualize
python3 main.py bloxorz level-2 genertic visualize
```
# The data in the game
The data of configuration of the game in:

`./data/data-bloxorz.json for bloxorz game.`

`./data/data-water.json for water-sort game`

> The Data will be loaded in load_data.py srcipt file. 

> Plase set configuration match with that format to make new level in game.