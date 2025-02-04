import curses

def draw_menu(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    height, width = stdscr.getmaxyx()
    box = curses.newwin(height - 2, width - 2, 1, 1)
    box.box()

    items = [
        "🔥 Monitor Personalizado 🔥",
        "• Proceso A: Ejecutando",
        "• Proceso B: Inactivo",
        "• Proceso C: Cargando...",
        "• Proceso D: Finalizado"
    ]

    selected_row = 1 
    
    while True:
        box.erase() 
        box.box() 
        
        for idx, item in enumerate(items):
            if idx == selected_row:
                box.addstr(2 + idx, 4, item, curses.color_pair(2) | curses.A_BOLD)
            else:
                box.addstr(2 + idx, 4, item, curses.color_pair(1))

        box.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and selected_row > 1:
            selected_row -= 1
        elif key == curses.KEY_DOWN and selected_row < len(items) - 1:
            selected_row += 1
        elif key == ord('q'):
            break

        curses.napms(50) 

curses.wrapper(draw_menu)
