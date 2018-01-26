import random
from time import time
import datetime
import argparse
import os
import sys
import textwrap

from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

args = None
__version__ = "1.0.0"
__doc__     = """Math equation pdf generator"""

def equation():
    a = random.randint(1,9)
    if args.operation == 'all':
    	sign = ' + ' if random.randint(0,1)==1 else ' - '
    else:
    	sign = ' ' + args.operation + ' '
    b = str(random.randint(1,a if sign ==" - " else 9))
    return str(a)+sign+b+' ='

def main():
    if args.version :
        print( "math_equation.py v%s" % (__version__, ) )
        sys.exit(0)

    random.seed(time())
    current_date = str(datetime.date.today())
    filename = current_date + '.pdf'
    doc = SimpleDocTemplate(filename) 
    elements = []
    
    ptext = '<font size=24>%s</font>' % current_date
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    elements.append(Paragraph(ptext, styles["Center"]))
    data = []
    for i in range(39):
        data.append([])
        line = ""
        for j in range(3):
            data[i].append(equation())
    
    t = Table(data, 170, 50)
    t.setStyle(TableStyle([('FONTSIZE', (0,0),(-1,-1),24)]))
    elements.append(t)
    doc.build(elements)

    # if (todo):
    #     os.system("start " + filename)
    # else:
    #     os.system("open " + filename)

if __name__ == '__main__':
  
    description = """\
        This script can be used to generate set of math equations in the pdf document 
        """
    example_of_use = """ 
            Set the IP and port: python switch_disturber.py -i 192.168.1.50 -p 60001
        """
    parser = argparse.ArgumentParser \
        ( formatter_class=argparse.ArgumentDefaultsHelpFormatter
        , description = textwrap.dedent (description)
        , epilog = textwrap.dedent (example_of_use)
        )

    parser.add_argument \
        ( "-v", "--version"
        , action = "store_true"
        , help = "show program's version number and exit"
        )

    parser.add_argument \
        ( "-o", "--operation"
        , type=str
        , default="all"
        , help = "Choose operations for equation: +, -, all"        
        )

    args = parser.parse_args () # parse the command line
    main()
    
    
