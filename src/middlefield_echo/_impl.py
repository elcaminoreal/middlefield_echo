from __future__ import print_function

import typing

from caparg import command, option
import middlefield

@middlefield.COMMANDS.command(
                             parser=command('',
                                            what=option(type=typing.List[str],
                                                        have_default=True)),
                             dependencies=['echo_printer'])
def echo(args, dependencies):
    dependencies['echo_printer'](*args['what'])

@middlefield.COMMANDS.dependency()
def echo_printer(dependencies, maybe_dependencies):
    return print
