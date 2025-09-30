# Traffic signal - input color (red/Yellow/Green) and print action (stop/slow/go)
color = input("Enter the Traffic signal color (red/yellow/green) : ")
if color == 'red' or color == 'RED':
    print("Stop")
elif color == 'yellow' or color == 'YELLOW':
    print("Slow")
elif color == 'green' or color == 'GREEN':
    print("go")
else:
    print("Plz Enter the valide traffic color (red/ yellow / green)")
    