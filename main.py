import tkinter
from urllib.request import urlopen

from PIL import Image
import requests
from io import BytesIO
import copy
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from cmu_112_graphics import *
import time
import urllib.request
import webbrowser
from PIL import Image
from reddit     import *
from twitter import *
from youtube import *
from instagram import *


def appStarted(app):
    app.testing = 0
    # app.reddit = scrapeReddit()
    app.redditColors = ['#6C7A89'] * 7
    # app.twitter = scrapeTwitter()
    app.twitterColors = ['#003171'] * 7
    app.twitterTextColors = ['black'] * 7
    # app.youtube = scrapeYoutube()
    app.youtubeColors = ['#E68364'] * 6
    app.youtubeTextColors = ['black'] * 6
    app.instaColors = ['#ffe6e6'] * 3
    # app.insta = scrapeInsta()
    # animations
    app.r1, app.r2, app.r3, app.r4 = 1, 1, 1, 1
    app.animateColors = ['white'] * 4
    app.headerColors = ['#6C7A89', '#22A7F0', '#E68364', '#D24D57']
    # custom cursor
    # app.cursor_radius = 5
    # app.cursor_fill = '#D9B611'
    # app.cursor_x, app.cursor_y = -1, -1


    app.reddit = []
    app.twitter = []
    app.youtube = []
    app.insta = []

    
def mousePressed(app,event):
    if (event.x<205):
        if(40<event.y<60):
            if app.reddit == []:
                app.reddit = scrapeReddit()
        elif (490<event.y<510):
            if app.youtube == []:
                app.youtube = scrapeYoutube()
                app.thumbnails = []
                for i in range(6):
                    thumbnail = app.youtube[i][2]
                    app.thumbnails.append(thumbnail)
                    urllib.request.urlretrieve(f'{app.youtube[i][2]}',f"./images/yt{i}.png")    
                    image = Image.open(f"../hack112/images/yt{i}.png")
                    newSize = (227,128)
                    im2 = image.resize(newSize) 
                    im2.save(f"../hack112/images/yt{i}.png")
                app.images_temp = [app.loadImage(thumbnail) for thumbnail in app.thumbnails]
                app.images = [app.scaleImage(image, 0.1771) for image in app.images_temp]
                
                
        #return
    elif (820<event.x<1005):
        if(40<event.y<60):
            if app.twitter == []:
                app.twitter = scrapeTwitter()
        elif (490<event.y<510):
            if app.insta == []:
                app.insta = scrapeInsta()
    
    # Links
    # Reddit
    if app.reddit != []:
        if 30 <= event.x <= 770 and 65 <= event.y <= 103:
            webbrowser.open(app.reddit[0][3])
        elif 30 <= event.x <= 770 and 118 <= event.y <= 156:
            webbrowser.open(app.reddit[1][3])
        elif 30 <= event.x <= 770 and 171 <= event.y <= 209:
            webbrowser.open(app.reddit[2][3])
        elif 30 <= event.x <= 770 and 224 <= event.y <= 262:
            webbrowser.open(app.reddit[3][3])
        elif 30 <= event.x <= 770 and 277 <= event.y <= 315:
            webbrowser.open(app.reddit[4][3])
        elif 30 <= event.x <= 770 and 330 <= event.y <= 368:
            webbrowser.open(app.reddit[5][3])
        elif 30 <= event.x <= 770 and 383 <= event.y <= 421:
            webbrowser.open(app.reddit[6][3])

    # Twitter
    if app.twitter != []:
        if 830 <= event.x <= 1570 and 65 <= event.y <= 103:
            webbrowser.open(app.twitter[0][3])
        if 830 <= event.x <= 1570 and 118 <= event.y <= 156:
            webbrowser.open(app.twitter[1][3])
        if 830 <= event.x <= 1570 and 171 <= event.y <= 209:
            webbrowser.open(app.twitter[2][3])
        if 830 <= event.x <= 1570 and 224 <= event.y <= 262:
            webbrowser.open(app.twitter[3][3])
        if 830 <= event.x <= 1570 and 277 <= event.y <= 315:
            webbrowser.open(app.twitter[4][3])
        if 830 <= event.x <= 1570 and 330 <= event.y <= 368:
            webbrowser.open(app.twitter[5][3])
        if 830 <= event.x <= 1570 and 383 <= event.y <= 421:
            webbrowser.open(app.twitter[6][3])

    # Youtube
    if app.youtube != []:
        if 30 <= event.x <= 256.67 and 508 <= event.y <= 685.5:  # 1
            webbrowser.open(app.youtube[0][3])
        if 286.67 <= event.x <= 513.34 and 508 <= event.y <= 685.5:  # 2
            webbrowser.open(app.youtube[1][3])
        if 543.34 <= event.x <= 770 and 508 <= event.y <= 685.5:  # 3
            webbrowser.open(app.youtube[2][3])
        if 30 <= event.x <= 256.67 and 703 <= event.y <= 880.5:  # 4
            webbrowser.open(app.youtube[3][3])
        if 286.67 <= event.x <= 513.34 and 703 <= event.y <= 880.5:  # 5
            webbrowser.open(app.youtube[4][3])
        if 543.34 <= event.x <= 770 and 703 <= event.y <= 880.5:  # 6
            webbrowser.open(app.youtube[5][3])
    
    #Insta
    if app.insta != []:
        if 800+30 <= event.x <= 800+256.67 and 515 <= event.y <= 861.67:  # 1
            webbrowser.open(app.insta[0][3])
        if 800+286.67 <= event.x <= 800+513.34 and 515 <= event.y <= 861.67:  # 2
            webbrowser.open(app.insta[1][3])
        if 800+543.34 <= event.x <= 800+770 and 515 <= event.y <= 861.67:  # 3
            webbrowser.open(app.insta[2][3])





def mouseMoved(app, event):
    # custom cursor
    # app.cursor_x = event.x
    # app.cursor_y = event.y

    # reddit header animation
    middle = app.width/4
    height = 30
    if middle-50 <= event.x <= middle+50 and height-20 <= event.y <= height+20:
        app.animateColors[0] = ['#BFBFBF']
        app.r1 = 27
        app.headerColors[0] = 'black'
    else:
        app.animateColors[0] = ['white']
        app.r1 = 1
        app.headerColors[0] = '#6C7A89'

    # twitter header animation
    middle2 = app.width/4 * 3
    height2 = 30
    if middle2-50 <= event.x <= middle2+50 and height2-20 <= event.y <= height2+20:
        app.animateColors[1] = ['#003171']
        app.r2 = 27
        app.headerColors[1] = 'white'
    else:
        app.animateColors[1] = ['white']
        app.r2 = 1
        app.headerColors[1] = '#22A7F0'

    # youtube header animation
    middle3 = app.width/4
    height3 = app.height/2 + 30
    if middle3-50 <= event.x <= middle3+50 and height3-20 <= event.y <= height3+20:
        app.animateColors[2] = ['#CF000F']
        app.r3 = 27
        app.headerColors[2] = 'white'
    else:
        app.animateColors[2] = ['white']
        app.r3 = 1
        app.headerColors[2] = '#E68364'

    # twitter header animation
    middle4 = app.width/4 * 3
    height4 = app.height/2 + 30
    if middle4-50 <= event.x <= middle4+50 and height4-20 <= event.y <= height4+20:
        app.animateColors[3] = ['#FBCACA']
        app.r4 = 27
        app.headerColors[3] = 'black'
    else:
        app.animateColors[3] = ['white']
        app.r4 = 1
        app.headerColors[3] = '#D24D57'


    # reddit colors
    if 30 <= event.x <= 770 and 65 <= event.y <= 103:
        app.redditColors[0] = '#6C7A89'
    else:
        app.redditColors[0] = '#95A5A6'
    if 30 <= event.x <= 770 and 118 <= event.y <= 156:
        app.redditColors[1] = '#6C7A89'
    else:
        app.redditColors[1] = '#95A5A6'
    if 30 <= event.x <= 770 and 171 <= event.y <= 209:
        app.redditColors[2] = '#6C7A89'
    else:
        app.redditColors[2] = '#95A5A6'
    if 30 <= event.x <= 770 and 224 <= event.y <= 262:
        app.redditColors[3] = '#6C7A89'
    else:
        app.redditColors[3] = '#95A5A6'
    if 30 <= event.x <= 770 and 277 <= event.y <= 315:
        app.redditColors[4] = '#6C7A89'
    else:
        app.redditColors[4] = '#95A5A6'
    if 30 <= event.x <= 770 and 330 <= event.y <= 368:
        app.redditColors[5] = '#6C7A89'
    else:
        app.redditColors[5] = '#95A5A6'
    if 30 <= event.x <= 770 and 383 <= event.y <= 421:
        app.redditColors[6] = '#6C7A89'
    else:
        app.redditColors[6] = '#95A5A6'

    # twitter colors
    if 830 <= event.x <= 1570 and 65 <= event.y <= 103:
        app.twitterColors[0] = '#003171'
        app.twitterTextColors[0] = 'white'
    else:
        app.twitterColors[0] = '#22A7F0'
        app.twitterTextColors[0] = 'black'
    if 830 <= event.x <= 1570 and 118 <= event.y <= 156:
        app.twitterColors[1] = '#003171'
        app.twitterTextColors[1] = 'white'
    else:
        app.twitterColors[1] = '#22A7F0'
        app.twitterTextColors[1] = 'black'
    if 830 <= event.x <= 1570 and 171 <= event.y <= 209:
        app.twitterColors[2] = '#003171'
        app.twitterTextColors[2] = 'white'
    else:
        app.twitterColors[2] = '#22A7F0'
        app.twitterTextColors[2] = 'black'
    if 830 <= event.x <= 1570 and 224 <= event.y <= 262:
        app.twitterColors[3] = '#003171'
        app.twitterTextColors[3] = 'white'
    else:
        app.twitterColors[3] = '#22A7F0'
        app.twitterTextColors[3] = 'black'
    if 830 <= event.x <= 1570 and 277 <= event.y <= 315:
        app.twitterColors[4] = '#003171'
        app.twitterTextColors[4] = 'white'
    else:
        app.twitterColors[4] = '#22A7F0'
        app.twitterTextColors[4] = 'black'
    if 830 <= event.x <= 1570 and 330 <= event.y <= 368:
        app.twitterColors[5] = '#003171'
        app.twitterTextColors[5] = 'white'
    else:
        app.twitterColors[5] = '#22A7F0'
        app.twitterTextColors[5] = 'black'
    if 830 <= event.x <= 1570 and 383 <= event.y <= 421:
        app.twitterColors[6] = '#003171'
        app.twitterTextColors[6] = 'white'
    else:
        app.twitterColors[6] = '#22A7F0'
        app.twitterTextColors[6] = 'black'

    # youtube colors
    if 30 <= event.x <= 256.67 and 508 <= event.y <= 685.5:  # 1
        app.youtubeColors[0] = '#CF000F'
        app.youtubeTextColors[0] = 'white'
    else:
        app.youtubeColors[0] = '#E68364'
        app.youtubeTextColors[0] = 'black'
    if 286.67 <= event.x <= 513.34 and 508 <= event.y <= 685.5:  # 2
        app.youtubeColors[1] = '#CF000F'
        app.youtubeTextColors[1] = 'white'
    else:
        app.youtubeColors[1] = '#E68364'
        app.youtubeTextColors[1] = 'black'
    if 543.34 <= event.x <= 770 and 508 <= event.y <= 685.5:  # 3
        app.youtubeColors[2] = '#CF000F'
        app.youtubeTextColors[2] = 'white'
    else:
        app.youtubeColors[2] = '#E68364'
        app.youtubeTextColors[2] = 'black'
    if 30 <= event.x <= 256.67 and 703 <= event.y <= 880.5:  # 4
        app.youtubeColors[3] = '#CF000F'
        app.youtubeTextColors[3] = 'white'
    else:
        app.youtubeColors[3] = '#E68364'
        app.youtubeTextColors[3] = 'black'
    if 286.67 <= event.x <= 513.34 and 703 <= event.y <= 880.5:  # 5
        app.youtubeColors[4] = '#CF000F'
        app.youtubeTextColors[4] = 'white'
    else:
        app.youtubeColors[4] = '#E68364'
        app.youtubeTextColors[4] = 'black'
    if 543.34 <= event.x <= 770 and 703 <= event.y <= 880.5:  # 6
        app.youtubeColors[5] = '#CF000F'
        app.youtubeTextColors[5] = 'white'
    else:
        app.youtubeColors[5] = '#E68364'
        app.youtubeTextColors[5] = 'black'

    # insta colors      ffe6e6
    if 800+30 <= event.x <= 800+256.67 and 515 <= event.y <= 861.67:  # 1
        app.instaColors[0] = '#ffb3b3'
    else:
        app.instaColors[0] = '#ffe6e6'
    if 800+286.67 <= event.x <= 800+513.34 and 515 <= event.y <= 861.67:  # 2
        app.instaColors[1] = '#ffb3b3'
    else:
        app.instaColors[1] = '#ffe6e6'
    if 800+543.34 <= event.x <= 800+770 and 515 <= event.y <= 861.67:  # 3
        app.instaColors[2] = '#ffb3b3'
    else:
        app.instaColors[2] = '#ffe6e6'


def redrawAll(app, canvas):
    vertical_divide = app.width / 2
    horizontal_divide = app.height / 2
    # 4-section dividers
    canvas.create_line(vertical_divide, 0, vertical_divide, app.height, width=2)
    canvas.create_line(0, horizontal_divide, app.width, horizontal_divide, width=2)
    # animated circles
    canvas.create_oval(vertical_divide / 2 - 2 * app.r1, 30 - app.r1, vertical_divide / 2 + 2 * app.r1,
                       30 + app.r1, width=0, fill=app.animateColors[0])
    canvas.create_oval(vertical_divide / 2 * 3 - 2 * app.r2, 30 - app.r2, vertical_divide / 2 * 3 + 2 * app.r2,
                       30 + app.r2, width=0, fill=app.animateColors[1])
    extra_margin = 15
    canvas.create_oval(vertical_divide / 2 - 2 * app.r3 - extra_margin, horizontal_divide + 30 - app.r3,
                       vertical_divide / 2 + 2 * app.r3 + extra_margin, horizontal_divide + 30 + app.r3, width=0,
                       fill=app.animateColors[2])
    extra_margin2 = 27
    canvas.create_oval(vertical_divide / 2 * 3 - 2 * app.r4 - extra_margin2, horizontal_divide + 30 - app.r4,
                       vertical_divide / 2 * 3 + 2 * app.r4 + extra_margin2,
                       horizontal_divide + 30 + app.r4, width=0, fill=app.animateColors[3])
    # section headers
    canvas.create_text(vertical_divide / 2, 30, text='Reddit', font=('Bold', '30'),
                       fill=app.headerColors[0])
    canvas.create_text(vertical_divide / 2 * 3, 30, text='Twitter', font=('Bold', '30'),
                       fill=app.headerColors[1])
    canvas.create_text(vertical_divide / 2, horizontal_divide+30, text='YouTube', font=('Bold', '30'),
                       fill=app.headerColors[2])
    canvas.create_text(vertical_divide / 2 * 3, horizontal_divide+30, text='Instagram', font=('Bold', '30'),
                       fill=app.headerColors[3])
    # rectangles
    height, gap = 38, 15
    x, y = 30, 50
    reddit_text_locations = []
    i = 0
    twitter_lengths = [195, 320]
    while y + height < horizontal_divide - 20:
        if app.reddit != []:
            canvas.create_rectangle(x, y + gap, vertical_divide - 30, y + height + gap, width=0, fill=app.redditColors[i])
            canvas.create_rectangle(170, y + gap, 200, y + height + gap, fill='white', width=0)  # used to be 200-230
        if app.twitter != []:
            canvas.create_rectangle(vertical_divide + 30, y + gap, app.width - 30, y + height + gap, width=0,
                                    fill=app.twitterColors[i])
            canvas.create_rectangle(vertical_divide + twitter_lengths[0] - 30, y + gap,
                                    vertical_divide + twitter_lengths[0], y + height + gap, fill='white', width=0)
            canvas.create_rectangle(vertical_divide + twitter_lengths[1] - 30, y + gap,
                                    vertical_divide + twitter_lengths[1], y + height + gap, fill='white', width=0)
        reddit_text_locations.append((y + gap + y + height + gap) / 2)
        y += height + gap
        i += 1


    if(app.reddit != []):
        for i in range(7):
            # reddit
            sub = app.reddit[i][1]
            if len(sub) > 17:
                sub = sub[:14].rstrip() + '...'
            title = app.reddit[i][0]
            max_title = 86
            if len(title) > max_title:
                title = title[:max_title - 3].rstrip() + '...'
            canvas.create_text(45, reddit_text_locations[i], text=sub, font='15', anchor=tkinter.W)
            canvas.create_text(215, reddit_text_locations[i], text=title, font='15', anchor=tkinter.W)
    else:
        canvas.create_text(114,50,text = "Click here to log in to Reddit")    
            
            
    # twitter
    if(app.twitter != []):
        for i in range(7):
            name = app.twitter[i][0]
            if len(name) > 16:
                name = name[:13].rstrip() + '...'
            handle = app.twitter[i][1]
            if len(handle) > 10:
                handle = handle[:7].rstrip() + '...'
            tweet = app.twitter[i][2]
            tweet_length = 64
            if len(tweet) > tweet_length:
                tweet = tweet[:tweet_length - 3].rstrip() + '...'
            # 3 twitter sections text creation
            canvas.create_text(845, reddit_text_locations[i], text=name, font='15', anchor=tkinter.W,
                            fill=app.twitterTextColors[i])
            canvas.create_text(800 + twitter_lengths[0] + 15, reddit_text_locations[i], text=handle, font='15',
                            anchor=tkinter.W, fill=app.twitterTextColors[i])
            canvas.create_text(800 + twitter_lengths[1] + 15, reddit_text_locations[i], text=tweet, font='15',
                            anchor=tkinter.W, fill=app.twitterTextColors[i])
    else:
        canvas.create_text(914,50,text = "Click here to log in to Twitter") 


    # youtube
    if app.youtube != []:
        vidnames = []
        for i in range(6):
            im2 = Image.open(f"../hack112/images/yt{i}.png")
            vidname = app.youtube[i][0]
            max_vidname = 32
            if vidname.isupper():
                vidname = vidname[:max_vidname-7].rstrip() + '...'
            elif len(vidname) > max_vidname:
                vidname = vidname[:max_vidname-3].rstrip() + '...'
            vidnames.append(app.youtube[i][0])
            creator = '(' + app.youtube[i][1] + ')'
            thumbnail = app.youtube[i][2]
            link = app.youtube[i][3]

            # testing youtube box sizes
            youtube_width = 226.67
            youtube_height = 127.55
            margin = 5
            shift = 7
            temp_x = [30, 30+youtube_width+30, 30+2*(youtube_width+30),30, 30+youtube_width+30, 30+2*(youtube_width+30)]
            
            # first row
            x = temp_x[i]
            if i < 3:
                canvas.create_rectangle(x, horizontal_divide+65-shift, x+youtube_width,
                                        horizontal_divide+65+youtube_height-shift,
                                        fill='grey', width=0)
                canvas.create_image(x, horizontal_divide+65-shift, image=ImageTk.PhotoImage(im2),
                                    anchor=tkinter.NW)
                # vidname title text
                canvas.create_rectangle(x, horizontal_divide+192.5+margin-shift, x+youtube_width,
                                        horizontal_divide+192.5+margin+45-shift,
                                        fill=app.youtubeColors[i], width=0)  # 192.5 = 65 + 127.5
                canvas.create_text(x+10, (horizontal_divide+192.5+margin-shift)+13,
                                text=vidname, font='5', fill=app.youtubeTextColors[i], anchor=tkinter.W)
                canvas.create_text(x+10, (horizontal_divide+192.5+margin-shift)+32,
                                text=creator, font='5', fill=app.youtubeTextColors[i], anchor=tkinter.W)
            # second row
            canvas.create_rectangle(x, horizontal_divide+260-shift, x+youtube_width,
                                    horizontal_divide+260+youtube_height-shift,
                                    fill='grey', width=0)
            canvas.create_image(x, horizontal_divide+260-shift, image=ImageTk.PhotoImage(im2),
                                anchor=tkinter.NW)
            canvas.create_rectangle(x, horizontal_divide+387.5+margin-shift, x+youtube_width,
                                    horizontal_divide+387.5+margin+45-shift,
                                    fill=app.youtubeColors[i], width=0)  # 260 + 127.5 = 387.5
            canvas.create_text(x+10, (horizontal_divide+387.5+margin-shift)+13,
                            text=vidname, font='5', fill=app.youtubeTextColors[i], anchor=tkinter.W)
            canvas.create_text(x+10, (horizontal_divide+387.5+margin-shift)+32,
                            text=creator, font='5', fill=app.youtubeTextColors[i], anchor=tkinter.W)
    else:
        canvas.create_text(114,500,text="Click here to log in to YouTube")

    # instagram

    if app.insta != []:
        for i in range(3):
            # testing instagram box sizes
            urllib.request.urlretrieve(
                f'{app.insta[i][2]}',f"./images/{i}.png")    
            image = Image.open(f"../hack112/images/{i}.png")
            newSize = (227,227)
            im2 = image.resize(newSize) 
            insta_size = 226.67
            shift, margin = -5, 25
            temp_x = [x+vertical_divide for x in [30, 30+insta_size+30, 30+2*(insta_size+30)]]
            x = temp_x[i]
            #canvas.create_rectangle(x, horizontal_divide+65-shift, x+insta_size,
            #                        horizontal_divide+65+insta_size-shift,
            #                        fill='grey', width=0)
            canvas.create_rectangle(x, horizontal_divide+291.67+margin-shift, x+insta_size,
                                    horizontal_divide+291.67+margin+90-shift,
                                    fill=app.instaColors[i], width=0)  # 291.67 = 65 + 226.67
            canvas.create_image(x+113, horizontal_divide+178-shift, image=ImageTk.PhotoImage(im2))


            # captions
            author = app.insta[i][0]
            caption = app.insta[i][1].replace('\xa0', '')
            cutoff = 30
            if len(caption) > cutoff * 2:
                first = caption[:cutoff] + '-'
                second = caption[cutoff:cutoff*2-3] + '...'
                canvas.create_text(x+15, horizontal_divide+291.67+margin-shift+35, text=first,
                                fill='black', anchor=NW)
                canvas.create_text(x+15, horizontal_divide+291.67+margin-shift+55, text=second,
                                fill='black', anchor=NW)
            elif len(caption) > cutoff:
                first = caption[:cutoff] + '-'
                second = caption[cutoff:]
                canvas.create_text(x+15, horizontal_divide+291.67+margin-shift+35, text=first,
                                fill='black', anchor=NW)
                canvas.create_text(x+15, horizontal_divide+291.67+margin-shift+55, text=second,
                                fill='black', anchor=NW)
            else:
                canvas.create_text(x+15, horizontal_divide+291.67+margin-shift+35, text=caption,
                                fill='black', anchor=NW, width=200)
            canvas.create_text(x+15, horizontal_divide+291.67+margin-shift+15, text=author,
                                    fill='black', anchor=NW, width=196.67)
    else:
        canvas.create_text(914,500,text="Click here to log in to Instagram")
    

    # custom cursor
    # canvas.create_oval(app.cursor_x-app.cursor_radius, app.cursor_y-app.cursor_radius,
    #                    app.cursor_x+app.cursor_radius, app.cursor_y+app.cursor_radius, fill=app.cursor_fill,
    #                    width=0)

def appStopped(app):
    files = "./images"
    for image in os.listdir(files):
        os.remove(f"./images/{image}")


runApp(width=1600, height=900)
