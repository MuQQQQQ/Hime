import tkinter
import time
import pickle

path = "E:/pics/"
def start(player,strings,start_button):
    count = 1
    start_button['text'] = 'hso!'
    start_t = time.time()
    for each in strings:
        t = 1/30 * count - time.time() + start_t
        if t>0:
            time.sleep(t)
        player['text'] = each
        window.update()
        count += 1
    print(time.time()-start_t)

with open(path+'0.dat', 'rb') as fp:
    strings = pickle.load(fp)
window = tkinter.Tk()
window.title('WTMSB!')
window.geometry('1500x720')
player = tkinter.Label(window,bg = 'black', fg = 'white', font = ('Verdana 10 bold', 8))                                             
player.place(x = 10, y = 50)
start_button = tkinter.Button(window, text = 'Start', command = lambda: start(player,strings,start_button))
start_button.place(x = 750, y = 0)
window.mainloop()
