import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name="mandalorian game",
    options={'build_exe': {'packages': ['pygame', 'random'],
                           'include_files': ['functions', 'Sons', 'Sprites',
                                             'Fonte', 'classes', 'basic_game_config.py',
                                             'sounds.py', 'sprite_groups.py']}},

    executables=executables

)
