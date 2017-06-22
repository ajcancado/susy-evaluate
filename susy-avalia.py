#!/usr/bin/env python3

import json
import os.path
import subprocess
import sys

from abc import ABC, abstractmethod


class Evaluator(ABC):
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

        for f in files:
            output = self.process(self.execute(f))
            if len(output) > 0:
                print(output)
            else:
                print('[{file}]: Nenhum erro de análise estática foi '
                        'encontrado'.format(file=os.path.basename(f)))


class Cppcheck(Evaluator):
    # Full path to current file's directory
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    # Full path to configuration file
    CONFIG_PATH = BASE_PATH + '/susy-avalia-config.json'

    ErrorId = {}

    def init(self):        
        with open(self.CONFIG_PATH) as cfg_file:
            self.ErrorId = json.load(cfg_file)

    def execute(self, infile):
        process = subprocess.Popen(['cppcheck', '--enable=style',
                '--template={file}::{line}::{id}::{severity}::{message}',
                infile], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
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
                fname, fline, eid, sev, msg = r.split('::')
                fname = os.path.basename(fname)
                if eid in self.ErrorId:
                    fmt_result.append(self.ErrorId[eid].format(file=fname,
                            line=fline, id=eid, severity=sev, message=msg))
            except:
                continue
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
                if f.lower().endswith(('.c', '.cpp')):
                    file_list.append(f)

        ccheck.evaluate(file_list)
