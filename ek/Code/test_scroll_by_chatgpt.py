import tkinter as tk

root = tk.Tk()

# 스크롤바 생성
scrollbar = tk.Scrollbar(root, orient='vertical')
scrollbar.pack(side='right', fill='y')

# 스크롤 가능한 Canvas 위젯 생성
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.pack(side='left', fill='both', expand=True)

# 스크롤바와 Canvas 위젯 연결
scrollbar.config(command=canvas.yview)

# 스크롤 가능한 영역으로 사용할 Frame 생성
scrollable_frame = tk.Frame(canvas)

# Frame에 내용 삽입
for i in range(50):
    tk.Label(scrollable_frame, text=f'This is label #{i}').pack()

# Canvas 위젯에 Frame 삽입
canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')

# 스크롤바에도 Canvas 위젯 연결
scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

root.mainloop()
