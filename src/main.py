import flet as ft


def main(page: ft.Page):

    # Create a menu bar passing in arguments to the MenuStyle() to add text and style
    menubar = ft.MenuBar(
        
        # expand argument, sets menu bar to match the width of the window
        expand = True,              
        
        # style argument, takes own arguments to put menu at top of window and the colour
        style = ft.MenuStyle(
            alignment = ft.alignment.top_left,
            bgcolor = ft.Colors.RED_300,
        ),

        # controls argument,  takes own argument of a set of 'Submenu buttons' to display cascading menus
        controls = [
            
            # submenu button for 'Add books'. Add icon, colour change, behaviours/events
            ft.SubmenuButton(

                # set the text of the button and use in built icons. Add style to change to blue when hover over for clarity
                content = ft.Text("Add Books"),
                leading = ft.Icon(ft.Icons.LOCAL_LIBRARY),
                style = ft.ButtonStyle(
                    bgcolor = {ft.ControlState.HOVERED: ft.Colors.BLUE_400},
                ),

                # add some sub menu buttons with text and colour change on hover.
                controls = [
                    ft.MenuItemButton(
                        content = ft.Text("Add Single Book"),
                        style = ft.ButtonStyle(
                            bgcolor = {ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                    ),
                    ft.MenuItemButton(
                        content = ft.Text("Add Multiple Books"),
                        style = ft.ButtonStyle(
                            bgcolor = {ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                    )
                ],
            ),

            # submenu button for 'Edit books'. Add icon, colour change, behaviours/events
            ft.SubmenuButton(
                content = ft.Text("Edit Books"),
                leading = ft.Icon(ft.Icons.EDIT),
                style = ft.ButtonStyle(
                    bgcolor = {ft.ControlState.HOVERED: ft.Colors.BLUE_400},
                ),
                controls = [
                    ft.MenuItemButton(
                        content = ft.Text("Edit Single Book"),
                        style = ft.ButtonStyle(
                            bgcolor = {ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                    ),
                    ft.MenuItemButton(
                        content = ft.Text("Edit Multiple Books"),
                        style = ft.ButtonStyle(
                            bgcolor = {ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                    )
                ],    
            ),

            # submenu button for 'Convert books'. Add icon, colour change, behaviours/events
            ft.SubmenuButton(
                content = ft.Text("Convert Books"),
                leading = ft.Icon(ft.Icons.CHANGE_CIRCLE),
                style = ft.ButtonStyle(
                    bgcolor = {ft.ControlState.HOVERED: ft.Colors.BLUE_400},
                ),
                controls = [
                    ft.MenuItemButton(
                        content = ft.Text("Edit Single Book"),
                        style = ft.ButtonStyle(
                            bgcolor = {ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                    ),
                    ft.MenuItemButton(
                        content = ft.Text("Edit Multiple Book"),
                        style = ft.ButtonStyle(
                            bgcolor = {ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                    )
                ],
            ),

            # submenu button for 'Remove books'. Add icon, colour change, behaviours/events
            ft.SubmenuButton(
                content = ft.Text("Remove Books"),
                leading = ft.Icon(ft.Icons.DELETE),
                style = ft.ButtonStyle(
                    bgcolor = {ft.ControlState.HOVERED: ft.Colors.BLUE_400},
                ),
                controls = [
                    ft.MenuItemButton(
                        content = ft.Text("Remove Single Book"),
                        style = ft.ButtonStyle(
                            bgcolor = {ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                    ),
                    ft.MenuItemButton(
                        content = ft.Text("Remove Multiple Book"),
                        style = ft.ButtonStyle(
                            bgcolor = {ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                    )
                ],
            ),
        ],
    )

    # add the menu bar to the main page
    page.add(ft.Row([menubar]))

    # a DataTable control used to display book info (title, author, series, genre etc) in a table view 
    library_display = ft.DataTable(
        columns = [
            ft.DataColumn(ft.Text("Title")),
            ft.DataColumn(ft.Text("Author")),
            ft.DataColumn(ft.Text("Series")),
            ft.DataColumn(ft.Text("Year"), numeric = True),
            ft.DataColumn(ft.Text("Genre")),
        ],
        rows = [
            ft.DataRow(
                cells = [
                    ft.DataCell(ft.Text("Harry Potter 1")),
                    ft.DataCell(ft.Text("J.K.Rowling")),
                    ft.DataCell(ft.Text("Harry Potter")),
                    ft.DataCell(ft.Text("1997")),
                    ft.DataCell(ft.Text("Fantasy")),
                ]
            )
        ]
    )

    page.add(ft.Column([library_display]))
# run the app
ft.app(main)