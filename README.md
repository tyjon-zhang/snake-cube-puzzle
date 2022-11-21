# snake-cube-puzzle
Solution of any 3*3*3 snake cube puzzle

It's the puzzle look like [this](http://web.cecs.pdx.edu/~mpj/snakecube/snake.png)

Step1: Make the snake of cube into a two-dimensional line.

Like [this](https://i.etsystatic.com/5295493/r/il/d7b3ac/647840466/il_570xN.647840466_j15z.jpg)

Step2: Enter the count of cubes at between each rectangle turn(Note: the cubes of rectangle are counted repeatly).

For example, what you have to enter according to the picture above is

```
3 2 2 3 2 3 2 2 3 3 2 2 2 3 3 3 3
```

What to use to separate the numbers is not matter, as long as it's common, like space```" "```, tab```"\t"```, and comma```","```

Don't use enter```"\n"```

Then you will get your solution

e.g.

```
please, reshape it into a line, enter the num between each rectangle(separate with space):3 2 2 3 2 3 2 2 3 3 2 2 2 3 3 3 3
■ ■ ■ 
    ■ ■ 
      ■
      ■ ■ 
        ■
        ■ ■ 
          ■ ■ ■ 
              ■
              ■ ■ 
                ■ ■ 
                  ■
                  ■ ■ ■ 
                      ■
                      ■ ■ ■ 
[1, 1, 1] 
[2, 1, 1] right ->️
[3, 1, 1] right ->️
[3, 2, 1] up ^
[2, 2, 1] left <-️
[2, 2, 2] front(to yourself)
[2, 2, 3] front(to yourself)
[2, 3, 3] up ^
[2, 3, 2] back (away from yourself️
[2, 3, 1] back (away from yourself️
[3, 3, 1] right ->️
[3, 3, 2] front(to yourself)
[3, 2, 2] down v
[3, 1, 2] down v
[2, 1, 2] left <-️
[1, 1, 2] left <-️
[1, 2, 2] up ^
[1, 2, 1] back (away from yourself️
[1, 3, 1] up ^
[1, 3, 2] front(to yourself)
[1, 3, 3] front(to yourself)
[1, 2, 3] down v
[1, 1, 3] down v
[2, 1, 3] right ->️
[3, 1, 3] right ->️
[3, 2, 3] up ^
[3, 3, 3] up ^
```
