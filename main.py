import flet as ft
from db import main_db


def main(page: ft.Page):
    page.title = 'Todo List'
    page.theme_mode = ft.ThemeMode.DARK
    page.window_maximized = True 

    task_list = ft.Column(spacing=10)


    def load_tasks():
        task_list.controls.clear()
        for task_id, task_text in main_db.get_tasks():
            task_list.controls.append(create_task_row(task_id, task_text))
        page.update()

    def create_task_row(task_id, task_text):
        task_field = ft.TextField(value=task_text, expand=True, dense=True, read_only=True)

        def enable_edit(e):
            task_field.read_only = False
            page.update()

        def save_edit(e):
            main_db.update_task_db(task_id, task_field.value)
            task_field.read_only = True
            page.update()

        return ft.Row([
            task_field,
            ft.IconButton(ft.icons.EDIT, icon_color=ft.colors.YELLOW_400, on_click=enable_edit),
            ft.IconButton(ft.icons.SAVE, icon_color=ft.colors.GREEN_400, on_click=save_edit),
            ft.IconButton(ft.icons.DELETE, icon_color=ft.colors.RED_400, on_click=lambda e: delete_task(task_id))
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    
    def add_task(e):
        if task_input.value.strip():
            task_id = main_db.add_task_db(task_input.value)
            task_list.controls.append(create_task_row(task_id, task_input.value))
            task_input.value = ""
            page.update()

    def delete_task(task_id):
        main_db.delete_task_db(task_id)
        load_tasks()

    task_input = ft.TextField(hint_text='Добавьте задачу', expand=True, dense=True, on_submit=add_task)
    add_button = ft.ElevatedButton("Добавить", on_click=add_task, icon=ft.icons.ADD)

    # page.add(
    #     ft.Column([
    #         ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
    #         task_list
    #     ])
    # )

    content = ft.Container(
        content = ft.Column([
            ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            task_list
        ], alignment=ft.MainAxisAlignment.CENTER), 
        padding=20,
        alignment=ft.alignment.center
    )

    background_image = ft.Image(
        src='/Users/kurmanbek/Desktop/Geeks/Groups_flet/group_51-2_to_do_list/image.png',
        fit=ft.ImageFit.FILL,
        width=page.width,
        height=page.height
    )

    background = ft.Stack([background_image, content])

    def on_resize(e):
        background_image.width = page.width
        background_image.height = page.height
        page.update()

    page.add(background)
    page.on_resized = on_resize

    load_tasks()


if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main)
    

