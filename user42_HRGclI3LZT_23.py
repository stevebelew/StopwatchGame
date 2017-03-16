# template for "Stopwatch: The Game"
import simplegui

# define global variables
count = 0
wins = 0
tries = 0
timer_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    minutes = t//600
    tens_seconds = ((t//10) %60)//10
    seconds = int (((t / 10) % 10) % 60)
    tenths = t % 10
    return str(minutes) + ':' + str(tens_seconds) + str(seconds) + '.' + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def reset():
    global wins
    global tries
    global count
    global timer_running
    timer_running = False   
    timer.stop()
    count = 0
    tries = 0
    wins = 0
    
    
def start():
    global tries
    global timer_running
    timer_running = True
    timer.start()
    tries += 1
    
def stop():
    global wins
    timer.stop()
    global timer_running
    if count % 10 == 0 and  timer_running == True:
        wins += 1
    timer_running = False   
    
# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1
    
# define draw handler
def draw(canvas):
    global count
    global wins
    global tries
    canvas.draw_text(format(count), (40, 120), 48, 'Red') 
    canvas.draw_text(str(wins) + ' / ' + str(tries), (150, 20), 18, 'Green')  
    
# create frame
frame = simplegui.create_frame('Testing', 200, 200, 300)

# register event handlers
start_button = frame.add_button('Start',start)
stop_button = frame.add_button('Stop', stop)
reset_button = frame.add_button('Reset', reset)
timer = simplegui.create_timer(100,tick)
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
