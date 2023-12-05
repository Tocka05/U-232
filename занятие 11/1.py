import requests
import json
import tkinter as tk
from tkinter import messagebox


def get_repo_info():
    repo = entry.get()

    try:
        response = requests.get(f'https://api.github.com/users/{repo}')
        if response.status_code == 200:
            repo_data = response.json()
            result = {
                'company': repo_data['company']['login'] if repo_data['company'] else None,
                'created_at': repo_data['created_at'],
                'email': repo_data['email'] if repo_data['email'] else None,
                'id': repo_data['id'],
                'name': repo_data['name'],
                'url': repo_data['url']
            }

            with open('result.json', 'w') as file:
                json.dump(result, file)

            messagebox.showinfo('Success', 'Информация сохранена в файл')
        else:
            messagebox.showerror('Error',
                                 f'Произошла ошибка при получении информации. Код ошибки: {response.status_code}')
    except Exception as e:
        messagebox.showerror('Error', f'Произошла ошибка: {str(e)}')


root = tk.Tk()
root.title('GitHub Repo Info')
root.geometry('400x200')

label = tk.Label(root, text='Введите имя репозитория:')
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text='Получить информацию', command=get_repo_info)
button.pack()

root.mainloop()