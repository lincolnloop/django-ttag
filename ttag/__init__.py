try:
    from ttag.args import Arg, BasicArg, BooleanArg, ConstantArg, DateArg, \
        DateTimeArg, IntegerArg, IsInstanceArg, KeywordsArg, \
        ModelInstanceArg, StringArg, TimeArg
    from ttag.core import Tag
    from ttag.exceptions import TagArgumentMissing, TagValidationError
except ImportError:
    # This allows setup.py to skip import errors which may occur if ttag is
    # being installed at the same time as Django.
    pass

VERSION = (1, 0, 'alpha', 3)


def get_version(number_only=False):
    version = [str(VERSION[0])]
    number = True
    for bit in VERSION[1:]:
        if not isinstance(bit, int):
            if number_only:
                break
            number = False
        version.append(number and '.' or '-')
        version.append(str(bit))
    return ''.join(version)
