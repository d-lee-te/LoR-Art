# LoR-Art
Grabbing the backgrounds of the LoR game, so I can have cool laptop backgrounds
## Process and Thoughts
While working on a couple of other things, I realized that LoR probably isn't going to recieve more sets, and I absolutely love the art. [SixMoreVodka](https://www.sixmorevodka.com/home) really did fantastic work, and since my laptop can't run the wallpapers I like using on Wallpaper Engine, I decided the next best step was to grab all of the amazing art done to use as a background for my laptop.

I actually already did this like two years ago, but I must have deleted the script, I decided I should quickly make it again. xp

To do this, I went to the [LoR API page](https://developer.riotgames.com/docs/lor) and grabbed all of the art from each set. 
I wanted to save a step, so I went ahead and extracted all of the zips and threw them into a folder with my script. 

The goal here is to grab all of the full arts with none of the attack or health values for the cards and none of the descriptions for the spells.
I also didn't really want any of the alternate full arts since they were pretty much identical to the actual full arts.


### File Traversal
It's been a second since I've done some python File IO travesal. Thankfully, print statements exist and google exist.

What I needed for this small script:
- os.getcwd() to check my current working directory
- os.path.join() so I could go to new directories and access files
- os.chdir() to change my working directory
- os.makedirs() so I could check if I had made a file

I basically just went through each set, went into the img folder, and then checked each img's file name.

### Filtering Images
Like I said earlier, I wanted to grab just the actual full arts. To do that though, I needed to avoid the alternate arts, the icons, and anything with an actual value.

Grabbing full arts are pretty simple. You check the filename of the image and see if it has 'full' in its file name. You can also check to see if the filename to see if it's an 'alt' or not.

Now you run it, and you realize that you have a bunch of icons in the folder with everything else. Oops.

I was split for a little bit on whether to use another python module to check for each pic's dimensions to see if it would qualify as a full art, but then I decided the easier way to do this was to just compare file size. The full arts are obviously going to be bigger than the icons. It was just a matter of figuring out how much bigger.

I went through a couple of full arts in the first set, and I can see that all of them seem to be bigger than a mb. Easy-peasy. 

Just to check to see if each image is bigger than 1mb, and it works!

### Copying the pics
For a little bit, I was stuck between whether I wanted to delete/empty each set to just keep each set or to keep all of the sets as they were and to copy the files I cared about into a seperate folder.

I went with the latter. That said, I hadn't really done a copy/paste operation with python before.

I figured it couldn't be that bad, and what do you know: Python has another built-in module for things like this. All you need is the file path for where the pic is and another file path for where you want it to go. 

So I went ahead and imported shutil, and copied it through and through.

## Final Notes
I liked LoR. The turns were a little long, but I really want LoR to make a comeback somehow someway. Until then, I will stare at the peak art made for this game on my laptop background.
