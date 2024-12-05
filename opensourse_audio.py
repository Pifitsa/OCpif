from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from pydub import AudioSegment
import pydub.effects
print("test")
print("Лёша лох")
def close_app():
    ("bnlhuy8uyfgtcdiyhghfihgyiftg")
    root.destroy()
    print('На сегодня ты наредактировался, лох')

root = Tk()  # создаем корневой объект - окно
root.title("Аудиоредактор от Владоса Темщика и Вовки ХаХалка")  # устанавливаем заголовок окна
root.geometry("800x600+200+200")  # устанавливаем размеры окна
root.resizable(False, False)
# Удаляем строку, которая устанавливает иконку
# root.iconbitmap(default='penis.ico')
root.protocol('WM_DELETE_WINDOW', close_app)

input_file_entry = Entry(width=50)
input_file_entry.place(x=15, y=15)
input_file_entry.insert(0, 'Путь к файлу')

audio_segment = None

def load_audio_file():
    global audio_segment
    filepath = filedialog.askopenfilename()
    if filepath != "":
        input_file_entry.delete(0, END)
        input_file_entry.insert(0, filepath)
        audio_segment = open_audio(filepath)
        audio_image_panel.place(x=0, y=40)
        print('Файл загружен')

def volume_changed():
    global audio_segment
    new_volume = float(volume.get())
    if audio_segment:
        audio_segment = change_volume(audio_segment, new_volume)
        print('Громкость изменена')

def speed_changed():
    global audio_segment
    new_speed = float(speed.get())
    if audio_segment:
        audio_segment = change_speed(audio_segment, new_speed)
        print('Скорость изменена')

def replace_selected_fragment():
    print('Еблан, у тебя фрагмент не удаляется!!!!ДЕБИЛОЙД')

def open_replace_window():
    replace_fragment_window = Toplevel(root)
    replace_fragment_window.title('Вырезка фрагмента')
    replace_fragment_window.geometry('300x200')

    text_lable = Label(replace_fragment_window, text='Выберите фрагмент')
    text_lable.place(x=90, y=15)

    from_entry = Entry(replace_fragment_window, width=10)
    from_entry.place(x=50, y=50)
    from_entry.insert(0, 'От')

    lable_from = Label(replace_fragment_window, text='->')
    lable_from.place(x=120, y=50)

    to_entry = Entry(replace_fragment_window, width=10)
    to_entry.place(x=150, y=50)
    to_entry.insert(0, 'До')

    confirm_button = Button(replace_fragment_window, text='Confirm', command=replace_selected_fragment)
    confirm_button.place(x=120, y=100)

def return_backward():
    print('Долбоклюй, у тебя не возвращает изменения')

def return_forward():
    print('Совсем ящер? Еще и вперед не возвращает')

def fade_in_fragment():
    print('У тебя не фейд инится')

def fade_out_fragment():
    print('У тебя не фейд аутится')

def export_file():
    global audio_segment
    filepath = filedialog.asksaveasfilename(defaultextension=".mp3")
    if filepath != "":
        if audio_segment:
            audio_segment.export(filepath, format="mp3")
            print('Файл экспортирован')
        else:
            print('Файл не загружен')

load_input_file_btn = Button(text='Загрузить', command=load_audio_file)
load_input_file_btn.place(x=330, y=12)

export_file_button = Button(text='Экспортировать', command=export_file)
export_file_button.place(x=695, y=12)

audio_image = ImageTk.PhotoImage(Image.open('dorojka1.png').resize((800, 100), Image.Resampling.BILINEAR))
audio_image_panel = Label(root, image=audio_image)

volume = StringVar(value="100")
volume_label = Label(text='Громкость')
volume_label.place(x=15, y=130)
volume_entry = Entry(width=10, textvariable=volume)
volume_entry.place(x=15, y=150)
volume_entry.bind('<Return>', lambda event: volume_changed())

speed = StringVar(value='1')
speed_lable = Label(text='Скорость')
speed_lable.place(x=100, y=130)
speed_entry = Entry(width=10, textvariable=speed)
speed_entry.place(x=100, y=150)
speed_entry.bind('<Return>', lambda event: speed_changed())

replace_button = Button(text='Вырезать кусок', command=open_replace_window)
replace_button.place(x=40, y=180)

return_backward_button = Button(text='<=', command=return_backward)
return_backward_button.place(x=420, y=12)

return_forward_button = Button(text='=>', command=return_forward)
return_forward_button.place(x=460, y=12)

fragment_to_edit_lable = Label(text="Фрагмент:")
fragment_to_edit_lable.place(x=500, y=15)

fragment_to_edit_from = StringVar(value='0')
fragment_to_edit_from_entry = Entry(width=7, textvariable=fragment_to_edit_from)
fragment_to_edit_from_entry.place(x=565, y=15)

fragment_to_edit_to_lable = Label(text="-->")
fragment_to_edit_to_lable.place(x=610, y=15)

fragment_to_edit_to = StringVar(value='10^00')
fragment_to_edit_to_entry = Entry(width=7, textvariable=fragment_to_edit_to)
fragment_to_edit_to_entry.place(x=640, y=15)

fade_in_button = Button(text='fade in', command=fade_in_fragment)
fade_in_button.place(x=200, y=145)

fade_out_button = Button(text='fade out', command=fade_out_fragment)
fade_out_button.place(x=250, y=145)

fade_in_out_value = StringVar(value='1.0')
fade_in_out_entry = Entry(width=10, textvariable=fade_in_out_value)
fade_in_out_entry.place(x=225, y=180)

root.mainloop()

def open_audio(file: str):
    if file[-3:] == 'mp3':
        return AudioSegment.from_mp3(file)
    elif file[-3:] == 'wav':
        return AudioSegment.from_wav(file)

def change_volume(segment: AudioSegment, value, start=0, end=0):
    if end == 0:
        end = len(segment)
    audio_slice = segment[start:end]
    audio_slice += value
    return segment[:start] + audio_slice + segment[end:]

def change_speed(segment: AudioSegment, value, start=0, end=0):
    if end == 0:
        end = len(segment)
    audio_slice = segment[start:end]
    audio_slice = pydub.effects.speedup(audio_slice, value)
    return segment[:start] + audio_slice + segment[end:]