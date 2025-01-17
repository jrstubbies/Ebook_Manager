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
            
            # submenu button for the 'Add books' submenu. Allows for addition of icon, colour change, behaviours
            ft.SubmenuButton(
                content = ft.Text("Add Books"),
                leading = ft.Icon(ft.Icons.LOCAL_LIBRARY),
                style = ft.ButtonStyle(
                    bgcolor = {ft.ControlState.HOVERED: ft.Colors.BLUE_400},
                ),
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

            # submenu button for the 'Edit books' submenu. Allows for addition of icon, colour change, behaviours
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

            # submenu button for the 'Convert books' submenu. Allows for addition of icon, colour change, behaviours
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

            # submenu button for the 'Remove books' submenu. Allows for addition of icon, colour change, behaviours
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


# run the app
ft.app(main)