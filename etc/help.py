def show_help():
    commands="help exit clear cls echo reset ls dir cd mkdir rmdir(+sudo) opendir run cat touch"
    commands=commands.replace(" ","\n")
    print(commands)