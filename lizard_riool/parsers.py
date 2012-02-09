# (c) Nelen & Schuurmans. GPL licensed, see LICENSE.txt.

"""Module docstring.

This serves as a long usage message.
"""

from models import Put, Riool, Rioolmeting
import logging

logger = logging.getLogger(__name__)


def parse(file_name, objects=[]):
    ""

    classes = {
        ## '*ALGE': None,  # no action
        '*MRIO': Rioolmeting,
        '*PUT': Put,
        '*RIOO': Riool,
        ## '*WAAR': None,  # no action
        }

    prev_obj = None
    with open(file_name) as f:
        for i, line in enumerate(f):
            line_no = i + 1
            line = line.strip("\r\n")
            record_type = line.split('|')[0]
            if record_type not in classes:
                continue
            obj = classes[record_type].\
                parse_line_from_rioolbestand(line, line_no)
            obj.update_coordinates(prev_obj)
            objects.append(obj)
            prev_obj = obj


def main(options, args):
    """
    """

    for file_name in args:
        parse(file_name)


if __name__ == '__main__':
    from optparse import OptionParser
    usage = "usage: %prog [options] input_files..."
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()

    main(options, args)
