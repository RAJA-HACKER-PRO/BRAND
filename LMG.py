import platform

arch = platform.architecture()[0]

if arch == "32bit":
    from LMG_32bit import approval
else:
    from LMG_64bit import approval


main()
