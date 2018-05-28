import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../')))

import mailsender.html_template as html_template
import mailsender.mail as mail
import mailsender.secrets as secrets
