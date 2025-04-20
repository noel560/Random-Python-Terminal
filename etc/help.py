def show_help():
    commands="help exit clear cls echo reset ls dir cd mkdir rmdir opendir run cat touch rm whereis"
    commands=commands.replace(" ","\n")
    print(commands)