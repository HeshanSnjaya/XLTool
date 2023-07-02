import tkinter
import openpyxl as xl
import pandas as pd
import customtkinter as tk
from customtkinter import filedialog
from tkinter.messagebox import askyesno

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("500x250")
root.title('XL Tool')


def open_file():
    while True:
        try:
            open_file_path = filedialog.askopenfilename(filetypes=[("Excel file", '.xlsx')])
            print(open_file_path)
            root.after(500, move_progress)
            wb = xl.load_workbook(open_file_path)
            ws = wb.active
            root.after(500, move_progress)
            break
        except:
            answer_file_add = askyesno(title='Add File Error',
                                          message='Unable to add the file.\nDo you want to try again?')
            if not answer_file_add:
                default_move_progress()
                return

    answer_cofirmation = askyesno(title='confirmation',
                      message='File is successfully added.\nDo you want to save?')
    if answer_cofirmation:
        while True:
            try:
                save_file_path = filedialog.asksaveasfilename(filetypes=[("Excel file", '.xlsx')])
                root.after(500, move_progress)
                for merge in list(ws.merged_cells):
                    ws.unmerge_cells(range_string=str(merge))
                root.after(500, move_progress)
                df = pd.DataFrame(ws.values)
                root.after(500, move_progress)
                df = df.replace('nan', pd.NA)
                root.after(500, move_progress)
                df.dropna(how='all', inplace=True, axis=0)
                root.after(500, move_progress)
                df.dropna(how='all', inplace=True, axis=1)
                root.after(500, move_progress)
                df.to_excel(save_file_path+'.xlsx')
                root.after(500, move_progress)
                break
            except:
                answer_file_save = askyesno(title='Save File Error',
                                           message='Unable to save the file.\nDo you want to try again?')
                if not answer_file_save:
                    default_move_progress()
                    return
        tkinter.messagebox.showinfo(title=None, message='File saved.')
        default_move_progress()
        return
    else:
        default_move_progress()
        return

def move_progress():
    current_width = sub_progress['width']
    sub_progress.configure(width= current_width+20)

def default_move_progress():
    sub_progress.configure(width=10)

if __name__ == '__main__':
    frame=tk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60 , fill="both", expand=True)

    label= tk.CTkLabel(master=frame, text="XL Tool",font= ("Roboto",24))
    label.pack(pady=12, padx=10)

    button_1=tk.CTkButton(master=frame, text='Open File',command=open_file)
    button_1.pack(pady=12,padx=10)

    progress_frame= tk.CTkFrame(root, fg_color='black')

    sub_progress=tk.CTkFrame(progress_frame, fg_color='blue')
    sub_progress.pack_propagate(False)
    sub_progress.configure(width=10 ,height=10)
    sub_progress.pack(side=tk.LEFT)

    progress_frame.pack_propagate(False)
    progress_frame.configure(width=200 ,height=10)
    progress_frame.pack(pady=10)

root.mainloop()



