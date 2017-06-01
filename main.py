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
                output = self.process(self.execute(f))
                if len(output) > 1:
                    out.write(output)
                else:
                    filename = f.split('/')[-1]
                    message = '[{file}]: Nenhum erro de análise estática foi encontrado\n'
                    out.write(message.format(file=filename))


class Cppcheck(Evaluator):

    ErrorId = {
        'memleak': '[{file}:{line}]: (erro) Vazamento de memória',
        'redundantAssignment': '[{file}:{line}]: (erro) Atribuição redundante',
        'uninitvar': '[{file}:{line}]: (erro) Variável não inicializada',
        'nullPointer': '[{file}:{line}]: (erro) Desreferenciamento de ponteiro nulo'
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
            try:
                r = r.decode('utf-8')
                fname, fline, eid, sev, msg = r.split('::')
                filename = fname.split('/')[-1]
                if eid in self.ErrorId:
                    fmt_result.append(self.ErrorId[eid].format(file=filename,
                            line=fline, id=eid, severity=sev, message=msg))
            except:
                continue
        return '\n'.join(fmt_result) + '\n'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(-1)

    ccheck = Cppcheck()
    with open(sys.argv[1]) as infile:
        file_list = infile.read().strip().split('\n')
        ccheck.evaluate(file_list)
