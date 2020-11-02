# -*- coding: utf-8 -*-
"""
sphinxcontirb.autorun
~~~~~~~~~~~~~~~~~~~~~~

Run the code and insert stdout after the code block.

Global options

Add to your ``conf.py`` file::

    autorun_languages = {}
    autorun_languages['pycon_output_encoding'] = 'UTF-8'
    autorun_languages['pycon_input_encoding'] = 'UTF-8'
    autorun_languages['pycon_runfirst'] = '''
    lines of code to run before that included in the runblock
    this code does not appear in the output
    use it to set up formatting, for example
    import numpy as np
    np.set_printoptions(precision=4, suppress=True)
    '''

Set ``pycon_input_encoding`` to UTF-8 if you use Unicode characters in the input file, since this means
the text passed to ``autorun`` will be UTF-8 encoded
Set ``pycon_output_encoding`` to UTF-8 if the output of the code in the runblock produces Unicode
characters, for example ``ansitable``

"""
import os
from subprocess import PIPE, Popen

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.errors import SphinxError

from sphinx_autorun import version

__version__ = version.version


class RunBlockError(SphinxError):
    category = 'runblock error'


class AutoRun(object):
    here = os.path.abspath(__file__)
    pycon = os.path.join(os.path.dirname(here), 'pycon.py')
    config = {
        'pycon': 'python ' + pycon,
        'pycon_prefix_chars': 4,
        'pycon_show_source': False,
        'console': 'bash',
        'console_prefix_chars': 1,
    }

    @classmethod
    def builder_init(cls, app):
        cls.config.update(app.builder.config.autorun_languages)


class RunBlock(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'linenos': directives.flag,
    }
    print("Peter's version")

    def run(self):
        config = AutoRun.config
        language = self.arguments[0]

        if language not in config:
            raise RunBlockError('Unknown language %s' % language)

        # Get configuration values for the language
        args = config[language].split()
        input_encoding = config.get(language+'_input_encoding', 'ascii')
        output_encoding = config.get(language+'_output_encoding', 'ascii')
        prefix_chars = config.get(language+'_prefix_chars', 0)
        show_source = config.get(language+'_show_source', True)
        runfirst = config.get(language+'_runfirst', None)
        runfirst = runfirst.strip().split('\n')

        # Build the code text
        if output_encoding == "ascii":
            bufsize = 1
        else:
            bufsize = 0
        proc = Popen(args, bufsize=bufsize, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        codelines = [line[prefix_chars:] for line in self.content]
        if runfirst is not None:
            codelines = runfirst + codelines
        code = u'\n'.join(codelines).encode(input_encoding)

        # print('-------------------------------')
        # print(code)
        # Run the code
        stdout, stderr = proc.communicate(code)
        # print(stdout)

        # Process output
        if stdout:
            out = stdout.decode(output_encoding)
        if stderr:
            out = stderr.decode(output_encoding)

        nlines = len(runfirst)
        if nlines > 0:
            out = out.split(u'\n')
            out = u'\n'.join(out[nlines:])

        # Get the original code with prefixes
        # print(self.content)
        # print(out)
        if show_source:
            code = u'\n'.join(self.content)
            code_out = u'\n'.join((code, out))
            
        else:
            code_out = out
        # print(code_out)

        literal = nodes.literal_block(code_out, code_out)
        literal['language'] = language
        literal['linenos'] = 'linenos' in self.options
        return [literal]


def setup(app):
    app.add_directive('runblock', RunBlock)
    app.connect('builder-inited', AutoRun.builder_init)
    app.add_config_value('autorun_languages', AutoRun.config, 'env')
