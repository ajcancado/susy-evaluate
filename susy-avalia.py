#!/usr/bin/env python3

import json
import os
import shutil
import subprocess
import sys

from abc import ABC, abstractmethod


class Evaluator(ABC):
    """
    Abstract Base Class for a Susy Evaluator
    """

    def init(self):
        pass

    @abstractmethod
    def execute(self, infile):
        pass

    @abstractmethod
    def process(self, result):
        pass

    def evaluate(self, files):
        self.init()

        output = self.process(self.execute(files))
        if len(output) > 0:
            print(output)
        else:
            fnames = ', '.join(map(os.path.basename, files))
            print('[{files}]: Nada a reportar.'.format(files=fnames))


class Cppcheck(Evaluator):
    """
    Cppcheck evaluator for Susy
    """

    # Full path to current file's directory
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    # Config dir name
    CONFIG_DIR = 'susy-avalia-config'

    # Config file name
    CONFIG_FILE = 'susy-avalia-config.json'

    # Full path to configuration file
    CONFIG_PATH = os.path.join(BASE_PATH, CONFIG_DIR, CONFIG_FILE)

    # Cppcheck cfg dir name
    CCCFG_DIR = 'cppcheck-cfg'

    # Full path to cppcheck cfg dir
    CCCFG_PATH = os.path.join(BASE_PATH, CONFIG_DIR, CCCFG_DIR)

    # Control directory name
    CTRL_DIR = '.susy-avalia-ctrl'

    # Full path to control dir
    CTRL_PATH = os.path.join(BASE_PATH, CTRL_DIR)

    # Error message table
    ErrorId = {}

    def init(self):
        if not os.path.exists(self.CTRL_PATH):
            os.mkdir(self.CTRL_PATH)

        cfg_dir = os.path.join(self.CTRL_PATH, 'cfg')
        if not os.path.exists(cfg_dir):
            shutil.copytree(self.CCCFG_PATH,
                    os.path.join(self.CTRL_PATH, 'cfg'))

        cppcheck_bin = os.path.join(self.CTRL_PATH, 'cppcheck')
        if not os.path.exists(cppcheck_bin):
            bin_path = shutil.which('cppcheck')
            if bin_path:
                shutil.copy(bin_path, self.CTRL_PATH)
            else:
                print('Error! No binary cppcheck found!', file=sys.stderr)
                sys.exit(-1)

        with open(self.CONFIG_PATH) as cfg_file:
            self.ErrorId = json.load(cfg_file)

    def execute(self, infiles):
        process = subprocess.Popen([os.path.join(self.CTRL_PATH, 'cppcheck'),
                '--enable=style,unusedFunction',
                '--inconclusive',
                '--template={file}||{line}||{id}||{severity}||{message}'] +
                infiles, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        retcode = process.wait()
        r = process.stdout.read()
        return r

    def process(self, result):
        result = result.strip().split(b'\n')
        result = result[1:]
        fmt_result = []
        for r in result:
            try:
                r = r.decode('utf-8')
                fname, fline, eid, sev, msg = r.split('||')
                fname = os.path.basename(fname)
                if eid in self.ErrorId:
                    fmt_result.append(self.ErrorId[eid].format(file=fname,
                            line=fline, id=eid, severity=sev, message=msg))
            except:
                continue
        if len(fmt_result) >= 12:
            total = len(fmt_result)
            fmt_result = fmt_result[:10]
            fmt_result.append('\nE mais {n} possíveis problemas '
                    'encontrados.'.format(n=total - 10))
        return '\n'.join(fmt_result)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(-1)

    ccheck = Cppcheck()
    with open(sys.argv[1]) as infile:
        file_list_temp = infile.read().strip().split('\n')

        file_list = []
        for f in file_list_temp:
            if os.path.exists(f):
                if f.lower().endswith(('.c', '.cpp', '.h', '.hpp')):
                    file_list.append(f)

        ccheck.evaluate(file_list)
