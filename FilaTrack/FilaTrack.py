import flet as ft
import sqlite3

db = sqlite3.connect('FilaTrack_database.db')
c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS history(
        title text,
        material text,
        weight float,
        time integer,
        price float
)""")

def main(page: ft.Page):
    page.title = 'FilaTrack'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 645
    page.window.height = 610
    page.window.resizable = True 

    title = ft.TextField(width=350, bgcolor='#272727', label='Title')
    material = ft.Dropdown(
        label='Material',
        bgcolor='#272727',
        width=170,
        options=[
            ft.dropdown.Option('PLA'),
            ft.dropdown.Option('PETG'),
            ft.dropdown.Option('ABS'),
            ft.dropdown.Option('TPU'),
        ],
        value='PLA',
    )
    weight = ft.TextField(width=170, bgcolor='#272727', label='used weight (g)')
    price = ft.TextField(width=170, bgcolor='#272727', label='filament price / 1kg')
    time = ft.TextField(width=170, bgcolor='#272727', label='printing time (m)')
    electricity = ft.TextField(width=170, bgcolor='#272727', label='electricity (Kč/h)')
    total_price_out = ft.Text('', size=23, color='#8f8fc2', weight=ft.FontWeight.BOLD)
    filament_price = ft.Text(' ', color='#8f8fc2')
    electricity_price = ft.Text('', color='#8f8fc2')

    total_prints = ft.Text('', size=30,)
    total_filament = ft.Text('', size=30)
    total_spent = ft.Text('', size=30)
    total_time = ft.Text('', size=30)

    History = ft.Column([])

    def navigate_to(index):
        def handler(e):
            page.clean()  
            if index == 0:
                page.add(page_calculator1)
            elif index == 1:
                page.add(page_history1)
                load_history()
            elif index == 2:
                page.add(page_stats1)
                stats()
            page.update()
        return handler
    
    def cout():
        weight_value = float(weight.value)
        price_value = float(price.value)
        electricity_value = float(electricity.value)
        time_value = float(time.value)

        filament = round(price_value / 1000 * weight_value, 2)
        electricity_cost = round(time_value / 60 * electricity_value, 2)
        total = filament + electricity_cost

        filament_price.value = filament
        electricity_price.value = electricity_cost
        total_price_out.value = round(total, 2)

    def save():
        weight_value = float(weight.value)
        price_value = float(price.value)
        electricity_value = float(electricity.value)
        title_value = title.value
        material_value = material.value
        time_value = int(time.value) /60
        time_value = round(time_value, 2)
        total = round(price_value / 1000 * weight_value, 2) + round(time_value * electricity_value, 2)
        total = round(total, 2)

        c.execute("INSERT INTO history VALUES (?, ?, ?, ?, ?)", (title_value, material_value, weight_value, time_value, total))
        db.commit()


    def stats():
        c.execute("SELECT COUNT(*) FROM history")
        result = c.fetchone()[0] 
        total_prints.value = result if result else 0

        c.execute("SELECT SUM(weight) FROM history")
        result1 = c.fetchone()[0]
        total_filament.value = round(result1 / 1000 if result1 else 0, 3)

        c.execute("SELECT SUM(price) FROM history")
        result2 = c.fetchone()[0]
        total_spent.value = round(result2, 2) if result2 else 0

        c.execute("SELECT SUM(time) FROM history")
        result3 = c.fetchone()[0]
        total_time.value = round(result3, 2) if result3 else 0

        page.update()

    def delete_db():
        c.execute("DELETE FROM history")
        db.commit()
        stats()
        
    def load_history():
        c.execute("SELECT title, material, weight, time, price FROM history")
        items = c.fetchall()

        rows = []
        for item in items:
            rows.append(
                ft.Row(
                    [
                        ft.Text(item[0], width=80),
                        ft.Text(item[1], width=60),
                        ft.Text(f"{item[2]} g", width=70),
                        ft.Text(f"{item[3]} h", width=60),
                        ft.Text(f"{item[4]} Kč", width=70),
                    ],
                    spacing=3
                )
            )
        History.controls = rows

    side_bar = ft.Container(
        content=ft.Column(
            [   
                ft.Row(
                    [
                        ft.Text('FilaTrack', size=40, weight=ft.FontWeight.W_500, color='#A78BFA'),
                    ]
                ),
                ft.Divider(),
                ft.Row(
                    [
                        ft.IconButton(icon=ft.Icons.CALCULATE, on_click=navigate_to(0)),
                        ft.Text('Calculator')
                    ]
                ),
                ft.Row(
                    [
                        ft.IconButton(icon=ft.Icons.LIST_ALT, on_click=navigate_to(1)),
                        ft.Text('Print History')
                    ]   
                ),
                ft.Row(
                    [
                        ft.IconButton(icon=ft.Icons.BAR_CHART_OUTLINED, on_click=navigate_to(2)),
                        ft.Text('Stats')
                    ]
                )
            ]
        ),
        width=235,
        height=580,
        bgcolor="#16213e",
        padding=20,
        border_radius=10,
    )

    total_price = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text('Total price', color='#8f8fc2')
                    ],
                    spacing=15,
                ),
                ft.Row(
                    [
                        total_price_out,
                        ft.Text(' Kč', size=23, color='#8f8fc2', weight=ft.FontWeight.BOLD),
                    ],
                    spacing=15,
                ),
                ft.Row(
                    [
                        ft.Text('filament: ', color='#8f8fc2'),
                        filament_price,
                        ft.Text(' Kč', color='#8f8fc2'),
                        ft.Text(' - ', color='#8f8fc2'),
                        ft.Text('electricity: ', color='#8f8fc2'),
                        electricity_price,
                        ft.Text(' Kč', color='#8f8fc2'),
                    ]
                ),
            ]
        ),
        width=350,
        height=105,
        padding=10,
        bgcolor="#232364",
        border_radius=10,
        border=ft.Border.all(1, "#333"),

    )

    page_calculator = frame = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text('Printing parameters', size=20)
                    ],
                ),
                ft.Row(
                    [
                        title
                    ]
                ),
                ft.Row(
                    [
                        material,
                        weight,
                    ]
                ),
                ft.Row(
                    [
                        price,
                        time,
                    ]
                ),
                ft.Row(
                    [
                        electricity
                    ]
                ),
                ft.Row(
                    [
                        ft.OutlinedButton(content=ft.Text('calculate'), width=350, on_click=cout),
                    ]
                ),
                ft.Row(
                    [
                        total_price
                    ]
                ),
                ft.Row(
                    [
                        ft.OutlinedButton(content=ft.Text('save'), width=350, on_click=save),
                    ]
                ),
            ],
            spacing=25,
        ),
        width=372,
        height=580,
        padding=10,
        bgcolor="#1e1e3a",
        border_radius=10,
        border=ft.Border.all(1, "#333"),
    )

    page_history = frame = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text('Title', color='grey'),
                        ft.Container(width=25),
                        ft.Text('Material', color='grey'),
                        ft.Text('Weight', color='grey'),
                        ft.Text('Time', color='grey'),
                        ft.Text('Price', color='grey'),
                    ],
                    spacing=20,
                ),
                ft.Divider(),
                History
            ]
        ),
        width=372,
        height=580,
        padding=10,
        bgcolor="#1e1e3a",
        border_radius=10,
        border=ft.Border.all(1, "#333"),
    )

    page_stats = ft.Column(
        [
            ft.Row(
                [
                    ft.Text('Stats', size=25, weight=ft.FontWeight.BOLD)
                ]
            ),
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                            ft.Icon(icon=ft.Icons.PRINT, color='#A78BFA', size=30),
                            ft.Text('Total prints', color='grey', size=20),
                            total_prints
                            ]

                        ),
                        width=180,
                        height=180,
                        padding=10,
                        bgcolor="#1e1e3a",
                        border_radius=10,
                        border=ft.Border.all(1, "#333"),
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                            ft.Icon(icon=ft.Icons.SCALE, color='#13cb7e', size=30),
                            ft.Text('Total filament', color='grey', size=20),
                            ft.Row(
                                [
                                    total_filament,
                                    ft.Text(' kg', size=30)
                                ]
                            )
                            ]

                        ),
                        width=180,
                        height=180,
                        padding=10,
                        bgcolor="#1e1e3a",
                        border_radius=10,
                        border=ft.Border.all(1, "#333"),
                    ),
                ]
            ),
            ft.Row(
                [
                ft.Container(
                    content=ft.Column(
                            [
                            ft.Icon(icon=ft.Icons.PAID, color='#d8a81c', size=30),
                            ft.Text('Total spent', color='grey', size=20),
                            ft.Row(
                                [
                                    total_spent,
                                    ft.Text(' Kč', size=30)

                                ]
                            )
                            ]

                        ),
                    width=180,
                    height=180,
                    padding=10,
                    bgcolor="#1e1e3a",
                    border_radius=10,
                    border=ft.Border.all(1, "#333"),
                ),
                ft.Container(
                    content=ft.Column(
                            [
                            ft.Icon(icon=ft.Icons.SCHEDULE, color='#1c88d7', size=30),
                            ft.Text('Total time', color='grey', size=20),
                            ft.Row(
                                [
                                    total_time,
                                    ft.Text(' h', size=30)
                                ]
                            )
                            ]

                        ),
                    width=180,
                    height=180,
                    padding=10,
                    bgcolor="#1e1e3a",
                    border_radius=10,
                    border=ft.Border.all(1, "#333"),
                ),

                ]
            ),
            ft.Row(
                [
                    ft.OutlinedButton('delete all stats', on_click=delete_db)
                ]
            )
        ]
    )


    page_calculator1 = ft.Row(
        [
                side_bar,
                page_calculator
        ],
            spacing=20,
    )

    page_history1 = ft.Row(
        [
                side_bar,
                page_history
        ],
            spacing=20,
    )

    page_stats1 = ft.Row(
        [
                side_bar,
                page_stats
        ],
            spacing=20,
    )



    page.add(
        ft.Row(
            [
                side_bar,
                page_calculator
            ],
            spacing=20,
        )
    )

    page.update()
ft.app(target=main)
db.commit()
db.close()
