## Russian E-book Downloader

Helps you to download e-books in bulk. 

### Usage 

```
$ python rbd.py -h
```

+ Genres (**--genre**)

   * detective
   * det_action (Detective action.)
   * thriller
   * dramaturgy
   * computers 
   * love_history 
   * sci_popular
   * network_literature (Books published by independent writers.)

+ Start and End numbers (**--start_number** and **--end_number**)

    The script checks all e-books in specified genre and returns a list. (Newest to the oldest)
    *Start number* and *end number* specifies the range of indicies to be 
     downloaded.
   
   For example; if given --start_number 50 --end_number 100, script will download from the 50th to the 100th book
   in the chronological order.
   
+ Save directory (**--dir**)
   
   Which path to save the downloaded books.
   
+ File types (**--file_type**)
   
   Supported file types; **fb2**,**epub**, **mobi**,**pdf**.
   
   Recommended file types; **fb2** and **epub**.
