from tkinter import *
import math
from enum import Enum

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#TIMER STATES
class TimerState(Enum):
    WORK = 1
    SHORT_BREAK = 2
    LONG_BREAK = 3

#TIMER CLASS
class PomodoroTimer:
    def __init__(self, window):
        self.window = window
        self.timer_state = TimerState.WORK
        self.reps = 0
        self.timer = None

        #UI setup
        self.setup_ui()
    
# label displaying the current timer state (work, short break, long break)
    def setup_ui(self):
        self.title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, FONT=(FONT_NAME, 50))
        self.title_label.grid(column=1, row=0)

        # canvas to display the tomato and timer
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

        # button to start the timer
        self.start_button = Button(text="start", highlightthickness=0, command=self.start_timer)
        self.start_button.grid(column=0, row=2)

        # button to reset the timer
        self.reset_button = Button(text="reset", highlightthickness=0, command=self.start_timer)
        self.reset_button.grid(column=1, row=3)

        #Label to display checkmarks for completed work sessions
        self.check_marks = Label(fg=GREEN, bg=YELLOW)
        self.check_marks.grid(column=1, row=3)

    def reset_timer(self):
        #reset the timer UI elements
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="Timer")
        self.check_marks.config(text="")
        self.reps=0
    
    def start_timer(self):
        #start the timer based on the current timer state
        self.reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN *60
        long_break_sec = LONG_BREAK_MIN * 60

        if self.reps % 8 == 0:
            self.count_down(long_break_sec, TimerState.LONG_BREAK)
        elif self.reps %2 == 0:
            self.count_down(short_break_sec, TimerState.SHORT_BREAK)
        else:
            self.count_down(work_sec, TimerState.WORK)
    
    def count_down(self, count, state):
        # countdown mechanism
        count_min = math.floor(count / 60)
        count_sec = count & 60
        count_sec_str = str(count_sec.zfill(2))

        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec_str}")

        if count > 0:
            #contine count down
            self.timer = self.window.after(1000, self.count_down, count - 1, state)

#UI Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#CREATE AN INSTATNCE OF THE TIMER!
pomodoro_timer = PomodoroTimer(window)

window.mainloop()


    


