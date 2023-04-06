import tkinter as tk

root = tk.Tk()

#상단 프레임 생성
top_frame = tk.Frame(root, bg="#663399", width=400,height=50)
top_frame.pack(side="top",fill='both')

# 좌 프레임 생성
left_frame = tk.Frame(root, bg='#663399', width=200, height=400, bd=3)
left_frame.pack(side='left')

# 좌 프레임에 버튼 배치
left_button = tk.Button(left_frame, text='BANPICK TOOL', font=('Arial', 14), bg='#663399')
left_button.place(relx=0.5, rely=0.5, anchor='center')

# 우 프레임 생성
right_frame = tk.Frame(root, bg='#663399', width=200, height=400)

# 우 프레임에 버튼 배치
right_button = tk.Button(right_frame, text='ANALYZING TOOL', font=('Arial', 14), bg='#663399')
right_button.place(relx=0.5, rely=0.5, anchor='center')

# 우 프레임을 윈도우 오른쪽에 위치시킴
right_frame.pack(side='right')


# 상단 라벨 생성
top_label = tk.Label(top_frame, text='BACK LCK ANALYZER', font=('Arial', 16, 'bold'), bg='#663399', fg='white')
top_label.pack(side='top', fill='x')

root.mainloop()
