#!/usr/bin/python3

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

        with open('output.txt', 'w') as out:
            for f in files:
                out.write(self.process(self.execute(f)))


class Cppcheck(Evaluator):
    ErrorId = {
        'memleak': '[{file}:{line}]: (erro) Vazamento de memória',
        'redundantAssignment': '[{file}:{line}]: Descrição redundantAssignment',
        'uninitvar': '[{file}:{line}]: (erro) Variável não inicializada',
        'unreadVariable': '[{file}:{line}]: Descrição unreadVariable'
    }

    def init(self):
        # TODO: Aqui será lido o arquivo CSV para preencher o dict
        pass

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
            r = r.decode('utf-8')
            fname, fline, eid, sev, msg = r.split('::')
            if eid in self.ErrorId:
                fmt_result.append(self.ErrorId[eid].format(file=fname,
                        line=fline, id=eid, severity=sev, message=msg))
        return '\n'.join(fmt_result) + '\n'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(-1)

    ccheck = Cppcheck()
    with open(sys.argv[1]) as infile:
        file_list = infile.read().strip().split('\n')
        ccheck.evaluate(file_list)
